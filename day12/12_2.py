from collections import defaultdict, deque

def solve(garden_map):
    rows = len(garden_map)
    cols = len(garden_map[0])

    visited = [[False]*cols for _ in range(rows)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

    def get_region_cells(sr, sc):
        region_type = garden_map[sr][sc]
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        cells = []
        while q:
            r, c = q.popleft()
            cells.append((r, c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not visited[nr][nc] and garden_map[nr][nc] == region_type:
                        visited[nr][nc] = True
                        q.append((nr, nc))
        return cells

    def get_boundary_edges(cells):
        # Each cell contributes boundary edges where it meets non-region cells or edges of the grid
        cell_type = garden_map[cells[0][0]][cells[0][1]]
        edges = set()
        cell_set = set(cells)
        for (r, c) in cells:
            # Up
            if r == 0 or garden_map[r-1][c] != cell_type:
                edges.add(((r,c),(r,c+1)))
            # Down
            if r == rows-1 or garden_map[r+1][c] != cell_type:
                edges.add(((r+1,c),(r+1,c+1)))
            # Left
            if c == 0 or garden_map[r][c-1] != cell_type:
                edges.add(((r,c),(r+1,c)))
            # Right
            if c == cols-1 or garden_map[r][c+1] != cell_type:
                edges.add(((r,c+1),(r+1,c+1)))
        return edges

    def build_graph(edges):
        adj = defaultdict(list)
        for p1, p2 in edges:
            adj[p1].append(p2)
            adj[p2].append(p1)
        return adj

    def find_connected_components(adj):
        visited_nodes = set()
        components = []
        for start in adj.keys():
            if start not in visited_nodes:
                # BFS or DFS to find a connected component
                comp = []
                stack = [start]
                visited_nodes.add(start)
                while stack:
                    node = stack.pop()
                    comp.append(node)
                    for nxt in adj[node]:
                        if nxt not in visited_nodes:
                            visited_nodes.add(nxt)
                            stack.append(nxt)
                components.append(comp)
        return components

    def extract_loop(adj, component):
        # component is all vertices in one connected component
        # Since each vertex should have degree 2, this component forms a single cycle.
        # Find the lowest-leftmost vertex to start for consistency
        start = min(component, key=lambda x: (x[0], x[1]))

        loop = [start]
        # Follow the cycle
        # Each vertex has exactly 2 neighbors; one will lead to the next step.
        prev = None
        cur = start

        while True:
            neighbors = adj[cur]
            # cur has 2 neighbors; pick the one that is not prev
            if prev is None:
                # first step: just pick either neighbor
                nxt = neighbors[0] if neighbors[0] != cur else neighbors[1]
            else:
                nxt = neighbors[0] if neighbors[0] != prev else neighbors[1]
            if nxt == start:
                # loop completed
                loop.append(start)
                break
            loop.append(nxt)
            prev, cur = cur, nxt

        return loop

    def count_sides(loop):
        # loop is closed (last == first)
        def direction(p1,p2):
            r1,c1 = p1
            r2,c2 = p2
            return 'H' if r1 == r2 else 'V'
        
        sides = 0
        current_dir = None
        for i in range(len(loop)-1):
            d = direction(loop[i], loop[i+1])
            if d != current_dir:
                sides += 1
                current_dir = d
        return sides

    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region_cells = get_region_cells(r, c)
                area = len(region_cells)
                if area == 0:
                    continue
                edges = get_boundary_edges(region_cells)
                if not edges:
                    # single cell would still have edges, but just in case
                    continue
                adj = build_graph(edges)
                # Each connected component in adj is one loop
                components = find_connected_components(adj)
                total_sides = 0
                for comp in components:
                    loop = extract_loop(adj, comp)
                    total_sides += count_sides(loop)
                
                total_price += area * total_sides

    return total_price


if __name__ == "__main__":
    garden_map = []
    with open('12ex.in', 'r') as file:
        for line in file:
            garden_map.append(line.strip('\n'))
    
    result = solve(garden_map)
    
    print(result) 

