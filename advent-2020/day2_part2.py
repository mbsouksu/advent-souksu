from utils.utils import read_input
import re

def main():
    file=read_input('inputs\day2_input.txt')
    
    count = 0
    for password in file:
        positions =list(map(int,re.findall('\d+', password)))
        rule_string = re.findall("[a-zA-Z]", password)[0]
        letter = password.split(': ')[1]
        
        position_one = letter[positions[0]-1] == rule_string #Check the condition
        position_two = letter[positions[1]-1] == rule_string
        if position_one + position_two ==1:
            count+=1
    print(f'Answer: {count}')
    #Answer: 727
        
if __name__ == '__main__':
    main()