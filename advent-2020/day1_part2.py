from utils.utils import read_input
import itertools

def main():
    file=read_input('inputs\day1_input.txt')
    file_int=list(map(int, file))
    file_sorted=sorted(file_int) #itertools.combinations works based on input sequence so sorting could fasten it up
    
    for first_number, second_number, third_number in itertools.combinations(file_sorted,3):
        if first_number + second_number + third_number==2020:
            print(f'Numbers are {first_number}, {second_number} and {third_number}')
            print(f'Result: {first_number * second_number * third_number}')

def main2():
    file=read_input('inputs\day1_input.txt')
    file_int=list(map(int, file))
    file_sorted=sorted(file_int)
    
    for index, first_number in enumerate(file_sorted):
        for second_number in file_sorted[index:]:
            cumulative = first_number + second_number
            if cumulative < 2020 and (2020-cumulative) in file_int:
                print(f'Numbers are {first_number}, {second_number} and {2020-cumulative}')
                print(f'Result: {first_number * second_number * (2020-cumulative)}')
                break
        else:
            continue  # Continue loop if inner `break` not reached
        break  # Inner `break` reached, break out of outer loop as well
    
def main3():
    file=read_input('inputs\day1_input.txt')
    file_int=list(map(int, file))
    file_sorted=sorted(file_int)
    
    found = False
    for index, first_number in enumerate(file_sorted):
        for second_number in file_sorted[index:]:
            cumulative = first_number + second_number
            if cumulative < 2020 and (2020-cumulative) in file_int:
                print(f'Numbers are {first_number}, {second_number} and {2020-cumulative}')
                print(f'Result: {first_number * second_number * (2020-cumulative)}')
                found = True
                break
        if found:
            break

def main4():
    file=read_input('inputs\day1_input.txt')
    file_int=list(map(int, file))
    file_sorted=sorted(file_int)
    
    found = False
    for index, first_number in enumerate(file_sorted):
        for second_number in file_sorted[index:]:
            cumulative = first_number + second_number
            if cumulative < 2020 and (2020-cumulative) in file_int:
                return print(f'Numbers are {first_number}, {second_number} and {2020-cumulative}'), print(f'Result: {first_number * second_number * (2020-cumulative)}')
            
if __name__ == '__main__':
    main()