l1 = []
l2 = []
with open('1.in', 'r') as file:
	for line in file:
		x, y = line.split('   ')
		l1.append(int(x))
		l2.append(int(y))
l1 = sorted(l1)
print(l1)
l2 = sorted(l2)
print(l2)
ans = 0
for i in range(len(l1)):
	ans += abs(l1[i]-l2[i])
print("Part 1")
print(ans)

sim = 0
for x in l1:
	while len(l2) > 0 and x >= l2[0]:
		if x == l2[0]:
			print(x)
			sim += x
		l2.pop(0)
	if len(l2) == 0:
		break
print(sim)
