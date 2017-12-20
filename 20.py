import re

class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '<{},{},{}>'.format(self.x, self.y, self.z)
    def __str__(self):
        return '<{},{},{}>'.format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def norm(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

class Particle(object):
    def __init__(self, id, pos, vel, acc):
        self.id = id
        self.position = pos
        self.velocity = vel
        self.acceleration = acc

    def tick(self):
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity

    def __repr__(self):
        return '{}: p={}, v={}, a={}'.format(self.id, self.position, self.velocity, self.acceleration)

    def __eq__(self, other):
        return self.id == other.id
        

def parse_line(idx, line):
    groups = [int(i) for i in re.match(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>", line).groups()]
    position = Vector(groups[0], groups[1], groups[2])
    velocity = Vector(groups[3], groups[4], groups[5])
    acceleration = Vector(groups[6], groups[7], groups[8])
    return Particle(idx, position, velocity, acceleration)

def parse(lines):
    lines = [l.strip() for l in lines]
    return [parse_line(i,l) for i,l in enumerate(lines)]

if __name__ == '__main__':
    with open('input_20.txt') as f:
        content = f.readlines()
    
    particles = parse(content)

    sorted_by_abs_acc = sorted(particles, key=lambda p: p.acceleration.norm())
    print('Part 1:', sorted_by_abs_acc[0].id)

    for x in range(100):
    #while True:
        for p in particles:
            p.tick()

        processed = []
        to_destroy = []
        for p in particles:
            matching = [q for q in processed if q.position == p.position]
            if len(matching) > 0:
                to_destroy.append(p)
                for q in [m for m in matching if m not in to_destroy]:
                    to_destroy.append(q)
            processed.append(p)

        for p in to_destroy:
            particles.remove(p)

        sorted_by_abs_acc = sorted(particles, key=lambda p: p.acceleration.norm())
        sorted_by_abs_pos = sorted(particles, key=lambda p: p.position.norm())

        if sorted_by_abs_acc == sorted_by_abs_pos:
            break
    
    print('Part 2:', len(particles))

