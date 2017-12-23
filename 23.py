import re
import math

def is_int(i):
    return isinstance(i, int) or re.match(r"-?\d+", str(i))

def parse(instruction):
    inst_bits = instruction.split(' ')
    cmd = inst_bits[0]
    x = int(inst_bits[1]) if is_int(inst_bits[1]) else inst_bits[1]
    y = int(inst_bits[2]) if is_int(inst_bits[2]) else inst_bits[2]
    return cmd, x, y

def is_not_prime(n):
    m = math.sqrt(n)
    for i in range(int(m)):
        if int(n/(i+2)) == n/(i+2):
            return True
    return False    

if __name__ == '__main__':
    with open('input_23.txt') as f:
        content = f.readlines()

    instructions = [parse(line.strip()) for line in content]

    registries = {
        k: 0 for k in 'abcdefgh'
    }

    get_value = lambda x: x if is_int(x) else registries[x]

    current = 0
    mul_count = 0
    while current >= 0 and current < len(instructions):
        current_inst = instructions[current]
        cmd, x, y = current_inst[0], current_inst[1], current_inst[2]
        if cmd == 'set':
            registries[x] = get_value(y)
            current += 1
        elif cmd == 'sub':
            registries[x] -= get_value(y)
            current += 1
        elif cmd == 'mul':
            registries[x] *= get_value(y)
            current += 1
            mul_count += 1
        elif cmd == 'jnz':
            current += y if get_value(x) != 0 else 1

    print('Part 1:', mul_count)    


    b = 109900
    count = 0
    while b <= 126900:
        if is_not_prime(b):
            count += 1
        b += 17

    print('Part 2:', count)