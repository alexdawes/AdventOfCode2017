import re
from collections import Counter

class ProgramLite(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children.split(', ') if children else []

    def __repr__(self):
        return '{} ({}) [{}]'.format(self.name, self.weight, ','.join([c.name for c in self.children]))

class Program(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        
    def __repr__(self):
        return '{} ({}) [{}]'.format(self.name, self.weight, ','.join([c.name for c in self.children]))

    def get_all_children(self):
        children = [c.name for c in self.children]
        for child in self.children:
            children += child.get_all_children()
        return list(set(children))

    def get_full_weight(self):
        if not self.children:
            return self.weight
        return self.weight + sum([child.get_full_weight() for child in self.children])
        

def parse_input(input):
    results = []
    r = re.compile('(\w+) \((\d+)\)( -> (.+))?')
    for line in input:
        name, weight, unused, children = re.match(r, line).groups()
        results.append(ProgramLite(name, int(weight), children))
    return { p.name: p for p in results }

def convert_program(lite_program, lite_programs, programs):
    if lite_program.name in programs:
        return programs[lite_program.name]

    if not lite_program.children:
        program = Program(lite_program.name, lite_program.weight, [])
        programs[lite_program.name] = program
        return program
    
    children = []
    for child in lite_program.children:
        if child not in programs:
            lite_child = lite_programs[child]
            programs[child] = convert_program(lite_child, lite_programs, programs)
        children.append(programs[child])

    program = Program(lite_program.name, lite_program.weight, children)
    programs[program.name] = program
    return program

def convert(lite_programs):
    programs = {}
    for lite_program in lite_programs.values():
        convert_program(lite_program, lite_programs, programs)
    return programs

if __name__ == '__main__':
    with open('input_7.txt') as f:
        content = f.readlines()
    lines = [c.strip() for c in content]
    input = parse_input(lines)

    programs = convert(input)

    root = [p for p in programs.values() if len(p.get_all_children()) == len(programs) - 1][0]

    print('Part 1:', root.name)

    root
    root_counter = Counter([c.get_full_weight() for c in root.children])
    most_common = root_counter.most_common()
    expected_child_weight = most_common[0][0]
    invalid_child_weight = most_common[1][0]

    offset = expected_child_weight - invalid_child_weight

    invalid_child = [c for c in root.children if c.get_full_weight() == invalid_child_weight][0]
    current = invalid_child


    while True:
        if not current.children:
            result = expected_child_weight
            break

        current_child_weights = [c.get_full_weight() for c in current.children]
        if len(set(current_child_weights)) == 1:
            result = expected_child_weight - sum(current_child_weights)
            break
        
        possible_weights = list(set(current_child_weights))

        if possible_weights[0] + offset == possible_weights[1]:
            expected_child_weight = possible_weights[1]
            invalid_child_weight = possible_weights[0]
        else:
            expected_child_weight = possible_weights[0]
            invalid_child_weight = possible_weights[1]

        current = [c for c in current.children if c.get_full_weight() == invalid_child_weight][0]

    print('Part 2:', result)

