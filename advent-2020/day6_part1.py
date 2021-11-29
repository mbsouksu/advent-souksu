from utils.utils import read_input_whole
import re
        
def main():
    file = read_input_whole(r'inputs\day6_input.txt')
    file = file.split('\n\n')
        
    count = 0
    for group in file:
        count += len(set(re.findall(r'\w', group)))
    print(f'Answer: {count}')
    #Answer: 6506
        
if __name__ == '__main__':
    main()