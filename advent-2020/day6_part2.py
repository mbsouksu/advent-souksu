from utils.utils import read_input_whole
import re
from collections import Counter
        
def main():
    file = read_input_whole(r'inputs\day6_input.txt')
    file = file.split('\n\n')
    
    count = 0
    for group in file:
        group_size = group.count('\n') + 1
        letters = Counter(re.findall(r'\w', group))
        count += Counter(list(letters.values()))[group_size]
    print(f'Answer: {count}')
    #Answer: 3243 

if __name__ == '__main__':
    main()