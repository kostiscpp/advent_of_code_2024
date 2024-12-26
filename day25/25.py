locks = []
keys = []

def fits(l, k):
	for s in [x + y for x, y in zip(l, k)]:
		if s > 5:
			return 0
	return 1

def count_keys():
	ans = 0
	for lock in locks:
		for key in keys:
			ans += fits(lock, key)
	return ans


with open("25.in", "r") as file:
	k = False
	for i, line in enumerate(file):
		if i % 8 == 0:
			k = (line[0] == "#")
			if k:
				locks.append([0, 0, 0, 0, 0])
			else:
				keys.append([-1, -1, -1, -1, -1])
		elif i % 8 != 7:
			for j, l in enumerate(line):
				if l == "#":
					if k:
						locks[-1][j] += 1
					else:
						keys[-1][j] += 1
print(count_keys())
