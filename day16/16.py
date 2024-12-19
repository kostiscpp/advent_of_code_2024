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
			return cost

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

	return None

G = []
with open('16.in', 'r') as file:
	for line in file:
		G.append(line.strip('\n'))

print(solve_maze(G))
