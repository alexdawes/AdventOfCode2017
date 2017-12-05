def captcha(input, selector):
    summands = [int(input[i]) if input[selector(i)] == input[i] else 0 for i in range(len(input))]
    return sum(summands)

def captcha_1(input):
    input = str(input)
    selector = lambda i: (i + 1) % len(input)
    return captcha(input, selector)

def captcha_2(input):
    input = str(input)
    step = int(len(input)/2)
    selector = lambda i: (i + step) % len(input)
    return captcha(input, selector)

if __name__ == '__main__':
    with open('input_1.txt') as f:
        input = f.read()

    print('Part 1:', captcha_1(input))
    print('Part 2:', captcha_2(input))