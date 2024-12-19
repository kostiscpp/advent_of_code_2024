grid = [["." for _ in range(71)] for _ in range(71)]

def is_valid(x, y, n, m):
	return 0 <= x < n and 0 <= y < m and grid[y][x] != "#"



with open("18.in", "r") as file:
	for count, line in enumerate(file):
		if count < 3016:
			x, y = tuple(map(int, line.strip('\n').split(',')))
			grid[y][x] = "#"
			dirs = [(0,1), (1, 0), (0, -1), (-1, 0)]
			queue = [(0,0, 0)]
			visited = {(0,0)}
			while queue:
				xq, yq, dist = queue.pop(0)
				if (xq, yq) == (70, 70):
					ans = dist
					break
				for dx, dy in dirs:
					xn, yn = xq + dx, yq + dy
					if is_valid(xn, yn, 71, 71) and (xn, yn) not in visited:
						queue.append((xn, yn, dist + 1))
						visited.add((xn, yn))
				ans = -1
			if ans == -1:
				print(x, y)
				break
