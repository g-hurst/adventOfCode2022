def parse_data(f_name):
    data = [[list(map(int, pairs.split('-'))) for pairs in line.strip().split(',')] for line in open(f_name, 'r')]
    return data

def part_1(data):
    count = 0
    
    for pair in data:
        count += (pair[0][0] <= pair[1][0]) and \
                 (pair[0][1] >= pair[1][1]) or  \
                 (pair[0][0] >= pair[1][0]) and \
                 (pair[0][1] <= pair[1][1])
    return count

def part_2(data):
    count = 0
    
    for pair in data:
        dist1 = pair[0][1] - pair[0][0]
        dist2 = pair[1][1] - pair[1][0]
        start_diff = pair[1][0] - pair[0][0]
        if start_diff > 0:
            count += dist1 >= start_diff
        else:
            count += dist2 >= abs(start_diff)
    return count

if __name__ == '__main__':
    example = parse_data('example.txt')
    data    = parse_data('input.txt')
    
    assert part_1(example) == 2
    assert part_2(example) == 4

    p1 = part_1(data)
    p2 = part_2(data)

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')