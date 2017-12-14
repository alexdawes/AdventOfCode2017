hash = __import__('10').hash

def get_group(grid, coords):
    group = []
    to_process = [coords]
    while len(to_process) > 0:
        p = to_process.pop()
        if p not in group:
            group.append(p)
        neighbours = [[p[0] + 1, p[1]], [p[0] - 1, p[1]], [p[0], p[1] + 1], [p[0], p[1] - 1]]
        neighbours = [n for n in neighbours if n[0] not in [-1, 128] and n[1] not in [-1,128]]
        for n in neighbours:
            if grid[n[0]][n[1]] == 1 and n not in group and n not in to_process:
                to_process.append(n)

    return group

def count_used(grid):
    return sum([sum(row) for row in grid])

if __name__ == '__main__':
    with open('input_14.txt') as f:
        content = f.read()

    key = content.strip()

    hashes = [hash('{}-{}'.format(key, str(i))) for i in range(128)]

    rows = [[int(i) for i in list(bin(int(hsh, base=16))[2:])] for hsh in hashes]

    grid = []
    for row in rows:
        grid.append([0 for i in range(128-len(row))] + row)

    print('Part 1:', count_used(grid))

    group_count = 0
    while count_used(grid) > 0:
        row_idx = [i for i in range(128) if sum(grid[i]) > 0][0]
        col_idx = [j for j in range(128) if grid[row_idx][j] == 1][0]
        coords = [row_idx,col_idx]
        group = get_group(grid, coords)
        group_count += 1
        for coord in group:
            grid[coord[0]][coord[1]] = 0

    print('Part 2:', group_count)
