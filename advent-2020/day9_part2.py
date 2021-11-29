from utils.utils import read_input
from day9_part1 import finder

def summer(file, number):
    step = 2 #create possible sum combinations, adding all to a list and check every time the sum could be another approach, this is faster
    
    while True:
        for i in range(file.index(number)-25): #loop until the week point and before preamble_length
            num = sum(file[i:i+step])
            if num == number:
                return min(file[i:i+step]) + max(file[i:i+step])
        else:
            step += 1

def main():
    file = read_input(r'inputs\day9_input.txt')
    file = [int(x) for x in file]
    number = finder(file, 25)
    result = summer(file, number)
    print(f'Answer: {result}')
    #Answer: 20532569
       
if __name__ == "__main__":
    main()