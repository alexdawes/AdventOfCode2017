import re

def init_registry(keys):
    return { k: 0 for k in keys }

def is_int(i):
    return isinstance(i, int) or re.match(r"-?\d+", str(i))

def get_value(registry, i):
    return (registry[i] if i in registry else 0) if not is_int(i) else i

class Program(object):
    def __init__(self, id, instructions):
        self.id = id
        self.registry = None
        self.queue = []
        self.partner = None
        self.send_count = 0
        self.waiting = False
        self.instructions = instructions
        self.index = 0

    def set_partner(self, partner):
        self.partner = partner

    def init_registry(self, keys):
        self.registry = { k: self.id for k in keys }
        
    def run(self):
        if self.index < 0 or self.index >= len(self.instructions):
            self.waiting = True
            return

        inst = self.instructions[self.index].split(' ')
        cmd, args = inst[0], [int(i) if is_int(i) else i for i in inst[1:]]

        if cmd == 'snd':
            self.snd(*args)
        elif cmd == 'rcv':
            self.rcv(*args)
        elif cmd == 'set':
            self.set(*args)
        elif cmd == 'add':
            self.add(*args)
        elif cmd == 'mul':
            self.mul(*args)
        elif cmd == 'mod':
            self.mod(*args)
        elif cmd == 'jgz':
            self.jgz(*args)

    def snd(self, value):
        self.partner.queue.append(get_value(self.registry, value))
        self.send_count += 1
        self.index += 1

    def rcv(self, key):
        if len(self.queue) == 0:
            self.waiting = True
        else:
            value, self.queue = self.queue[0], self.queue[1:]
            self.waiting = False
            self.registry[key] = value
            self.index += 1
        
    def set(self, key, value):
        val = get_value(self.registry, value)
        if not is_int(val): 
            print('SET',key,value, self.registry)
        self.registry[key] = val
        self.index += 1

    def add(self, key, value):
        val = get_value(self.registry, value)
        if not is_int(val): print('ADD',key,value)
        self.registry[key] += val
        self.index += 1

    def mul(self, key, value):
        val = get_value(self.registry, value)
        if not is_int(val): print('MUL',key,value)
        self.registry[key] *= val
        self.index += 1
        
    def mod(self, key, value):
        val = get_value(self.registry, value)
        if not is_int(val): print('MOD',key,value)
        self.registry[key] %= val
        self.index += 1

    def jgz(self, key, value):
        self.index += get_value(self.registry, value) if get_value(self.registry, key) > 0 else 1

def run(instructions):
    keys = list(set([inst.split(' ')[1] for inst in instructions if not is_int(inst.split(' ')[1])]))
    registry = init_registry(keys)

    sound = None

    current = 0

    while current >= 0 and current < len(instructions):
        
        current_inst = instructions[current]
        cmd, args = current_inst.split(' ')[0], [int(i) if is_int(i) else i for i in current_inst.split(' ')[1:]]

        if cmd == 'snd':
            sound = get_value(registry, args[0])
            current += 1

        elif cmd == 'set':
            registry[args[0]] = get_value(registry, args[1])
            current += 1
        
        elif cmd == 'add':
            registry[args[0]] += get_value(registry, args[1])
            current += 1

        elif cmd == 'mul':
            registry[args[0]] *= get_value(registry, args[1])
            current += 1

        elif cmd == 'mod':
            registry[args[0]] %= get_value(registry, args[1])
            current += 1

        elif cmd == 'rcv':
            if get_value(registry, args[0]) > 0:
                return sound
            else:
                current += 1

        elif cmd == 'jgz':
            if get_value(registry, args[0]) > 0:
                current += get_value(registry, args[1])
            else:
                current += 1
               
if __name__ == '__main__':
    with open('input_18.txt') as f:
        content = f.readlines()

    lines = [l.strip() for l in content]

    value = run(lines)

    print('Part 1:', value)
                
    p0 = Program(0, lines)
    p1 = Program(1, lines)

    keys = list(set([inst.split(' ')[1] for inst in lines if not is_int(inst.split(' ')[1])]))
    p0.init_registry(keys)
    p1.init_registry(keys)

    p0.set_partner(p1)
    p1.set_partner(p0)

    while True:
        p0.run()
        p1.run()

        if p0.waiting and p1.waiting:
            break

    print('Part 2:', p1.send_count)
    