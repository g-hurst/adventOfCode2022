from collections import Counter

def part_1(data):
    sames = [set(list(d[:len(d)//2])).intersection(set((list(d[len(d)//2:])))) for d in data]
    sames = Counter([item for sublist in sames for item in sublist])

    total = 0
    for letter in sames.keys():
        weight = (ord(letter) - ord('a') + 1) if letter.islower() else (ord(letter) - ord('A') + 27)
        total += sames[letter] * weight
    return total

def part_2(data):
    sub_groups = []
    curr = []
    while len(data):
        curr.append(data.pop(0))
        if len(curr) == 3:
            sub_groups.append(curr)
            curr = []

    conv = lambda x: set(list(x))
    badges = [conv(group[0]).intersection(conv(group[1])).intersection(conv(group[2])) for group in sub_groups]
    badges = Counter([item for sublist in badges for item in sublist])

    total = 0
    for letter in badges.keys():
        weight = (ord(letter) - ord('a') + 1) if letter.islower() else (ord(letter) - ord('A') + 27)
        total += badges[letter] * weight
    return total

if __name__ == '__main__':
    example = [line.strip() for line in open('example.txt', 'r')]
    data    = [line.strip() for line in open('input.txt', 'r')]

    assert part_1(example) == 157
    assert part_2(example) == 70

    p1 = part_1(data)
    p2 = part_2(data)

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')
