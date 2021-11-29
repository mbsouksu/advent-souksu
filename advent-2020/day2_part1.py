from utils.utils import read_input
import re

def main():
    file=read_input('inputs\day2_input.txt')
    
    count = 0
    for password in file:
        boundaries =list(map(int,re.findall('\d+', password)))
        rule_string = re.findall("[a-zA-Z]", password)[0]
        limit = password.count(rule_string) - 1 #counting also the first one
        
        if limit >= boundaries[0] and limit <= boundaries[1]:
            count += 1
    print(count)
    #Answer: 620
    
if __name__ == '__main__':
    main()
    
