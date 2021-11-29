from utils.utils import read_input

def main():
    file = read_input('inputs\day3_input.txt')
    length = len(file[0]) - 1
    
    loc_x = 0
    count = 0
    
    for line in file:
        if loc_x >= length:
            loc_x = loc_x%length
        
        if line[loc_x] == '#':
            count += 1
        
        loc_x += 3
    
    print(f'Answer: {count}')
    #Answer: 228
    
if __name__ == '__main__':
    main()