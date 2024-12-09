def turn_right(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'

def direction_to_delta(direction):
    if direction == '^':
        return (-1, 0)
    elif direction == 'v':
        return (1, 0)
    elif direction == '<':
        return (0, -1)
    elif direction == '>':
        return (0, 1)

def solve_lab_guard_path(lab_map):
    rows = len(lab_map)
    cols = len(lab_map[0])

    guard_row = guard_col = None
    guard_dir = None
    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] in '^v<>':
                guard_row, guard_col = r, c
                guard_dir = lab_map[r][c]
                break
        if guard_dir is not None:
            break

    visited = set()
    visited.add((guard_row, guard_col))

    while True:
        dx, dy = direction_to_delta(guard_dir)
        next_row = guard_row + dx
        next_col = guard_col + dy

        if 0 <= next_row < rows and 0 <= next_col < cols:
            if lab_map[next_row][next_col] == '#':
                guard_dir = turn_right(guard_dir)
            else:
                guard_row, guard_col = next_row, next_col
                visited.add((guard_row, guard_col))
        else:
            break

    return len(visited)

W = []
with open('5.in', 'r') as file:
    for line in file:
        W.append(line.strip())
print(solve_lab_guard_path(W))

