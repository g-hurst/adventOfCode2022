from collections import Counter

def part_1(ctr):
    scores = {'A X': 3, 'B X': 0, 'C X': 6,
              'A Y': 6, 'B Y': 3, 'C Y': 0,
              'A Z': 0, 'B Z': 6, 'C Z': 3}
    for k in scores.keys():
        scores[k] += 1 * ('X' in k) + 2 * ('Y' in k) + 3 * ('Z' in k) 
   
    return sum([ctr[k] * scores[k] for k in ctr.keys()])

def part_2(ctr):
    scores = {'A X': 3, 'B X': 1, 'C X': 2,
              'A Y': 4, 'B Y': 5, 'C Y': 6,
              'A Z': 8, 'B Z': 9, 'C Z': 7}
   
    return sum([ctr[k] * scores[k] for k in ctr.keys()])  

if __name__ == "__main__":
    
    test_data = Counter(['A Y', 'B X', 'C Z'])
    assert part_1(test_data) == 15
    assert part_2(test_data) == 12

    data = Counter([line.strip() for line in open('input.txt', 'r')])
    p1 = part_1(data)
    p2 = part_2(data)

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')