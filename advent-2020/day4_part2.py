from utils.utils import read_input_whole
import re

def main():
    file = read_input_whole('inputs\day4_input.txt')
    file = file.split('\n\n')    
    
    count = 0
    for line in file:
        if (re.search(r'byr:19[2-9]\d|byr:200[0-2]', line) and re.search(r'iyr:201\d|iyr:2020', line) and re.search(r'eyr:202\d|eyr:2030', line) and
            re.search(r'hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in', line) and re.search(r'hcl:#\w{6}', line) and 
            re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)', line) and re.search(r'pid:\d{9}\b', line)):
            
            count += 1
    print(f'Answer: {count}')
    #Answer: 109          

if __name__ == '__main__':
    main()