
class Node(object):
    def __init__(self, component, used, remaining):
        self.component = component
        used = used
        remaining = remaining

        non_used = self.component.front if self.component.back == used else self.component.back

        matching = [r for r in remaining if r.front == non_used or r.back == non_used]
        self.children = [Node(r, non_used, [x for x in remaining if x.id != r.id]) for r in matching]

    def max_sum(self):
        return self.component.front + self.component.back + (max([c.max_sum() for c in self.children]) if len(self.children) > 0 else 0)

    def max_length(self):
        return 1 + (max([c.max_length() for c in self.children]) if len(self.children) > 0 else 0)

    def bridges_of_length(self, n):
        if n == 0:
            return [[self]] if len(self.children) == 0 else []
        
        return [[self] + bridge for c in self.children for bridge in c.bridges_of_length(n-1)]


class Component(object):
    def __init__(self, id, f, b):
        self.id = id
        self.front = f
        self.back = b

    def __repr__(self):
        return '{}/{}'.format(self.front, self.back)

def parse(id, line):
    ports = [int(a) for a in line.split('/')]
    return Component(id, ports[0], ports[1])

if __name__ == '__main__':
    with open('input_24.txt') as f:
        content = f.readlines()

    components = [parse(i, l.strip()) for i, l in enumerate(content)]

    trees = [Node(x, 0, [y for y in components if y.id != x.id]) for x in components if x.front == 0 or x.back == 0]

    max_bridge_value = max([t.max_sum() for t in trees])

    print('Part 1:', max_bridge_value)

    max_bridge_length = max([t.max_length() for t in trees])

    bridges = [bridge for t in trees for bridge in t.bridges_of_length(max_bridge_length - 1)]

    strengths = [sum([n.component.front + n.component.back for n in bridge]) for bridge in bridges]

    print('Part 2:', max(strengths))

    


