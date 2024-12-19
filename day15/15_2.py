def can_push(x, y, dy, grid):
	n, m = len(grid), len(grid[0])
	b = ["[", "]"]
	b2x = { "[" : 1, "]" : -1}
	if not(0 <= y + dy < n and grid[y + dy][x] in b):
		return []
	
	y += dy
	boxes = set()
	prev = set()
	boxes.add((x, y))
	boxes.add((x + b2x[grid[y][x]], y))
	prev.add((x, y))
	prev.add((x + b2x[grid[y][x]], y))
	while 0 <= y + dy < n and prev != set():
		temp = set()
		y += dy
		for bx, by in prev:
			if grid[y][bx] in b:
				temp.add((bx, y))
				boxes.add((bx, y))
				temp.add((bx + b2x[grid[y][bx]], y))
				boxes.add((bx + b2x[grid[y][bx]], y))
			elif grid[y][bx] == "#":
				return []
		prev = temp
	for xp, yp in boxes:
		if not(0 <= yp + dy < n) or grid[yp + dy][xp] == "#":
			return []
	return boxes


def count_score(grid, dirs):
	dirs_map = {">" : (1, 0) ,"<" : (-1, 0) ,"^" : (0, -1) ,"v" : (0, 1) }
	n, m = len(grid), len(grid[0])
	robot = (-1, -1)
	for x in range(m):
		for y in range(n):
			if grid[y][x] == "@":
				robot = (x, y)
				break
	prev = -1
	for d in dirs:
		d_x, d_y = dirs_map[d]
		if 0 <= robot[0] + d_x < m and 0 <= robot[1] + d_y < n and grid[robot[1] + d_y][robot[0] + d_x] != "#":
			if d_x != 0:
				i = 1
				while 0 <= robot[0] + i*d_x < m and grid[robot[1]][robot[0] + i*d_x] in ["[", "]"]:
					i += 1
				if 0 <= robot[0] + i*d_x < m and grid[robot[1]][robot[0] + i*d_x] != "#":
					if grid[robot[1]][robot[0] + d_x] in ["[", "]"]:
						br = ["[", "]"] if d_x > 0 else ["]", "["]
						for j in range(2, i+1):
							grid[robot[1]][robot[0] + j*d_x] = br[j % 2]
					grid[robot[1]][robot[0] + d_x] = "@"
					grid[robot[1]][robot[0]] = "."
					robot = (robot[0] + d_x, robot[1])
			else:
				boxes = can_push(robot[0], robot[1], d_y, grid)
				global old_grid
				old_grid = [[y for y in x] for x in grid]
				for x, y in boxes:
					grid[y][x] = "."
				for x, y in boxes:
					grid[y + d_y][x] = old_grid[y][x]
				if boxes != [] or grid[robot[1] + d_y][robot[0]] == ".":
					grid[robot[1] + d_y][robot[0]] = "@"
					grid[robot[1]][robot[0]] = "."
					robot = (robot[0], robot[1] + d_y)
			bad = False
			for y in range(n):
				for x in range(m):
					if (grid[y][x] == "[" and grid[y][x+1] != "]") or (grid[y][x] == "]" and grid[y][x-1] != "["):
						bad = True
						break
			if bad:
				break
	ans = 0
	for x in range(m):
		for y in range(n):
			if grid[y][x] == "[":
				ans += x + 100*y
	return ans

def fix_line(line):
	nl = []
	for x in line:
		if x == "O":
			nl.append("[")
			nl.append("]")
		elif x == "@":
			nl.append("@")
			nl.append(".")
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
