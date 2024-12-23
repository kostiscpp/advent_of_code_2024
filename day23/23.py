G = dict()

with open('23.in', 'r') as file:
	for line in file:
		if line == '\n':
			break
		a, b = line.strip('\n').split('-')
		if a not in G:
			G[a] = []
		G[a].append(b)
		if b not in G:
			G[b] = []
		G[b].append(a)
	ans = 0
	for a in G.keys():
		for b in G[a]:
			for c in G.keys():
				if a in G[c] and b in G[c] and 't' in ''.join([a[0], b[0], c[0]]):
					ans += 1
	print(ans//6)
