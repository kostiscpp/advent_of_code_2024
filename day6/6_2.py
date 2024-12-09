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

def find_guard_start(lab_map):
    rows = len(lab_map)
    cols = len(lab_map[0])
    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] in '^v<>':
                return (r, c, lab_map[r][c])
    return None

def simulate(lab_map):
    rows = len(lab_map)
    cols = len(lab_map[0])
    start = find_guard_start(lab_map)
    if not start:
        return True
    start_r, start_c, start_dir = start

    r, c, d = start_r, start_c, start_dir
    visited_states = set()
    visited_states.add((r, c, d))

    step_limit = rows * cols * 10
    steps = 0

    while steps < step_limit:
        steps += 1
        dx, dy = direction_to_delta(d)
        nr, nc = r + dx, c + dy

        if 0 <= nr < rows and 0 <= nc < cols:
            if lab_map[nr][nc] == '#':
                d = turn_right(d)
                if (r, c, d) in visited_states:
                    return False
                visited_states.add((r, c, d))
            else:
                r, c = nr, nc
                if (r, c, d) in visited_states:
                    return False
                visited_states.add((r, c, d))
        else:
            return True

    return False

def solve(lab_map):
    rows = len(lab_map)
    cols = len(lab_map[0])
    start_r, start_c, start_dir = find_guard_start(lab_map)

    mutable_map = [list(row) for row in lab_map]

    loop_positions = 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) != (start_r, start_c) and mutable_map[r][c] == '.':
                mutable_map[r][c] = '#'
                if not simulate(mutable_map):
                    loop_positions += 1
                mutable_map[r][c] = '.'

    return loop_positions

if __name__ == "__main__":
    import sys
    lab_map = [line.rstrip('\n') for line in sys.stdin if line.strip()]
    result = solve(lab_map)
    print(result)

