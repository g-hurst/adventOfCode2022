class file_tree():
    def __init__(self, name, contents=[], size=0):
        self.name      = name
        self.contents  = contents
        self.size      = size
    
def parse_data(f_name):
    # builds a file tree from the command log file. 
    def build_tree(log, parent=None):
        while len(log) > 0:
            line = log.pop(0)
            if '$ cd ..' in line:
                return log
            elif '$ cd ' in line:
                dir_name = 'dir ' + line.replace('$ cd ','')
                new_parent = file_tree(name=dir_name, contents=[], size=0)
                if parent != None:
                     parent.contents[parent.contents.index(dir_name)] = new_parent
                log = build_tree(log, new_parent)
            elif '$ ls' in line:
                while(len(log) > 0 and '$' not in log[0]):
                    parent.contents.append(log.pop(0))
        
        if parent == None:
            return new_parent
        else:
            return log
    
    # assigns sizes to each of the directories in the file tree
    def assign_sizes(head):
        total = 0
        for item in head.contents:
            if type(item) == str:
                total += int(item.split()[0])
            else:
                item.size = assign_sizes(item)
                total += item.size
        return total

    # calling the functions to make the file tree
    log = [line.strip() for line in open(f_name, 'r')]  
    head      = build_tree(log)
    head.size = assign_sizes(head)
    
    return head

def part_1(head):
    total = 0
    for item in head.contents:
        if type(item) == file_tree:
            if item.size <= 100000:
                total += item.size
            total += part_1(item)  
    return total 


def part_2(head, closest_sz, needed_sz):
    for item in head.contents:
        if type(item) == file_tree:
            if (item.size > needed_sz) and (needed_sz - closest_sz) < (needed_sz - item.size):
                closest_sz = item.size
            closest_sz = part_2(item, closest_sz, needed_sz)
    return closest_sz

if __name__ == '__main__':
    example = parse_data('example.txt')
    head    = parse_data('input.txt')

    get_sz = lambda x: 30000000 - (70000000 - x)

    assert part_1(example) == 95437
    assert part_2(example, example.size, get_sz(example.size)) == 24933642

    p1 = part_1(head)
    p2 = part_2(head, head.size, get_sz(head.size))

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')
