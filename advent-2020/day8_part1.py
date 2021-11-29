from utils.utils import read_input

def stepup(file):    
    index=0
    acc=0
    seenIndex = list()
    while index < len(file):
        
        if index in seenIndex:
            return False, acc
        else:
            seenIndex.append(index)
            step, step_size = file[index].split()
            step_size = int(step_size)
        
            if step == 'acc':
                index += 1
                acc += step_size
            elif step == 'jmp':
                index += step_size
            else:
                index += 1
    return True, acc

def main():
    file = read_input(r'inputs\day8_input.txt')
    acc = stepup(file)[1]
           
    print(f'Answer: {acc}')
    #Answer: 1331
       
if __name__ == "__main__":
    main()