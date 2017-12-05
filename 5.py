def get_num_steps(input, get_new_value):    
    current = 0
    count = 0
    input_clone = [i for i in input]

    while current >= 0 and current < len(input_clone):
        next = current + input_clone[current]
        input_clone[current] = get_new_value(input_clone[current])
        current = next
        count += 1

    return count


if __name__ == '__main__':
    with open('input_5.txt') as f:
        content = f.readlines()

    input = [int(c.strip()) for c in content]

    print('Part 1:', get_num_steps(input, lambda current: current + 1))
    print('Part 2:', get_num_steps(input, lambda current: current + 1 if current < 3 else current - 1))