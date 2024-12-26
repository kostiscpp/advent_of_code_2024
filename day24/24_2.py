vals = {}
wires = {}
def lazy_eval(wire, vs, d):
	if wire in vs:
		return vs[wire]
	if d >= 995:
		return -1
	binop, op1, op2 = wires[wire]
	res = 0	
	if binop == "AND":
		res = lazy_eval(op1, vs, d+1) and lazy_eval(op2, vs, d+1)
	elif binop == "OR":
		res = lazy_eval(op1, vs, d+1) or lazy_eval(op2, vs, d+1)
	elif binop == "XOR":
		res = lazy_eval(op1, vs, d+1) ^ lazy_eval(op2, vs, d+1)
	vs[wire] = res
	return res

def evaluate(x, y):
	vs = vals.copy()
	real = x + y
	for reg in sorted(vals.keys()):
		if reg[0] == "x":
			vs[reg] = x % 2
			x //= 2
		else:
			vs[reg] = y % 2
			y //= 2
	for wire in wires.keys():
		if wire not in vs:
			vs[wire] = lazy_eval(wire, vs, 1)
	z_wires = [w for w in vs.keys() if w.startswith('z')]
	z_wires.sort()
	ans = 0
	for i, wire in enumerate(z_wires):
		bit = vs[wire]
		ans += bit * (1 << i)
	return ans

def get_dep(a):
	gate, op1, op2 = wires[f'z{a if a > 9 else '0' + str(a)}']
	print(f'z{a if a > 9 else '0' + str(a)} =', op1, gate, op2)
	def rec(o, d):
		if o not in wires:
			return
		g, o1, o2 = wires[o]
		print(d*' ' ,o, '=', o1, g, o2)
		rec(o1, d+1)
		print()
		rec(o2, d+1)
	rec(op1, 1)
	rec(op2, 1)
with open("24.in", "r") as file:
	for line in file:
		if len(line) == 7:
			c, v = line.strip('\n').split(': ')
			vals[c] = int(v)
		elif line[0] != '\n':
			op1, binop, op2, _, r = line.strip('\n').split(' ')
			wires[r] = [binop, op1, op2]
	z13 = wires["z13"]
	wires["z13"] = wires["hsw"]
	wires["hsw"] = z13
	if evaluate(1 << 13, 1 << 13) == 2*(1 << 13):
		print(13)
	z18 = wires["z18"] 
	wires["z18"] = wires["skf"]
	wires["skf"] = z18
	if evaluate(1 << 18, 1 << 18) == 2*(1 << 18):
		print(18)
	nvr = wires["nvr"]
	wires["nvr"] = wires["wkr"]
	wires["wkr"] = nvr
	if evaluate(1 << 26, 1 << 26) == 2*(1 << 26):
		print(26)
	suspects = ["tgj", "mkm", "njc", "bjm", "kbk"] 
	narrowed_down = []
	w0 = "z07"
	for w in suspects:
		temp = wires[w]
		wires[w] = wires[w0]
		wires[w0] = temp
		flag = True
		for a in range(45):
			if evaluate(1 << a, 0) != 1 << a:
				flag = False
			if evaluate(1 << a, 1 << a) != 2*(1 << a):
				flag = False
		if flag:
			narrowed_down.append(w)
			narrowed_down.append(w0)
		temp = wires[w]
		wires[w] = wires[w0]
		wires[w0] = temp
	for i in range(0, len(narrowed_down), 2):
		print(','.join(sorted(narrowed_down[i:i+2] + ["z13", "hsw", "skf", "z18", "nvr", "wkr"])))
