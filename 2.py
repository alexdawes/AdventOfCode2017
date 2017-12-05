def row_checksum_1(row):
    return max(row) - min(row)

def row_checksum_2(row):
    for i in range(len(row)):
        for j in range(len(row)):
            if i == j:
                continue

            div = row[i] / row[j]
            if div == int(div):
                return div

def array_checksum(rows, checksum):
    return int(sum([checksum(row) for row in rows]))

if __name__ == '__main__':

    with open('input_2.txt') as f:
        lines = f.readlines()
        arr = [[int(n) for n in l.strip().split('\t')] for l in lines]
    
    print('Part 1:', array_checksum(arr, row_checksum_1))
    print('Part 2:', array_checksum(arr, row_checksum_2))