def go_ne(coords):
    return [coords[0] + 1, coords[1] - 1]

def go_se(coords):
    return [coords[0] + 1, coords[1] + 1]

def go_sw(coords):
    return [coords[0] - 1, coords[1] + 1]

def go_nw(coords):
    return [coords[0] - 1, coords[1] - 1]

def go_n(coords):
    return [coords[0], coords[1] - 2]
    
def go_s(coords):
    return [coords[0], coords[1] + 2]

go_map = {
    'ne': go_ne,
    'se': go_se,
    'sw': go_sw,
    'nw': go_nw,
    'n': go_n,
    's': go_s
}

def get_end_coords(input):
    coords = [0,0]
    for direction in input:
        coords = go_map[direction](coords)
    return coords

def get_dist(coords):
    coords = [coords[0],coords[1]]
    counter = 0
    while coords[0] != 0 or coords[1] != 0:
        direction_map = { direction: go(coords) for direction, go in go_map.items() }
        dists = { direction: abs(c[0]) + abs(c[1]) for direction, c in direction_map.items() }
        min_direction = [direction for direction in direction_map.keys() if dists[direction] == min(dists.values())][0]
        coords = go_map[min_direction](coords)
        counter += 1
    return counter
    

if __name__ == '__main__':
    with open('input_11.txt') as f:
        content = f.read()

    input = content.strip().split(',')
    coords = get_end_coords(input)

    print('Part 1:', get_dist(coords))

    max_dist = 0
    coords = [0,0]
    for direction in input:
        coords = go_map[direction](coords)
        dist = get_dist(coords)
        max_dist = max(max_dist, dist)

    print('Part 2:', max_dist)