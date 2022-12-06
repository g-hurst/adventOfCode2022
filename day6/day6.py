import copy

def parse_data(f_name):
    with open(f_name, 'r') as f:
        data  = f.read()
        return data 

def part_1_and_2(data:str, n):
    data = list(data)  
    curr = data[:n] # note, this is unsafe on inputs less than length of n
    data = data[n:]
    marker = n
    is_found = (len(set(curr)) == n)
    while (is_found == False and len(data) > 0): # note, this will also return true if it reaches end of packet
        marker += 1
        curr = curr[1:] + [data.pop(0),]
        is_found = (len(set(curr)) == n)
    return marker

if __name__ == '__main__':
    data    = parse_data('input.txt')
    examples = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb',    7,  19), 
                ('bvwbjplbgvbhsrlpgdmjqwftvncz',      5,  23), 
                ('nppdvjthqldpwncqszvftbrmjlhg',      6,  23), 
                ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29), 
                ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',  11, 26)]


    for example, answer_p1, answer_p2 in examples:
        assert part_1_and_2(example, 4) == answer_p1
        assert part_1_and_2(example, 14) == answer_p2

    p1 = part_1_and_2(data, 4)
    p2 = part_1_and_2(data, 14)

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')