from itertools import product

def solve(res, nums):
	for combination in product("+*|", repeat=len(nums)-1):
		cur = nums[0]
		for i, op in enumerate(combination):
			if op == '*':
				cur *= nums[i+1]
			elif op == '+':
				cur += nums[i+1]
			else:
				cur = int(str(cur) + str(nums[i+1]))
		if cur == res:
			return res
	return 0
ans = 0
with open('7.in', 'r') as file:
	for line in file:
		test = line.split(' ')
		ans += solve(int(test[0][:-1]), list(map(int, test[1:])))
print(ans)
