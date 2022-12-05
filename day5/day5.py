import copy

def parse_data(f_name):
    with open(f_name, 'r') as f:
        crates, instructions  = f.read().split('\n\n')
        
        stacks = dict()
        crates = crates.split('\n')
        for stack in crates.pop(-1).split():
            inxex = (int(stack) - 1) * 4 + 1
            stacks[int(stack)] = [row[inxex] for row in crates[::-1] if not row[inxex].isspace()]
        
        instructions = [[int(word) for word in line.split() if word.isnumeric()] for line in instructions.split('\n')]
        
    return stacks, instructions

def part_1(data):
    stacks, instructions = copy.deepcopy(data)
    for inst in instructions:
        num, start, end = inst  
        pickup        = stacks[start][-1:-1 - num:-1] # find the stacks to be picked up
        stacks[start] = stacks[start][:-num]          # remove them from the old list
        stacks[end]   = stacks[end] + pickup          # add them to the new location

    return ''.join([stacks[k][-1] for k in stacks.keys() if len(stacks[k])])

def part_2(data):
    stacks, instructions = copy.deepcopy(data)
    for inst in instructions:
        num, start, end = inst  
        pickup        = stacks[start][-num:]   # find the stacks to be picked up (modified)
        stacks[start] = stacks[start][:-num]   # remove them from the old list
        stacks[end]   = stacks[end] + pickup   # add them to the new location

    return ''.join([stacks[k][-1] for k in stacks.keys() if len(stacks[k])])

if __name__ == '__main__':
    example = parse_data('example.txt')
    data    = parse_data('input.txt')
    
    assert part_1(example) == 'CMZ'
    assert part_2(example) == 'MCD'

    p1 = part_1(data)
    p2 = part_2(data)

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')