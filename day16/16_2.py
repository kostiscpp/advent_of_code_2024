import heapq

def solve_maze(maze):
	rows = len(maze)
	cols = len(maze[0])

	start = None
	end = None

	for r in range(rows):
		for c in range(cols):
			if maze[r][c] == 'S':
				start = (r, c)
			elif maze[r][c] == 'E':
				end = (r, c)
	
	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	dist = [[[float('inf')] * 4 for _ in range(cols)] for __ in range(rows)]

	start_direction = 1
	dist[start[0]][start[1]][start_direction] = 0

	pq = [(0, start[0], start[1], start_direction)]

	while pq:
		cost, r, c, d = heapq.heappop(pq)
		
		if (r, c) == end:
			break	
		if cost > dist[r][c][d]:
			continue

		dr, dc = directions[d]
		nr, nc = r + dr, c + dc
		if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
			new_cost = cost + 1
			if new_cost < dist[nr][nc][d]:
				dist[nr][nc][d] = new_cost
				heapq.heappush(pq, (new_cost, nr, nc, d))

		left_d = (d - 1) % 4
		right_d = (d + 1) % 4
		if cost + 1000 < dist[r][c][left_d]:
			dist[r][c][left_d] = cost + 1000
			heapq.heappush(pq, (cost + 1000, r, c, left_d))
		if cost + 1000 < dist[r][c][right_d]:
			dist[r][c][right_d] = cost + 1000
			heapq.heappush(pq, (cost + 1000, r, c, right_d))


	min_cost = min(dist[end[0]][end[1]][d] for d in range(4))

	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

	stack = []
	visited_states = set()

	for d in range(4):
		if dist[end[0]][end[1]][d] == min_cost:
			stack.append((end[0], end[1], d))
			visited_states.add((end[0], end[1], d))

	shortest_path_tiles = set()

	while stack:
		r, c, d = stack.pop()

		shortest_path_tiles.add((r, c))

		current_cost = dist[r][c][d]

		dr, dc = directions[d]
		prev_r, prev_c = r - dr, c - dc
		if 0 <= prev_r < rows and 0 <= prev_c < cols and maze[prev_r][prev_c] != '#':
			if current_cost - 1 >= 0:
				if dist[prev_r][prev_c][d] == current_cost - 1:
					prev_state = (prev_r, prev_c, d)
					if prev_state not in visited_states:
						visited_states.add(prev_state)
						stack.append(prev_state)

		left_d = (d + 1) % 4  
		if current_cost - 1000 >= 0 and dist[r][c][left_d] == current_cost - 1000:
			prev_state = (r, c, left_d)
			if prev_state not in visited_states:
				visited_states.add(prev_state)
				stack.append(prev_state)

		right_d = (d - 1) % 4
		if current_cost - 1000 >= 0 and dist[r][c][right_d] == current_cost - 1000:
			prev_state = (r, c, right_d)
			if prev_state not in visited_states:
				visited_states.add(prev_state)
				stack.append(prev_state)

	
	return len(shortest_path_tiles)

G = []
with open('16.in', 'r') as file:
	for line in file:
		G.append(line.strip('\n'))

print(solve_maze(G))
