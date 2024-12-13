
def count_cost(A, B, P):
	min_cost = None
	for A_count in range(101):
		for B_count in range(101):
			X = A[0] * A_count + B[0] * B_count
			Y = A[1] * A_count + B[1] * B_count
			if X == P[0] and Y == P[1]:
				cost = 3 * A_count + 1 * B_count
				if min_cost is None or cost < min_cost:
					min_cost = cost	
	return min_cost if min_cost != None else 0

A = (0, 0)
B = (0, 0)
Prize = (0, 0)
ans = 0
with open('13.in', 'r') as file:
	for line in file:
		if len(line) <= 2:
			continue
		inp = line.strip('\n').split(' ')
		if inp[1] == 'A:':
			A = (int(inp[2][2:].strip(',')), int(inp[3][2:]))
		elif inp[1] == 'B:':
			B = (int(inp[2][2:].strip(',')), int(inp[3][2:]))
		else:
			Prize = (int(inp[1][2:].strip(',')), int(inp[2][2:]))
		ans += count_cost(A, B, Prize)
	print(ans)
