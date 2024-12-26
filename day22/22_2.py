MOD = 16777216

def secret(n, N):
	prices = [n % 10]
	for _ in range(N):
		n = ((64*n) ^ n) % MOD
		n = ((n // 32) ^ n) % MOD
		n = ((2048*n) ^ n) % MOD
		prices.append(n % 10)
	changes = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
	return changes, prices

ans = {}

with open("22.in", "r") as file:
	for line in file:
		n = int(line.strip('\n'))
		chs, prs = secret(n, 2000)
		found = {}
		for i in range(len(chs) - 3):
			p = (chs[i], chs[i+1], chs[i+2], chs[i+3])
			if p not in found:
				found[p] = True
				if p not in ans:
					ans[p] = 0
				ans[p] += prs[i+4]
	print(max(ans.values()))
