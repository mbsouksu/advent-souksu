from operator import itemgetter
from collections import Counter


with open('inputs/day3_input.txt', 'r') as f:
    file = f.read().splitlines()

def q1(file, rate: str):
    rate_types = ['gamma', 'epsilon']
    if rate not in rate_types:
        raise ValueError("rate must be one of %r." % rate_types)
        
    elements = Counter(map(itemgetter(0), file))
    if rate == 'gamma':
        common_bit = elements.most_common()[0][0]
    elif rate == 'epsilon':
        common_bit = elements.most_common()[1][0]

    if len(file[0]) == 1:
        return common_bit
    else:
        file = [x[1:] for x in file]
        return common_bit + q1(file, rate)


def q2(file, tiebreaker):
    elements = Counter(map(itemgetter(0), file)).most_common()
    if elements[0][1] == elements[1][1]:
        target_bit = str(tiebreaker)
    else:
        if tiebreaker == 1:
            target_bit = str(elements[0][0])
        else:
            target_bit = str(elements[1][0])
    
    if len(file) == 2:
        return [word for word in file if word.startswith(target_bit)][0]
    else:
        file = list(filter(lambda x: x[0] == target_bit, file))
        file = [x[1:] for x in file]
        return target_bit + q2(file, tiebreaker)

if __name__ == '__main__':

    gamma = int(q1(file, 'gamma'), 2)
    epsilon = int(q1(file, 'epsilon'), 2)
    print(gamma * epsilon) #Answer: 3901196
    
    oxygen = int(q2(file, 1), 2)
    co2 =  int(q2(file, 0), 2)
    print(oxygen * co2) #Answer: 4412188

