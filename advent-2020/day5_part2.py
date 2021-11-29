from utils.utils import read_input
import math

#elegant solution with yield
#https://stackoverflow.com/questions/16974047/efficient-way-to-find-missing-elements-in-an-integer-sequence
def missing_elements(L):
    l = sorted(L)
    return sorted(set(range(l[0], l[-1] + 1)).difference(L))
        
def main():
    file=read_input('inputs\day5_input.txt')
    
    ids = list()
    for line in file:
        min_row = 0
        max_row = 127
        for i in line[:7]:
            if i == 'F':
                max_row = math.floor((min_row + max_row) / 2)
            elif i == 'B':
                min_row = math.ceil((min_row + max_row) / 2)
        
        min_col = 0
        max_col = 7
        for i in line[7:]:
            if i == 'L':
                max_col = math.floor((min_col + max_col) / 2)
            elif i == 'R':
                min_col = math.ceil((min_col + max_col) / 2)
        ids.append(min_row*8 + min_col)
    
    print(f'Answer: {missing_elements(ids)[0]}')
    #Answer: 603
    
if __name__ == '__main__':
    main()