def parse(lines):
    arr = [[int(i) for i in l.strip().split(': ')] for l in content]
    return arr

def catches(depth, range, delay = 0):
    position = (depth + delay) % ( 2 * (range - 1) )
    if position >= range:
        position = 2 * (range - 1) - position
    return position == 0

if __name__ == '__main__':
    with open('input_13.txt') as f:
        content = f.readlines()

    input = parse(content)

    severity = 0
    for arr in input:
        if catches(arr[0], arr[1]):
            severity += arr[0] * arr[1]
    print('Part 1:', severity)

    wait = 0
    while True:
        caught = False
        for arr in input:
            if catches(arr[0], arr[1], wait):
                caught = True
                break

        if not caught:
            break
        
        wait += 1

    print('Part 2:', wait)