from utils.utils import read_input
import itertools

def finder(file, preamble_length):
    
    for i in range(preamble_length, len(file)-25): 
        stop_rule = 0
        preamble_list = file[:i] #take 25 number
        target_num = file[i]
        for first_number, second_number in itertools.combinations(preamble_list,2):
            if first_number + second_number == target_num: #check if it has a sum
                stop_rule += 1
        if stop_rule == 0: #if it has return it
            return target_num

def main():
    file = read_input(r'inputs\day9_input.txt')
    file = [int(x) for x in file]
    number = finder(file, 25)
    print(f'Answer: {number}')
    #Answer: 144381670
       
if __name__ == "__main__":
    main()