vals = {}
wires = {}

def lazy_eval(wire):
	if wire in vals:
		return vals[wire]
	binop, op1, op2 = wires[wire]
	res = 0	
	if binop == "AND":
		res = lazy_eval(op1) and lazy_eval(op2)
	elif binop == "OR":
		res = lazy_eval(op1) or lazy_eval(op2)
	elif binop == "XOR":
		res = lazy_eval(op1) ^ lazy_eval(op2)
	vals[wire] = res
	return res

with open("24.in", "r") as file:
	for line in file:
		if len(line) == 7:
			c, v = line.strip('\n').split(': ')
			vals[c] = int(v)
		elif line[0] != '\n':
			op1, binop, op2, _, r = line.strip('\n').split(' ')
			wires[r] = [binop, op1, op2]
	for wire in wires.keys():
		if wire not in vals:
			vals[wire] = lazy_eval(wire)
	
	z_wires = [w for w in vals.keys() if w.startswith('z')]
	z_wires.sort()
	ans = 0
	for i, wire in enumerate(z_wires):
		bit = vals[wire]
		ans += bit * (1 << i)
	print(ans)


