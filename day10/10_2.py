def is_valid(x, y, n, m):
	return (x >= 0 and y >=0 and x < n and y < m)

def is_path(G, s):
	ans = 0
	visited = set()
	nines = 0
	n, m = len(G), len(G[0])
	queue = [s]
	dirs = [(-1,0), (1,0), (0,-1), (0,1)]
	while queue:
		x, y = queue.pop(0)
		if G[x][y] == 9:
			nines += 1
			continue
		for dx, dy in dirs:
			xn, yn = x + dx, y + dy
			if is_valid(xn, yn, n, m):
				if G[xn][yn] - G[x][y] == 1:
					queue.append((xn, yn))
	return nines


def count_paths(G):
	ans = 0
	for r in range(len(G)):
		for c in range(len(G[0])):
			if G[r][c] == 0:
				ans += is_path(G, (r,c))
	return ans


G = []
with open('10.in', 'r') as file:
	for line in file:
		G.append(list(map(int, line.strip('\n'))))

print(count_paths(G))
