from utils.utils import read_input

file=read_input('inputs/day2_input.txt')

def q1(file):
    horizontal, depth = 0, 0
    for i in file:
        match i.split():
            case ["forward", x]:
                horizontal += int(x)
            case ["down", x]:
                depth += int(x)
            case [_, x]:
                depth -= int(x)
    print(f'Answer: {horizontal*depth}')
    #1815044

def q2(file):
    horizontal, depth, aim = 0, 0, 0
    for i in file:
        match i.split():
            case ["forward", x]:
                horizontal += int(x)
                depth += aim * int(x)
            case ["down", x]:
                aim += int(x)
            case [_, x]:
                aim -= int(x)
    print(f'Answer: {horizontal*depth}')
    #1739283308

if __name__ == '__main__':
    q2(file)