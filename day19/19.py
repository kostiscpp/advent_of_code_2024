def is_valid(towels, design):
	n = len(design)
	dp = [0 for _  in range(n+1)]
	dp[0] = 1
	for i in range(n):
		if dp[i] == 1:
			for towel in towels:
				if design.startswith(towel, i):
					dp[i + len(towel)] = 1
	return dp[n]



ans = 0
towel = []
with open('19.in', 'r') as file:
	for i, line in enumerate(file):
		if i == 0:
			towels = line.strip("\n").split(", ")
		if i > 1:
			ans += is_valid(towels, line.strip("\n"))

print(ans)
