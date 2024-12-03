def if_rm(i, l):
	l_new = l[:i] + l[i+1:]
	for i in range(len(l_new)-1):
		d = l_new[i+1] - l_new[i]
		if abs(d) > 3 or abs(d) < 1:
			return False
		if i < len(l_new)-2 and (d > 0) != (l_new[i+2] -  l_new[i+1] > 0):
			return False
	return True


safes = 0
with open('2.in', 'r') as file:
	for line in file:
		l = list(map(int, line.split(' ')))
		is_safe = 0
		if if_rm(0, l):
			is_safe = 1
		for i in range(len(l)-1):
			d = l[i+1] - l[i]
			if abs(d) > 3 or abs(d) < 1:
				if if_rm(i, l) or if_rm(i+1, l):
					is_safe = 1
				break
			if i < len(l)-2 and (d > 0) != (l[i+2] -  l[i+1]> 0):
				if if_rm(i, l) or  if_rm(i+1, l) or if_rm(i+2, l):
					is_safe = 1
				break
		safes += is_safe

print(safes)
