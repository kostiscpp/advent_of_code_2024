import math

def simulate(points, t):
	return [((x + vx * t) % 101, (y + vy * t) % 103, vx, vy) for (x, y, vx, vy) in points]

def clustering_metric(points):
    
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]
	cx = sum(xs) / len(xs)
	cy = sum(ys) / len(ys)
	ssd = 0.0
    
	for (x, y, vx, vy) in points:
		dx = x - cx
		dy = y - cy
		ssd += dx*dx + dy*dy
    
	return ssd

def bounding_box(points):
	
	xs = [p[0] for p in points]
	ys = [p[1] for p in points]
	
	return min(xs), max(xs), min(ys), max(ys)

def print_points(points):
	
	min_x, max_x, min_y, max_y = bounding_box(points)
	width = max_x - min_x + 1
	height = max_y - min_y + 1
	grid = [[' ' for _ in range(width)] for _ in range(height)]

	for (x, y, vx, vy) in points:
		grid[y - min_y][x - min_x] = '#'
    
	for row in grid:
		print(''.join(row))

points = []
with open("14.in", "r") as file:
	
	for line in file:
		parts = line.strip().split('v')
		pos_str = parts[0].split('=')[1].strip()
		px, py = pos_str.split(',')
		x, y = int(px), int(py)
		vel_str = parts[1].split('=')[1].strip()
		vx, vy = vel_str.split(',')
		vx, vy = int(vx), int(vy)
		points.append((x, y, vx, vy))
    	
	min_metric = float('inf')
	best_time = 0
	growth_count = 0
	prev_metric = float('inf')
		
	for t in range(200000):
		curr_pos = simulate(points, t)
		metric = clustering_metric(curr_pos)
		
		if metric < min_metric:
			min_metric = metric
			best_time = t
			growth_count = 0
		else:
			growth_count += 1
			if growth_count > 200000:
				break
		prev_metric = metric
    
	final_pos = simulate(points, best_time)
    
	print(best_time)    


