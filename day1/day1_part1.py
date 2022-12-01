def part_1(f_name):
    with open(f_name, 'r') as f:
        food_lists = f.read().split('\n\n')

    food_sums = [sum(list(map(int, food.split()))) for food in food_lists]

    return max(food_sums)


if __name__ == '__main__':
    f_name = 'day1\input.txt'
    
    assert part_1('day1\example.txt') == 24000
    p1 = part_1(f_name)
    print(f'answer to part 1: {p1}')
    