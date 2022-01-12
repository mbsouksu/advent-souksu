with open('inputs/day2_input.txt', 'r') as f:
    file = f.read().splitlines()


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
    return horizontal*depth
    

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
    return horizontal*depth

if __name__ == '__main__':
    print(q1(file)) #Answer: 1815044
    print(q2(file)) #Answer: 1739283308