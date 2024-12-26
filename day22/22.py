MOD = 16777216

def secret(n, N):
	for _ in range(N):
		n = ((64*n) ^ n) % MOD
		n = ((n // 32) ^ n) % MOD
		n = ((2048*n) ^ n) % MOD
		if N == 10:
			print(n)
	print(n)
	return n
ans = 0


with open("22.in", "r") as file:
	for line in file:
		n = int(line.strip('\n'))
		ans += secret(n, 2000)
	print(ans)
