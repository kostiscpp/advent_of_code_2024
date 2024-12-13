from functools import lru_cache
import math

@lru_cache(maxsize=None)
def count_nums(n, blinks):
	if blinks == 0:
		return 1
	if n == 0:
		return count_nums(1, blinks - 1)
	num_dig = int(math.log10(n)) + 1

	if num_dig % 2 == 0:
		h = 10 **(num_dig//2)
		l = n // h
		r = n % h
		return count_nums(l, blinks - 1) + count_nums(r, blinks - 1)
	return count_nums(n * 2024, blinks - 1)

nums = []
with open('11.in', 'r') as file:
	for line in file:
		nums = list(map(int, line.strip('\n').split(' ')))
	freq = dict()
	for n in nums:
		if n not in freq:
			freq[n] = 0
		freq[n] += 1
	ans = 0
	for n, f in freq.items():
		ans += f * count_nums(n, 75)
	print(ans)
