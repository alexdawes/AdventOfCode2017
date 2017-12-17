

def run(buff, position, steps, number):
    new_position = (position + steps) % len(buff)
    buff.insert(new_position + 1, number)
    return buff, new_position + 1

if __name__ == '__main__':
    with open('input_17.txt') as f:
        input = int(f.read().strip())

    buff = [0]
    position = 0
    steps = input
    for i in range(1, 2018):
        buff, position = run(buff, position, steps, i)

    print('Part 1:', buff[position + 1])

    curr_after_zero = None
    arr_len = 1
    position = 0
    for i in range(1,50000001):
        position = (position + steps) % arr_len + 1
        arr_len += 1
        if position == 1:
            curr_after_zero = i

    print('Part 2:', curr_after_zero)
        

    