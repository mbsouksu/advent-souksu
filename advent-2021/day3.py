from operator import itemgetter
from collections import Counter


with open('inputs/day3_input.txt', 'r') as f:
    file = f.read().splitlines()

def q1(file):
    gamma_rate = []
    for i in range(len(file[0])-1):
        elements = Counter(map(itemgetter(i), file))
        common_bit = elements.most_common(1)[0][0]
        gamma_rate.append(common_bit)
    epsilon_rate = int(''.join( ['1' if i == '0' else '0' for i in gamma_rate ]), 2)
    gamma_rate = int(''.join(gamma_rate), 2)
    
    return gamma_rate * epsilon_rate
    #3901196



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

    print(q1(file))
    oxygen = int(q2(file, 1), 2)
    co2 =  int(q2(file, 0), 2)
    print(oxygen * co2) #Answer: 4412188

