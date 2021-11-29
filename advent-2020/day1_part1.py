from utils.utils import read_input

def main():
    
    file=read_input('inputs\day1_input.txt')
    file_int=list(map(int, file))
    for number in file_int:
        if (2020 - number) in file_int:
            print(f'Two numbers are {number} and {2020-number}')
            print(f'Result: {number * (2020-number)}')
            break
    
if __name__ == '__main__':
    main()