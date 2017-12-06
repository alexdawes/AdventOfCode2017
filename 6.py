def get_max_idx(array):
    mx = max(array)
    idx = array.index(mx)
    return idx

def redistribute(array):
    array = [a for a in array]
    idx = get_max_idx(array)
    val = array[idx]
    array[idx] = 0
    while val > 0:
        idx = (idx + 1) % len(array)
        array[idx] += 1
        val -= 1
    return array

if __name__ == '__main__':
    with open('input_6.txt') as f:
        content = f.read()

    input = [int(n) for n in content.split('\t')]

    log = []
    count = 0

    while input not in log:
        count += 1
        log.append(input)
        input = redistribute(input)

    print('Part 1:', count)

    idx = log.index(input)

    loop_length = len(log) - idx

    print('Part 2:', loop_length)


