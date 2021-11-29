from utils.utils import read_input
import re

def add_child(parent_bag, bags_dict):
    children_counting = dict()
    
    def add_child_r(parent_bag, bags_dict):
        # If loop has elements that change the memory part, it will need nonlocal. 
        # But anyway, it is always safer option to use nonlocal. In this loop count= 
        # part change to update and it can be used without nonlocal
        nonlocal children_counting 
        content = bags_dict[parent_bag].strip().split(", ")
        if content[0]=='no other':
            return
        else:
            for child in content:                                       
                bagname = re.search(r"[a-zA-Z]+.[a-zA-Z]*", child)[0]   
                number = int(re.search(r"\d+", child)[0])              
                if bagname in children_counting:                        
                    children_counting[bagname] += number                
                else:                                                   
                    children_counting.update({bagname: number})                
                while number > 0:                                       
                    add_child_r(bagname, bags_dict)                     
                    number -= 1         
    
    add_child_r(parent_bag, bags_dict)
    return children_counting

def main():
    bags = read_input(r'inputs\day7_input.txt')
    bags_dict = {}                             # initialize the dict
    for bag in bags:                           # populate the dictionary
        bag = re.sub(r'( bags?|\.)', '', bag)  # Remove text not required
        bag = bag.split(" contain ")           # split each entry into parent and child bag - note the spaces
        bags_dict[bag[0]] = bag[1]
    count = add_child('shiny gold', bags_dict)
    print(f'Answer: {sum(count.values())}')
    #Answer: 45157        
    
if __name__ == "__main__":
    main()