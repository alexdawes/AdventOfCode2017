import pandas as pd
import numpy as np

cache = {}

def rotate(matrix):
    return pd.DataFrame(
        [
            [
                matrix[len(matrix) - j - 1][i]
                for i in range(len(matrix))
            ]
            for j in range(len(matrix))
        ]
    )

def hash_matrix(matrix):
    return ''.join(str(matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix)))

def flip(matrix):
    return pd.DataFrame(
        [
            [
                matrix[len(matrix) - j - 1][i]
                for j in range(len(matrix))
            ]
            for i in range(len(matrix))
        ]
    )

def split(matrix, n):
    m = int(len(matrix)/n)
    columns = list([int(r) for r in range(n)])
    rows = []
    for i in range(m):
        row = []
        for j in range(m):
            df = matrix.loc[i*n:((i+1)*n)-1,j*n:((j+1)*n)-1].reset_index(drop=True)
            df.columns = columns
            row.append(df)
        rows.append(row)
    return pd.DataFrame(rows)


def to_matrix(s):
    return pd.DataFrame([[1 if a == '#' else 0 for a in b] for b in s.split('/')])

class Rule(object):
    def __init__(self, frm, to):
        self.to = to
        self.total = total(frm)
        self.froms = []
        for i in range(4):
            self.froms.append(frm.copy())
            self.froms.append(flip(frm.copy()))
            frm = rotate(frm)

    def matches(self, matrix):
        if len(self.froms[0]) != len(matrix):
            return False
        if self.total != total(matrix):
            return False
        for frm in self.froms:
            if frm.equals(matrix):
                return True

        return False

def parse_rule(rule):
    from_str, to_str = rule.split(' => ')
    return Rule(to_matrix(from_str), to_matrix(to_str))

def parse(content):
    return [parse_rule(line.strip()) for line in content]

def total(matrix):
    return sum([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix))])

def merge(m_matrix):
    
    cols = []
    for i in range(len(m_matrix)):
        col = pd.concat([m_matrix[i][j] for j in range(len(m_matrix))])
        cols.append(col)

    df = pd.concat(cols, axis=1).reset_index(drop=True)
    df.columns = [int(r) for r in range(len(df))]
    return df

def run(matrix, rules):
    global cache
    l = len(matrix)
    if l % 2 == 0:
        m = 2
    else:
        m = 3

    split_matrix = split(matrix, m)
    l_split_matrix = len(split_matrix)

    result = []
    for i in range(l_split_matrix):
        row = []
        for j in range(l_split_matrix):
            sub_matrix = split_matrix[i][j]
            sub_result = None
            done = False

            hsh = hash_matrix(sub_matrix)
            if hsh in cache:
                sub_result = cache[hsh].copy()
                done = True

            else:
                for rule in rules:
                    if rule.matches(sub_matrix):
                        done = True
                        sub_result = rule.to
                        cache[hsh] = sub_result.copy()
                        break

            if not done:
                raise Exception('Not done.')

            row.append(sub_result)
        result.append(row)
    return merge(result)

if __name__ == '__main__':
    with open('input_21.txt') as f:
        content = f.readlines()


    rules = parse(content)

    matrix = to_matrix('.#./..#/###')

    for i in range(5):
        print('Running:', i+1)
        matrix = run(matrix, rules)

    print('Part 1:', total(matrix))

    for i in range(18-5):
        print('Running:', i+1+5)
        matrix = run(matrix, rules)

    print('Part 2:', total(matrix))