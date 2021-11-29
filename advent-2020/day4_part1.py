from utils.utils import read_input_whole
import re

def main():
    file = read_input_whole('inputs\day4_input.txt')
    file = file.split('\n\n')    
    
    count = 0
    for line in file:
        special_char=re.findall(':', line)
        
        if len(special_char) == 8:
            count += 1
        elif len(special_char) ==7 and 'cid' not in line:
            count += 1
    print(f'Answer: {count}')
    #Answer: 182

#way better approach
#https://topaz.github.io/paste/#XQAAAQABBAAAAAAAAAARiAaIocyAMoT6bRBBxWQ4kemaTUkt3JnRGN6zUZB4eQ9BKXpVNldzL9UHkxfZ8++300fxmIL9u0Q7jUikIsinmODFLNmw0tbPpuLxi4QbqQVetQg6bUXqK2mqBriDf/t3eXYGzZVot6h99Gc/2ucjDQ0BA3zjeaTvNJsYdyUFW/HZiqwzJd9Y5rC37ViywvCovGaRo+3SjJr3r6bKAztSNvMdSsV9k+IyXWiZMaDiwcHadBV5lr8rh+ucPJO8Acox8ovYXqspIlpKRqSV24LXfb3wRPd8ijPKxLhyCcyPI5zXDYaPfqwykrhjBRgX4NXGOs7UlwStjleIBNc9fD+vI75jgoojKCO6OwpXOFcUKx4KYiGS0MmZ3pzRyCL6f/YNJIukysrsNu9lm1qUkmiikFFLu18sJXofn44JRaHOB4tIyAOuhKKMORs57uJ0w5iHWN5i18HTHcmmpETwS6oJRiRgaMlad4lFqtVonWc7ue6BDWP8NXCiyV5WOzDFQPtlHhkrtlwp7EesRvekpXm9LYy/4goo6PNkt0+FpxWfob5N9ZIAHl7qTr8bO199ooovd4Ew4MWPXQf+ulOf1LaHLWQSBLHfuOZe8cn/VXSdAA==
def main2():
    file = read_input_whole('inputs\day4_input.txt')
    file = file.split('\n\n') 
    
    ValidTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ValidPassports = 0
    for passport in file:
        if all(x in passport for x in ValidTerms): #if all True, all returns True
            ValidPassports += 1 
   
    print(f'Answer: {ValidPassports}')
if __name__ == '__main__':
    main2()