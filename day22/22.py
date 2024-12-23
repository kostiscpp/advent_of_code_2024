def secret(n, N):
	for _ in range(N):
		n = 64*n ^ n
	return n


with open("22.in", "r") as file:
	for line in file:
		n = int(line.strip('\n')
		ans += secret(n, 2000)
