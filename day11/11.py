import math
from collections import Counter
def rules(nums):
	new_nums = Counter()
	for n, f in nums.items():
		if n != 0:
			dig = int(math.log10(n)) + 1
		if n == 0:
			new_nums[1] += f
		elif dig % 2 == 0:
			h = 10 ** (dig//2)
			l = n // h
			r = n % h
			new_nums[l] += f
			new_nums[r] += f
		else:
			mul = 2024 * n
			new_nums[mul] += f
	return new_nums


nums = []
with open('11.in', 'r') as file:
	for line in file:
		nums = line.strip('\n').split(' ')
	freq = Counter()
	for n in nums:
		nat = int(n)
		freq[nat] += 1
	for i in range(75):
		freq = rules(freq)
	print(sum(freq.values()))
