def part_2(f_name):
    with open(f_name, 'r') as f:
        food_lists = f.read().split('\n\n')

    food_sums = [sum(list(map(int, food.split()))) for food in food_lists]
    top_three = sorted(food_sums)[-3:]
    
    return sum(top_three)

if __name__ == '__main__':
    f_name = 'day1\input.txt'
    
    assert part_2('day1\example.txt') == 45000
    p2 = part_2(f_name)
    print(f'answer to part 2: {p2}')