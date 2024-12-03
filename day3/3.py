def isbetween(f, x, y, z, c):
	if z == 'dig':
		return f <= y and f >= x and c.isnumeric()
	return f <= y and f >= x and c == z



muls = 0
with open('3.in', 'r') as file:
	dfound = 0
	found = 0
	a = ""
	b = ""
	l = ""
	do = True
	for line in file:
		for x in line:
			if do:
				if x == 'm':
					dfound = 0
					found = 1
					a = ""
					b = ""
					l = x
				elif (x == 'u' and found == 1) or (x == 'l' and found == 2) or (x == '(' and found == 3) or (isbetween(found, 5, 7, ',', x)):
					found += 1
					if x == ',':
						l = '2'
				elif isbetween(found, 4, 6, 'dig', x) and l != '2':
					a += x
					found += 1
					l = '1'
				elif isbetween(found, 6, 10, 'dig', x) and l == '2':
					b += x
					found += 1
				elif isbetween(found, 7, 11, ')', x) and l == '2':
					muls += int(a) * int(b)
					found = 0
					a = ""
					b = ""
					l = ""
				elif x == 'd':
					dfound = 1
					found = 0
					a = ""
					b = ""
					l = ""
				elif (x == 'o' and dfound == 1) or (x == 'n' and dfound == 2) or (x == '\'' and dfound == 3) or (x == 't' and dfound == 4) or (x == '(' and dfound == 5):
					dfound += 1
				elif (x == ')' and dfound == 6):
					dfound = 0
					do = False
					found = 0
					a = ""
					b = ""
					l = ""
				else:
					dfound = 0
					found = 0
					a = ""
					b = ""
					l = ""
			else:
				if x == 'd':
					dfound = 1
				elif (x == 'o' and dfound == 1) or (x == '(' and dfound == 2):
					dfound += 1
				elif (x == ')' and dfound == 3):
					dfound = 0
					do = True
				else:
					dfound = 0
print(muls)
