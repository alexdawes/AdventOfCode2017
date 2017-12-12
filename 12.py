class Program(object):
    def __init__(self, id, neighbours):
        self.id = id
        self.neighbours = neighbours

    def __repr__(self):
        return '{} <-> {}'.format(self.id, ', '.join([str(n) for n in self.neighbours]))

def parse_input(lines):
    split = [l.split(' <-> ') for l in lines]
    return { int(s[0]): Program(int(s[0]), [int(t) for t in s[1].split(', ')]) for s in split }

def get_group(input, id):
    to_process = [id]
    connected_group = []

    while len(to_process) > 0:
        processing = to_process.pop()
        connected_group.append(processing)
        neighbours = input[processing].neighbours
        unprocessed = [n for n in neighbours if n not in connected_group and n not in to_process]
        to_process = list(set(to_process + unprocessed))

    return connected_group

if __name__ == '__main__':
    with open('input_12.txt') as f:
        content = f.readlines()

    input = parse_input(content)

    group_0 = get_group(input, 0)

    print('Part 1:', len(group_0))

    all_ids = list(input.keys())
    groups = []
    while len(all_ids) > 0:
        id = all_ids.pop()
        group = get_group(input, id)
        all_ids = [i for i in all_ids if i not in group]
        groups.append(group)

    print('Part 2:', len(groups))
