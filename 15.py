import re

def parse_inputs(lines):
    line_1, line_2 = lines
    input_1 = int(re.match(r"Generator A starts with (\d+)", line_1).groups()[0])
    input_2 = int(re.match(r"Generator B starts with (\d+)", line_2).groups()[0])
    return input_1, input_2

def generate_1(seed):
    return (seed * 16807) % 2147483647

def generate_2(seed):
    return (seed * 48271) % 2147483647    

def generate_1_2(seed):
    while True:
        seed = generate_1(seed)
        if seed % 4 == 0:
            return seed

def generate_2_2(seed):
    while True:
        seed = generate_2(seed)
        if seed % 8 == 0:
            return seed

def check(n1, n2):
    # bin_1 = bin(n1)[2:]
    # bin_2 = bin(n2)[2:]
    # bin_1 = bin_1 if len(bin_1) >= 16 else ''.join(['0' for i in range(16-len(bin_1))] + [b for b in bin_1])
    # bin_2 = bin_2 if len(bin_2) >= 16 else ''.join(['0' for i in range(16-len(bin_2))] + [b for b in bin_2])
    # s_1 = bin_1[-16:]
    # s_2 = bin_2[-16:]
    # return s_1 == s_2
    return n1 % 65536 == n2 % 65536


if __name__ == '__main__':
    with open('input_15.txt') as f:
        content = f.readlines()

    lines = [c.strip() for c in content]
    input_1, input_2 = parse_inputs(lines)

    val_1 = input_1
    val_2 = input_2
    count = 0

    for i in range(40000000):
        val_1 = generate_1(val_1)
        val_2 = generate_2(val_2)
        if check(val_1, val_2):
            count += 1

    print('Part 1:', count)

    val_1 = input_1
    val_2 = input_2
    count = 0

    for i in range(5000000):
        val_1 = generate_1_2(val_1)
        val_2 = generate_2_2(val_2)
        if check(val_1, val_2):
            count += 1

    print('Part 2:', count)
        

    
    