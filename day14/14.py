
quads = [0, 0, 0, 0]

def update(N, M, p, v, s):
	p_new = ((p[0] + s*v[0]) % N, (p[1] + s*v[1]) % M)
	if p_new[0] < N//2 and p_new[1] < M//2:
		quads[0] += 1
	elif p_new[0] > N//2 and p_new[1] < M//2:
		quads[1] += 1
	elif p_new[0] < N//2 and p_new[1] > M//2:
		quads[2] += 1
	elif p_new[0] > N//2 and p_new[1] > M//2:
		quads[3] += 1
	return quads

with open('14.in', 'r') as file:
	for line in file:
		inp = line.strip('\n').split(' ')
		p, v = (tuple(map(int, inp[0][2:].split(','))), tuple(map(int, inp[1][2:].split(','))))
		update(101, 103, p, v, 100)
	print(quads[0]*quads[1]*quads[2]*quads[3])
