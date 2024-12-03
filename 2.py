safes = 0
with open('2.in', 'r') as file:
	for line in file:
		l = list(map(int, line.split(' ')))
		inc = l[1] - l[0]
		is_safe = 1
		for i in range(2, len(l)):
			d = l[i] - l[i-1]
			if inc <= 3 and inc >= 1:
				if d > 3 or d < 1:
					is_safe = 0
					break
			elif inc <= -1 and inc >= -3:
				if d < -3 or d > -1:
					is_safe = 0
					break
			else:
				is_safe = 0
				break
		safes += is_safe

print(safes)
