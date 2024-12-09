from collections import deque


def is_ord(U, O):
	pos = {u: idx for idx, u in enumerate(U)}
	for x, y in O:
		if x in pos and y in pos:
			if pos[x] > pos[y]:
				return False
	return True

def count_pages(Or, Up):
	ans = 0
	for u in Up:
		if not u:
			continue
		if is_ord(u, Or):
			continue
		o = [(x,y) for x,y in Or if x in u and y in u]
		srt = top_sort(u, o)
		ans += int(srt[len(srt)//2])
	return ans

def top_sort(pages, Ord):
	graph = dict()
	in_degree = dict()
	for page in pages:
		in_degree[page] = 0
    
	for x, y in Ord:
		if x in pages and y in pages:
			if x not in graph:
				graph[x] = []
			if y not in graph:
				graph[y] = []
			graph[x].append(y)
			in_degree[y] += 1
    
	queue = deque([page for page in pages if in_degree[page] == 0])
    
	sorted_pages = []
    
	while queue:
		current = queue.popleft()
		sorted_pages.append(current)
		for neighbor in graph[current]:
			in_degree[neighbor] -= 1
			if in_degree[neighbor] == 0:
				queue.append(neighbor)
    
	return sorted_pages

Ord = []
Upd = []
with open('5.in', 'r') as file:
	for line in file:
		line = line.strip('\n')
		if len(line) == 5: 
			x, y = line.strip().split('|')
			Ord.append((x,y))
		elif len(line) > 1:
			Upd.append(line.strip().split(','))

print(count_pages(Ord, Upd))
