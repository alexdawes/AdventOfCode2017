tape = [0]
cursor = 0
state = 'A'

def move_left():
    global cursor, tape
    if cursor == 0:
        tape.insert(0,0)
    else:
        cursor -= 1

def move_right():
    global cursor, tape
    if cursor == len(tape) - 1:
        tape.append(0)
    cursor += 1

def read():
    global cursor, tape
    return tape[cursor]

def write(value):
    global cursor, tape
    tape[cursor] = value

def checksum():
    global tape
    return sum(tape)

if __name__ == '__main__':

    for i in range(12425180):
        current = read()
        if state == 'A':
            if current == 0:
                write(1)
                move_right()
                state = 'B'
            else:
                write(0)
                move_right()
                state = 'F'
        elif state == 'B':
            if current == 0:
                write(0)
                move_left()
                state = 'B'
            else:
                write(1)
                move_left()
                state = 'C'
        elif state == 'C':
            if current == 0:
                write(1)
                move_left()
                state = 'D'
            else:
                write(0)
                move_right()
                state = 'C'
        elif state == 'D':
            if current == 0:
                write(1)
                move_left()
                state = 'E'
            else:
                write(1)
                move_right()
                state = 'A'
        elif state == 'E':
            if current == 0:
                write(1)
                move_left()
                state = 'F'
            else:
                write(0)
                move_left()
                state = 'D'
        else:
            if current == 0:
                write(1)
                move_right()
                state = 'A'
            else:
                write(0)
                move_left()
                state = 'E'

    print('Part 1:', checksum())