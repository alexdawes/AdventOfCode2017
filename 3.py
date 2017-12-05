def get_map(input):
    positions = []
    current_direction = 1
    current_position = [0,0]
    current_length = 1

    while len(positions) < input:
        for j in range(current_length):
            positions.append([current_position[0], current_position[1]])
            current_position[0] += current_direction
        for j in range(current_length):
            positions.append([current_position[0], current_position[1]])
            current_position[1] += current_direction
        current_direction *= -1
        current_length += 1
        
    return positions

def manhatten_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_neighbours(pos):
    return [
        [pos[0] + i, pos[1] + j] 
        for i in range(-1,2) 
        for j in range(-1,2) 
        if i != 0 or j != 0
    ]

if __name__ == '__main__':
    with open('input_3.txt') as f:
        input = int(f.read())
    
    positions_arr = get_map(input)

    print('Part 1:', manhatten_distance(positions_arr[input - 1], [0,0]))

    new_positions = [1]

    current_idx = 1
    while current_idx < input:
        position = positions_arr[current_idx]
        neighbours = get_neighbours(position)
        neighbours_idxs = [positions_arr.index(pos) for pos in neighbours]
        filled_neighbour_idxs = [idx for idx in neighbours_idxs if idx < current_idx]
        summation = sum([new_positions[idx] for idx in filled_neighbour_idxs])
        if summation > input:
            result = summation
            break
        else:
            new_positions.append(summation)
            current_idx += 1

    print('Part 2:', result)