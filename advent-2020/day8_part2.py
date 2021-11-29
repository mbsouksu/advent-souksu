from utils.utils import read_input
from day8_part1 import stepup
import re

def second(file):
    for index, line in enumerate(file):
        instr, arg = line.split()
        if instr not in ['jmp', 'nop']:
            continue
        elif instr == 'jmp':
            file[index] = re.sub('jmp', 'nop', line)
        elif instr == 'nop':
            file[index] = re.sub('nop', 'jmp', line)
        retcode, retval = stepup(file)
        if retcode:
            return retval
        else:
            file[index] = instr + ' ' + arg         
                
def main():
    file = read_input(r'inputs\day8_input.txt')
    acc = second(file)
    print(f'Answer: {acc}')
    #Answer: 1121
    
if __name__ == "__main__":
    main()