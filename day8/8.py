from math import gcd
G = []
with open('8.in', 'r') as file:
	for line in file:
		G.append(line.strip('\n'))
	freq = {}
	rows, cols = len(G), len(G[0])
	for r in range(rows):
		for c in range(cols):
			ch = G[r][c]
			if ch != '.':
				if ch not in freq:
					freq[ch] = []
				freq[ch].append((r, c))
	
	def add_points(rA, cA, rB, cB):
		dr = rB - rA
		dc = cB - cA
		g = gcd(dr, dc)
		dr //= g
		dc //= g
		rr, cc = rA, cA
		while 0 <= rr < rows and 0 <= cc < cols:
			antinodes.add((rr, cc))
			rr += dr
			cc += dc
		rr, cc = rA - dr, cA - dc
		while 0 <= rr < rows and 0 <= cc < cols:
			antinodes.add((rr, cc))
			rr -= dr
			cc -= dc

	antinodes = set()
	for fr, pos in freq.items():
		n = len(pos)
		for i in range(n):
			rA, cA = pos[i]
			for j in range(i+1, n):
				rB, cB = pos[j]
				add_points(rA, cA, rB, cB)
print(len(antinodes))
