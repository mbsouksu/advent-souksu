from itertools import pairwise, islice
import collections

with open('inputs/day1_input.txt', 'r') as f:
    file = f.read().splitlines()
    file=list(map(int, file))

def q1(file):
    

    previous_number = file[0]
    count = 0
    for i,number in enumerate(file):
        if number > previous_number:
            count += 1
        previous_number = file[i]
    
    return count

def q2(file):
    previous_sum = sum(file[:3])
    count = 0
    for (a, _), (b, c) in pairwise(pairwise(file)):
        if a + b + c > previous_sum:
            count += 1  
        previous_sum = a + b + c

    return count


if __name__ == '__main__':
    print(q1(file)) #Answer: 1393
    print(q2(file)) #Answer: 1359