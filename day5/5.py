def count_pages(G, Up):
	ans = 0
	for u in Up:
		good = True
		for i in range(len(u)):
			for j in range(i+1, len(u)):
				if u[i] in G[u[j]]:
					good = False
					break
			if not good:
				break
		if good:
			ans += int(u[len(u)//2])
	return ans

Ord = {}
Upd = []
with open('5.in', 'r') as file:
	for line in file:
		line = line.strip('\n')
		if len(line) == 5: 
			x, y = line.split('|')
			if x not in Ord:
				Ord[x] = []
			Ord[x].append(y)
		elif len(line) > 1:
			Upd.append(line.split(','))

print(count_pages(Ord, Upd))
