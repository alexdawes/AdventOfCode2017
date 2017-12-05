def is_valid_1(phrase):
    words = phrase.split(' ')
    existing = []
    for word in words:
        if word in existing:
            return False
        else:
            existing.append(word)
    return True

def is_valid_2(phrase):
    words = phrase.split(' ')
    existing = []
    for word in words:
        word = ''.join(sorted(word))
        if word in existing:
            return False
        else:
            existing.append(word)
    return True

if __name__ == '__main__':
    with open('input_4.txt') as f:
        content = f.readlines()

    input = [c.strip() for c in content]

    print('Part 1:', len([phrase for phrase in input if is_valid_1(phrase)]))
    print('Part 2:', len([phrase for phrase in input if is_valid_2(phrase)]))