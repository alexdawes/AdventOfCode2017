def run_round(arr, lengths, position, skip):
    arr = [a for a in arr]
    for length in lengths:
        start_idx = position
        end_idx = position + length

        if end_idx >= len(arr):
            end_idx = end_idx % len(arr)

            end_bit = arr[start_idx:]
            start_bit = arr[:end_idx]
            arr_to_flip = end_bit + start_bit

            arr_to_flip.reverse()
            new_end_bit = arr_to_flip[:len(end_bit)]
            new_start_bit = arr_to_flip[len(end_bit):]

            arr = new_start_bit + arr[end_idx:start_idx] + new_end_bit

        else:
            arr_to_flip = arr[start_idx:end_idx]
            
            arr_to_flip.reverse()
            
            arr = arr[:start_idx] + arr_to_flip + arr[end_idx:]

        position = (position + length + skip) % len(arr)
        skip += 1
    
    return arr, position, skip

 


if __name__ == '__main__':
    with open('input_10.txt') as f:
        content = f.read()

    input = [int(i) for i in content.split(',')]

    arr = list(range(0,256))
    skip = 0
    position = 0
    
    arr, position, skip = run_round(arr, input, position, skip)

    print('Part 1:', arr[0] * arr[1])


    input = [ord(i) for i in content.strip()]

    lengths = input + [17, 31, 73, 47, 23]

    arr = list(range(0,256))
    skip = 0
    position = 0
    for i in range(64):
        arr, position, skip = run_round(arr, lengths, position, skip)
    
    sparse = arr
    dense = [
        arr[16*i] ^ arr[16*i+1] ^ arr[16*i+2] ^ arr[16*i+3] ^ arr[16*i+4] ^ arr[16*i+5] ^ arr[16*i+6] ^ arr[16*i+7] ^ arr[16*i+8] ^ arr[16*i+9] ^ arr[16*i+10] ^ arr[16*i+11] ^ arr[16*i+12] ^ arr[16*i+13] ^ arr[16*i+14] ^ arr[16*i+15]
        for i in range(16)
    ]

    hex_strs = [hex(i) for i in dense]
    hex_codes = [h[2:] if len(h) == 4 else '0' + h[2] for h in hex_strs]
    hash = ''.join(hex_codes)

    print('Part 2:', hash)





            
        