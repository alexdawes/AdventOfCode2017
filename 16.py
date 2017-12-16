import re

def swap(s, a, b):
    return s.replace(a,'X').replace(b,a).replace('X',b)

class Spin(object):
    def __init__(self, X):
        self.X = X
    def run(self, s):
        return s[-1 * self.X:] + s[:-1 * self.X]
    def __repr__(self):
        return 's{}'.format(self.X)

class Exchange(object):
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def run(self, s):
        return swap(s, s[self.A], s[self.B])
    def __repr__(self):
        return 'x{}/{}'.format(self.A,self.B)

class Partner(object):
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def run(self, s):
        return swap(s, self.A, self.B)
    def __repr__(self):
        return 'p{}/{}'.format(self.A, self.B)

def parse_step(step):
    spin_regex = r"s(\d+)"
    exchange_regex = r"x(\d+)/(\d+)"
    partner_regex = r"p(\w)/(\w)"

    spin_match = re.match(spin_regex, step)
    if spin_match:
        return Spin(int(spin_match.groups()[0]))

    exchange_match = re.match(exchange_regex, step)
    if exchange_match:
        groups = exchange_match.groups()
        return Exchange(int(groups[0]), int(groups[1]))

    partner_match = re.match(partner_regex, step)
    if partner_match:
        groups = partner_match.groups()
        return Partner(groups[0], groups[1])

    raise Error('Should not be here!')
    

def parse(input):
    step_strs = input.strip().split(',')
    return [parse_step(step) for step in step_strs]
            

if __name__ == '__main__':
    with open('input_16.txt') as f:
        content = f.read()

    steps = parse(content)

    s = 'abcdefghijklmnop'
    for step in steps:
        s = step.run(s)

    print('Part 1:', s)

    count = 1
    while s != 'abcdefghijklmnop':
        for step in steps:
            s = step.run(s)
        count += 1

    r = 1000000000 % count

    s = 'abcdefghijklmnop'
    for i in range(r):
        for step in steps:
            s = step.run(s)

    print('Part 2:', s)