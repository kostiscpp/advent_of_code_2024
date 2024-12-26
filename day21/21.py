gridA = {'7' : (0,0), '8' : (0,1), '9' : (0,2),
    	 '4' : (1,0), '5' : (1,1), '6' : (1,2),
    	 '1' : (2,0), '2' : (2,1), '3' : (2,2),
    				  '0' : (3,1), 'A' : (3,2)}

gridB =	{
    			 '^' : (0,1), 'A' : (0,2),
    '<' : (1,0), 'v' : (1,1), '>' : (1,2)}

N = 26 

def all_paths(me, goal, grid):
	dr = goal[0] - me[0]
	dc = goal[1] - me[1]
	rchar = '^' if dr < 0 else 'v'
	cchar = '<' if dc < 0 else '>'

	if grid == True:
		if me[1] == 0 and goal[0] == 3:
			yield abs(dc)*cchar + abs(dr)*rchar + "A"
		elif me[0] == 3 and goal[1] == 0:
			yield abs(dr)*rchar + abs(dc)*cchar + "A"
		else:
			yield abs(dc)*cchar + abs(dr)*rchar + "A"
			yield abs(dr)*rchar + abs(dc)*cchar + "A"
	else:
		if me[0] == 0 and goal[1] == 0:
			yield abs(dr)*rchar + abs(dc)*cchar + "A"
		elif me[1] == 0 and goal[0] == 0:
			yield abs(dc)*cchar + abs(dr)*rchar + "A"
		else:
			yield abs(dc)*cchar + abs(dr)*rchar + "A"
			yield abs(dr)*rchar + abs(dc)*cchar + "A"
dp = {}
def solve(seq, n):
	if n == 0:
		return len(seq)
	grid = {}
	if (seq, n) not in dp:
		if n == N:
			grid = gridA
		else:
			grid = gridB
		ans = 0
		me = 'A'
		for goal in seq:
			shortest = float('inf')
			for path in all_paths(grid[me], grid[goal], n == N):
				shortest = min(shortest, solve(path, n-1))
			ans += shortest
			me = goal
		dp[(seq, n)] = ans
	return dp[(seq, n)]
with open("21.in", "r") as file:
	ans = 0
	for line in file:
		seq = line.strip('\n')
		ans += int(seq[:-1]) * solve(seq, N)
	print(ans)
