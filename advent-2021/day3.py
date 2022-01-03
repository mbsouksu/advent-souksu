from utils.utils import read_input
from operator import itemgetter
from collections import Counter

file=read_input('inputs/day3_input.txt')

def q1(file):
    gamma_rate = []
    for i in range(len(file[0])-1):
        elements = Counter(map(itemgetter(i), file))
        common_bit = elements.most_common(1)[0][0]
        gamma_rate.append(common_bit)
    epsilon_rate = int(''.join( ['1' if i == '0' else '0' for i in gamma_rate ]), 2)
    gamma_rate = int(''.join(gamma_rate), 2)
  
    print(f'answer: {gamma_rate * epsilon_rate}')
    #3901196

def q2(file, tiebreaker):

    i = 0
    while len(file) > 1:
        elements = Counter([x[i] for x in file]).most_common()
        if (elements[0][1] == elements[1][1]) == tiebreaker:
            bit = elements[-1][0]
        else:
            bit = elements[0][0]
        file = list(filter(lambda x: x[i] == bit, file))
        i += 1
    return int(file[0], 2)

    #print(f'answer: {gamma_rate * epsilon_rate}')
    #3901196

def get_binary_rating(is_reversed=False):
    remaining_numbers = file.copy()
    num_bits = int(len(file[0]))
    for i in range(num_bits):
        if len(remaining_numbers) == 1:
            break
        binary_columns = list(zip(*remaining_numbers))
        first_column = binary_columns[i]
        key_number = "0"
        if is_reversed:
            if first_column.count("0") > first_column.count("1"):
                key_number = "1"
        else:
            if first_column.count("1") >= first_column.count("0"):
                key_number = "1"
        new_remaining_numbers = []
        for number in remaining_numbers:
            if number[i] == key_number:
                new_remaining_numbers.append(number)
        remaining_numbers = new_remaining_numbers
    return remaining_numbers[0]

oxygen_gen_rating_binary = get_binary_rating()
co2_scubber_rating_binary = get_binary_rating(is_reversed=True)
oxygen_gen_rating = int(oxygen_gen_rating_binary, 2)
co2_scrubber_rating = int(co2_scubber_rating_binary, 2)
life_support_rating = oxygen_gen_rating * co2_scrubber_rating
print(f"Life support rating: {life_support_rating}")