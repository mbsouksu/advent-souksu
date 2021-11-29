from utils.utils import read_input

def main():
    file = read_input(r'inputs\day9_input.txt')
    file = [int(x) for x in file]
    number = finder(file, 25)
    print(f'Answer: {number}')
    #Answer: 144381670
       
if __name__ == "__main__":
    main()