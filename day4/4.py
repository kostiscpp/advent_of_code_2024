W = []
ans = 0

def count_W(grid):
	count = 0
	rows = len(grid)
	cols = len(grid[0])
	word = "XMAS"
	word_len = len(word)

	directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]
	
	for row in range(rows):
		for col in range(cols):
			for dir_x, dir_y in directions:
				match = True
				for k in range(word_len):
					new_row = row + dir_x * k
					new_col = col + dir_y * k
					if (0 <= new_row < rows) and (0 <= new_col < cols):
						if grid[new_row][new_col] != word[k]:
							match = False
							break
					else:
						match = False
						break
				if match:
					count += 1
	return count

def count_X_MAS(grid):
	count = 0
	rows = len(grid)
	cols = len(grid[0])

	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == "A":
				if row > 0 and col > 0 and row < rows-1 and col < cols-1:
					if grid[row][col] == "A":
						if (grid[row-1][col-1], grid[row+1][col+1]) in [("M", "S"), ("S", "M")] and (grid[row-1][col+1], grid[row+1][col-1]) in [("M", "S"), ("S", "M")]:
							count += 1
	return count

with open('4.in', 'r') as file:
	for line in file:
		W.append(line.strip())

print(count_W(W))

print(count_X_MAS(W))
