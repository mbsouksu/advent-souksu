from utils.utils import read_input
from itertools import pairwise, islice
import collections

file=read_input('inputs/day1_input.txt')
file=list(map(int, file))

def q1(file):
    

    previous_number = file[0]
    count = 0
    for i,number in enumerate(file):
        if number > previous_number:
            count += 1
        previous_number = file[i]
    
    print(f'Answer: {count}')
    #1393

def q2(file):
    previous_sum = sum(file[:3])
    count = 0
    for (a, _), (b, c) in pairwise(pairwise(file)):
        if a + b + c > previous_sum:
            count += 1  
        previous_sum = a + b + c

    print(f'Answer: {count}')
    #1359

def sliding_window(iterable, n): #from python recipes
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield list(window)
    for x in it:
        window.append(x)
        yield list(window)

def q2_v2(file):
    previous_sum = sum(next(sliding_window(file, 3)))
    count = 0
    for a in sliding_window(file[1:], 3):
        if sum(a) > previous_sum:
            count += 1  
        previous_sum = sum(a)

    print(f'Answer: {count}')

if __name__ == '__main__':
    q2(file)