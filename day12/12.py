def is_convex(x, y, n, m, G, char):
	return (not(0 <= x < n and 0 <= y < m) or G[x][y] != char)
def same(x, y, n, m, G, char):
	return 0 <= x < n and 0 <= y < m and G[x][y] == char

def visit(G, s , visited):
	dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	queue = [s]
	char = G[s[0]][s[1]]
	visited.add(s)
	coords = [s]
	n, m = len(G), len(G[0])
	ans = 0
	area = 1
	while queue:
		x, y = queue.pop(0)
		for i in range(len(dirs)):
			xn, yn = x + dirs[i][0], y + dirs[i][1]
			if 0 <= xn < n and 0 <= yn < m and (xn, yn) not in visited:
				if G[xn][yn] == char:
					queue.append((xn, yn))
					visited.add((xn, yn))
					area += 1
			xnn, ynn = x +  dirs[(i + 1) % 4][0], y + dirs[(i + 1) % 4][1]
			xdn, ydn = xn + xnn - x, yn + ynn - y
			ans += (is_convex(xn, yn, n, m, G, char) and is_convex(xnn, ynn, n, m, G, char))
			ans += (is_convex(xdn, ydn, n, m, G, char) and same(xn, yn, n, m, G, char) and same(xnn, ynn, n, m, G, char))
	return ans * area, visited
	


def count_areas(G):
	visited = set()
	ans = 0
	for r in range(len(G)):
		for c in range(len(G[0])):
			if (r, c) not in visited:
				counted , visited = visit(G, (r, c), visited)
				ans += counted
	return ans

G = []
with open('12.in', 'r') as file:
	for line in file:
		G.append(line.strip('\n'))
	print(count_areas(G))
