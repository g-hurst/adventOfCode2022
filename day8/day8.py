import numpy as np

def parse_data(f_name):
    return np.array([[int(n) for n in line.strip()] for line in open(f_name, 'r')], dtype=int)

def part_1(data):
    total_visible = 0
    marked = np.zeros(data.shape)
    
    for i in range(data.shape[1]):
        # traverse across the top
        curr = 0
        marked[curr][i] = 1
        big = data[curr][i]
        while(big < 9 and curr < data.shape[0] - 1):
            curr += 1
            if data[curr][i] > big:
                big = data[curr][i]
                marked[curr][i] = 1
        
        # traverse across the bottom
        curr = data.shape[0] - 1
        marked[curr][i] = 1
        big = data[curr][i]
        while(big < 9 and curr > 1):
            curr -= 1
            if data[curr][i] > big:
                big = data[curr][i] 
                marked[curr][i] = 1
                    
    for i in range(1, data.shape[0] - 1): 
        # traverse across left
        curr = 0
        marked[i][curr] = 1
        big = data[i][curr]
        while(big < 9 and curr < data.shape[1] - 1):
            curr += 1
            if data[i][curr] > big:
                big = data[i][curr]
                marked[i][curr] = 1
        
        # traverse across right
        curr = data.shape[1] - 1
        marked[i][curr] = 1
        big = data[i][curr]
        while(big < 9 and curr > 1):
            curr -= 1
            if data[i][curr] > big:
                big = data[i][curr]
                marked[i][curr] = 1

    return int(np.sum(marked))


def part_2(data):
    def get_score(i, j):
        left  = 1
        right = 1
        up    = 1
        down  = 1
        while j - left  > 0             and data[i][j - left]  < data[i][j]: left  += 1
        while j + right < data.shape[1] - 1 and data[i][j + right] < data[i][j]: right += 1
        while i - up    > 0             and data[i - up][j]    < data[i][j]: up    += 1
        while i + down  < data.shape[0] - 1 and data[i + down][j]  < data[i][j]: down  += 1
        if left  == 0: left  = 1
        if right == 0: right = 1
        if up    == 0: up    = 1
        if down  == 0: down  = 1
        return left * right * up * down
    
    scores = np.zeros(data.shape)
    for i in range(1, scores.shape[0] - 1):
        for j in range(1, scores.shape[1] - 1):
            scores[i][j] = get_score(i, j)
    return int(scores.max())

if __name__ == '__main__':
    example = parse_data('example.txt')
    data    = parse_data('input.txt')

    assert part_1(example) == 21
    assert part_2(example) == 8

    p1 = part_1(data)
    p2 = part_2(data)

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')