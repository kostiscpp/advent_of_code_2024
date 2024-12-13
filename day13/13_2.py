
def count_cost(A, B, P):
	det = A[0]*B[1] - B[0]*A[1]
	if det == 0:
		return 0
	Ac = P[0]*B[1] - P[1]*B[0]
	Bc = P[1]*A[0] - P[0]*A[1]
	
	if Ac % det != 0 or Bc % det != 0:
		return 0
	
	Acount = Ac // det
	Bcount = Bc // det
	
	if Acount < 0 or Bcount < 0:
		return 0

	return Acount*3 + Bcount

A = (0, 0)
B = (0, 0)
Prize = (0, 0)
lmao = 10000000000000
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
			Prize = (Prize[0] + lmao, Prize[1] + lmao)
		ans += count_cost(A, B, Prize)
	print(ans)
