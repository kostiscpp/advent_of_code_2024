def count_score(grid, dirs):
	dirs_map = {">" : (1, 0) ,"<" : (-1, 0) ,"^" : (0, -1) ,"v" : (0, 1) }
	n, m = len(grid), len(grid[0])
	robot = (-1, -1)
	for x in range(m):
		for y in range(n):
			if grid[y][x] == "@":
				robot = (x, y)
				break
		
	for d in dirs:
		d_x, d_y = dirs_map[d]
		if 0 <= robot[0] + d_x < m and 0 <= robot[1] + d_y < n and grid[robot[1] + d_y][robot[0] + d_x] != "#":
			i = 1
			while 0 <= robot[0] + i*d_x < m and 0 <= robot[1] + i*d_y < n and grid[robot[1] + i*d_y][robot[0] + i*d_x] == "O":
				i += 1
			if 0 <= robot[0] + i*d_x < m and 0 <= robot[1] + i*d_y < n and grid[robot[1] + i*d_y][robot[0] + i*d_x] != "#":
				if grid[robot[1] + d_y][robot[0] + d_x] == "O":
					grid[robot[1] + i*d_y][robot[0] + i*d_x] = "O" 
				grid[robot[1] + d_y][robot[0] + d_x] = "@"
				grid[robot[1]][robot[0]] = "."
				robot = (robot[0] + d_x, robot[1] + d_y)
	ans = 0
	for x in range(m):
		for y in range(n):
			if grid[y][x] == "O":
				ans += x + 100*y
	return ans

def fix_line(line):
	nl = []
	for x in line:
		if x == "O":
			nl.append("[")
			nl.append("]")
		elif x == "@":
			nl.append(".")
			nl.append("@")
		else:
			nl.append(x)
			nl.append(x)

	return nl
grid = []
dirs = ""
with open('15.in', 'r') as file:
	for line in file:
		if line[0] == '#':
			grid.append(fix_line([x for x in line.strip('\n')]))
		elif line[0] in ['>','<','^','v']:
			dirs += line.strip('\n')
	print(count_score(grid, dirs))
