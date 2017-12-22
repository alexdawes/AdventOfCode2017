def rotate_right(direction):
    return (direction[1], -direction[0])

def rotate_left(direction):
    return (-direction[1], direction[0])

def rotate_flip(direction):
    return (-direction[0],-direction[1])

def move(current, direction):
    return (current[0] + direction[0], current[1] + direction[1])

def parse(content):
    grid = [[1 if a == '#' else 0 for a in l.strip()] for l in content]
    grid.reverse()
    len_x = len(grid[0])
    len_y = len(grid)
    middle = (int(len_x/2 - 0.5), int(len_y/2 - 0.5))
    infected = []
    for x in range(len_x):
        for y in range(len_y):
            if grid[y][x]:
                infected.append((x,y))
    return infected, middle, (0,1)

if __name__ == '__main__':
    with open('input_22.txt') as f:
        content = f.readlines()

    # content = [
    #     '..#',
    #     '#..',
    #     '...'
    # ]

    infected, current, direction = parse(content)

    infection_count = 0
    for i in range(10000):
        #print('Current', current, ', Direction', direction, ', Infected', infected)
        if current in infected:
            direction = rotate_right(direction)
        else:
            direction = rotate_left(direction)

        if current in infected:
            infected.remove(current)
        else:
            infected.append(current)
            infection_count += 1

        current = move(current, direction)

    print('Part 1:', infection_count)

    
    infected, current, direction = parse(content)
    states = { c: 2 for c in infected }
    infection_count = 0
    for i in range(10000000):

        if current not in states:
            states[current] = 0 

        current_state = states[current]

        if current_state == 0:
            direction = rotate_left(direction)
        elif current_state == 1:
            pass
        elif current_state == 2:
            direction = rotate_right(direction)
        else:
            direction = rotate_flip(direction)
        
        if current_state == 1:
            infection_count += 1

        states[current] = (current_state + 1) % 4

        current = move(current, direction)

    print('Part 2:', infection_count)