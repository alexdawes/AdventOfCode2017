garbo_count = 0

class Stream(object):
    def __init__(self, input):
        self._input = input

    def next(self):
        next = self._input[0]
        self._input = self._input[1:]
        return next

    def peek(self):
        return self._input[0]

    def len(self):
        return len(self._input)

def skip_garbage(stream):
    global garbo_count
    while True:
        next = stream.next()
        if next == '!':
            stream.next()
        elif next == '>':
            break
        else:
            garbo_count += 1

def clean(input):
    stream = Stream(input)
    s = ''

    while stream.len() > 0:
        next = stream.next()
        if next == '!':
            stream.next()
        elif next == '<':
            skip_garbage(stream)
        else:
            s += next

    return s.replace('{,', '{').replace(',}','}')
        
def split(input):
    s = Stream(input)
    brace_count = 0
    res = []
    c = ''
    while s.len() > 0:
        next = s.next()
        if next == '{':
            brace_count += 1
        elif next == '}':
            brace_count -= 1
        c += next
        if brace_count == 0:
            res.append(c)
            c = ''
            if s.len() > 0 and s.peek() == ',':
                s.next
    return res

    
def parse(input):
    contents = [i for i in split(input[1:-1]) if i and i != ',']
    return [parse(s) for s in contents]

def calc_score(obj, curr = 1):
    return curr + sum([calc_score(o, curr + 1) for o in obj])

if __name__ == '__main__':

    with open('input_9.txt') as f:
        input = f.read().strip()

    input = clean(input)

    obj = parse(input)

    score = calc_score(obj)

    print('Part 1:', score)

    print('Part 2:', garbo_count)

