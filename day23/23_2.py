G = dict()

def bron_kerbosch(R, P, X, G):
	if not P and not X:
		yield R
    
	while P:
		v = P.pop()
		yield from bron_kerbosch(
			R.union({v}),
			P.intersection(G[v]),
			X.intersection(G[v]),
			G
		)
		X.add(v)

def find_largest_clique(G):
	G = {key: set(G[key]) for key in G}
	all_nodes = set(G.keys())
	clique = max(list(bron_kerbosch(set(), all_nodes, set(), G)), key=len)
	return list(sorted(clique))

with open('23.in', 'r') as file:
	for line in file:
		if line == '\n':
			break
		a, b = line.strip('\n').split('-')
		if a not in G:
			G[a] = set()
		G[a].add(b)
		if b not in G:
			G[b] = set()
		G[b].add(a)

	print(','.join(find_largest_clique(G)))
