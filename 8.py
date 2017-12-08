import re
regex = re.compile('(\w+) (dec|inc) (-?\d+) if (\w+) (<=|>=|>|<|==|!=) (-?\d+)')

comparisons = {
    '<=': lambda a,b: a <= b,
    '>=': lambda a,b: a >= b,
    '<': lambda a,b: a < b,
    '>': lambda a,b: a > b,
    '==': lambda a,b: a == b,
    '!=': lambda a,b: a != b
}

operations = {
    'inc': lambda a,b: a + b,
    'dec': lambda a,b: a - b
}

registry = {}

class Condition(object):
    def __init__(self, variable, comparison, value):
        self.variable = variable
        self.comparison = comparison
        self.value = value

class Instruction(object):
    def __init__(self, variable, operation, value, condition):
        self.variable = variable
        self.operation = operation
        self.value = value
        self.condition = condition

def parse(line):
    var, op, amount, con_var, con_com, con_val = re.match(regex,line).groups()
    return Instruction(
        var, 
        operations[op], 
        int(amount), 
        Condition(
            con_var, 
            comparisons[con_com], 
            int(con_val)
        )
    )

def run(inst):
    if inst.variable not in registry:
        registry[inst.variable] = 0
    if inst.condition.variable not in registry:
        registry[inst.condition.variable] = 0

    if inst.condition.comparison(registry[inst.condition.variable], inst.condition.value):
        registry[inst.variable] = inst.operation(registry[inst.variable], inst.value)

if __name__ == '__main__':
    with open('input_8.txt') as f:
        content = f.readlines()

    input = [parse(c.strip()) for c in content]
    mx = 0

    for inst in input:
        run(inst)
        mx = max([mx, max(registry.values())])

    print('Part 1:', max(registry.values()))
    print('Part 2:', mx)

