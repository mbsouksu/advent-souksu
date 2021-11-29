from utils.utils import read_input
from functools import reduce

def main():
    file = read_input('inputs\day3_input.txt')
    length = len(file[0]) - 1
    
    step_sizes = [(1,1),(3,1), (5,1), (7,1), (1,2)]
    
    results = list()
    
    for step_hor, step_ver in step_sizes:
        loc_x = 0
        count = 0
        
        for line in file[::step_ver]:
            
            if loc_x >= length:
                loc_x = loc_x%length
            
            if line[loc_x] == '#':
                count += 1
            
            loc_x += step_hor
        results.append(count)
        
    print(f'Answer: {reduce(lambda x,y: x*y, results)}')
    #Answer: 6818112000
    
if __name__ == '__main__':
    main()