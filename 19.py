class UpDown():
    def __init__(self): pass
    def __repr__(self): return '|'
    def __eq__(self, other): return isinstance(other, UpDown)

class LeftRight():
    def __init__(self): pass
    def __repr__(self): return '-'
    def __eq__(self, other): return isinstance(other, LeftRight)

class ChangeDirection():
    def __init__(self): pass
    def __repr__(self): return '+'
    def __eq__(self, other): return isinstance(other, ChangeDirection)

class Letter(object):
    def __init__(self, value): self.value = value
    def __repr__(self): return self.value
    def __eq__(self, other): return isinstance(other, Letter) and other.value == self.value

class Grid(object):
    def __init__(self, grid):
        self.grid = grid
        self.x = grid[0].index(UpDown())
        self.y = 0
        self.direction = 'v'
        self.letters = []
        self.step_count = 0

    def get_current(self):
        return self.grid[self.y][self.x]

    def get_left(self):
        return self.grid[self.y][self.x - 1] if self.x > 0 else None

    def get_right(self):
        return self.grid[self.y][self.x + 1] if self.x < len(self.grid[self.y]) - 1 else None
    
    def get_up(self):
        return self.grid[self.y - 1][self.x] if self.y > 0 else None
    
    def get_down(self):
        return self.grid[self.y + 1][self.x] if self.y < len(self.grid) - 1 else None

    def walk(self):
        finished = False
        while not finished:
            finished = self.walk_one()

    def walk_one(self):
        if self.direction == 'v':
            self.y += 1
        elif self.direction == '^':
            self.y -= 1
        elif self.direction == '>':
            self.x += 1
        elif self.direction == '<':
            self.x -= 1

        current = self.get_current()

        if current == ChangeDirection():
            if self.get_left() == LeftRight() and self.direction != '>':
                self.direction = '<'
            elif self.get_right() == LeftRight() and self.direction != '<':
                self.direction = '>'
            elif self.get_up() == UpDown() and self.direction != 'v':
                self.direction = '^'
            elif self.get_down() == UpDown() and self.direction != '^':
                self.direction = 'v'
            else:
                raise Error('Should not be here!')

        if isinstance(current, Letter):
            self.letters.append(current.value)

        self.step_count += 1

        return current is None

def parse_char(char):
    if char == '|':
        return UpDown()
    if char == '-':
        return LeftRight()
    if char == '+':
        return ChangeDirection()
    if char == ' ':
        return None
    return Letter(char)

def parse(input):
    return [
        [
            parse_char(char)
            for char in line
        ]
        for line in input
    ]

if __name__ == '__main__':
    with open('input_19.txt') as f:
        content = f.readlines()
    

    input = parse([list(c) for c in content])

    grid = Grid(input)

    grid.walk()

    print('Part 1:', ''.join(grid.letters))

    print('Part 2:', grid.step_count)

