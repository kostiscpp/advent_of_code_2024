G = []

def is_valid(x, y, n, m):
	return 0 <= x < n and 0 <= y < m and G[x][y] != '#'

with open("20.in", "r") as file:
	for line in file:
		G.append(line.strip('\n'))
	
	n, m = len(G), len(G[0])
	start = (-1, -1)
	end = (-1, -1)
	for row in range(n):
		for col in range(m):
			if G[row][col] == 'S':
				start = (row, col)
			if G[row][col] == 'E':
				end = (row, col)
	dists = [[ float('inf') for col in range(m)] for row in range(n)]
	dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	queue = [start]
	visited = {start}
	dists[start[0]][start[1]] = 0
	d = 0
	while queue:
		xq, yq = queue.pop(0)
		moved = False
		if (xq, yq) == end:
			dists[xq][yq] = d
			break
		for dx, dy in dirs:
			xn, yn = xq + dx, yq + dy
			if is_valid(xn, yn, n, m) and (xn, yn) not in visited:
				queue.append((xn, yn))
				visited.add((xn, yn))
				dists[xn][yn] = d+1
				d += 1
	diste = [[ float('inf') for col in range(m)] for row in range(n)]
	queue = [end]
	visited = {end}
	diste[end[0]][end[1]] = 0
	d = 0
	while queue:
		xq, yq = queue.pop(0)
		if (xq, yq) == start:
			diste[xq][yq] = d
			break
		for dx, dy in dirs:
			xn, yn = xq + dx, yq + dy
			if is_valid(xn, yn, n, m) and (xn, yn) not in visited:
				queue.append((xn, yn))
				visited.add((xn, yn))
				diste[xn][yn] = d+1
				d += 1
	ans = 0	
	total = dists[end[0]][end[1]]
	for row in range(n):
		for col in range(m):
			if G[row][col] == '#':
				for dx, dy in dirs:
					for ddx, ddy in dirs:
						xn, yn = row + dx, col + dy
						xnn, ynn = row + ddx, col + ddy
						if (xn, yn) != (xnn, ynn) and is_valid(xn, yn, n, m) and is_valid(xnn, ynn, n, m):
							ans += ((total - (dists[xn][yn] + 2 + diste[xnn][ynn])) > 99) 
	print(ans)
	
