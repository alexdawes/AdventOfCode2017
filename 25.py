import re


class Core(object):
    def __init__(self, state):
        self.tape = [0]
        self.cursor = 0
        self.state = state

    def move_left(self):
        if self.cursor == 0: 
            self.tape.insert(0,0)
        else:
            self.cursor -= 1

    def move_right(self):
        if self.cursor == len(self.tape) - 1:
            self.tape.append(0)
        self.cursor += 1

    def read(self):
        return self.tape[self.cursor]

    def write(self, value):
        self.tape[self.cursor] = value

    def checksum(self):
        return sum(self.tape)
    
    def set_state(self, state):
        self.state = state
        
class Write(object):
    def __init__(self, value):
        self.value = value
    def run(self, core):
        core.write(self.value)

class MoveRight(object):
    def run(self, core):
        core.move_right()

class MoveLeft(object):
    def run(self, core):
        core.move_left()

class SetState(object):
    def __init__(self, state):
        self.state = state
    def run(self, core):
        core.set_state(self.state)

if __name__ == '__main__':

    with open('input_25.txt') as f:
        content = f.readlines()

    lines = [l.strip() for l in content]

    state = re.match(r"Begin in state (\w)\.", lines[0]).groups()[0]
    num_steps = int(re.match(r"Perform a diagnostic checksum after (\d+) steps\.", lines[1]).groups()[0])

    line_idx = 3
    blueprint = {}

    while line_idx < len(lines):
        state_key = re.match(r"In state (\w):", lines[line_idx]).groups()[0]
        blueprint[state_key] = { 0:[], 1:[] }
        line_idx += 1
        while line_idx < len(lines) and lines[line_idx]:
            val_key = int(re.match(r"If the current value is (\d):", lines[line_idx]).groups()[0])
            line_idx += 1
            while line_idx < len(lines) and lines[line_idx].startswith('-'):
                write_match = re.match(r"- Write the value (\d)\.", lines[line_idx])
                move_match = re.match(r"- Move one slot to the (left|right)\.", lines[line_idx])
                continue_match = re.match(r"- Continue with state (\w)\.", lines[line_idx])

                if write_match:
                    value = int(write_match.groups()[0])
                    blueprint[state_key][val_key].append(Write(value))
                elif move_match:
                    direction = move_match.groups()[0]
                    if direction == 'right':
                        blueprint[state_key][val_key].append(MoveRight())
                    else:
                        blueprint[state_key][val_key].append(MoveLeft())
                elif continue_match:
                    value = continue_match.groups()[0]
                    blueprint[state_key][val_key].append(SetState(value))
                else:
                    raise Exception('Should not be here.')

                line_idx += 1
                
        line_idx += 1

    core = Core(state)
    for i in range(num_steps):
        val = core.read()
        state = core.state
        for fn in blueprint[state][val]:
            fn.run(core)

    print('Part 1:', core.checksum())
            
                
                
