value = {"0" : 0, "1" : 1, "2" : 2, "3" : 3}
opcode = { "A" : "4", "B" : "5", "C" : "6"}
with open("17.in", "r") as file:
	for line in file:
		if line[0] == "R":
			_, R, V = line.strip("\n").split(" ")
			value[opcode[R[0]]] = int(V)
		elif line[0] == "P":
			Pr = line.strip("Program: ").strip("\n")
			Pr = Pr.split(",")
			i = 0
			n = len(Pr)-1
			to_print = []
			while i < n:
				instr = Pr[i]
				op = Pr[i+1]
				if instr == "0":
					value["4"] = value["4"] // (2**value[op])
				elif instr == "1":
					value["5"] = value["5"] ^ int(op)
				elif instr == "2":
					value["5"] = value[op] % 8
				elif instr == "3":
					if value["4"] != 0:
						i = int(op) - 2
				elif instr == "4":
					value["5"] = value["5"] ^ value["6"]
				elif instr == "5":
					to_print.append(str(value[op] % 8))	
				elif instr == "6":
					value["5"] = value["4"] // (2**value[op])
				elif instr == "7":
					value["6"] = value["4"] // (2**value[op])
				i += 2
			print(",".join(to_print))
