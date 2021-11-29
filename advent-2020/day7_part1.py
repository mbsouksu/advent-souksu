from utils.utils import read_input
import re

#https://topaz.github.io/paste/#XQAAAQDsCQAAAAAAAAARiAaIocyAMoT6bRHScawDa8677BWE1nqwUxOIlQeZKrD4cqo9iXP46lb15D1zmXBzUOpNrVgwPc4tyfaZ97LW7USUYtZiPl/ygvaaZvzlHixvDF7Kv6PpR5vsOjF/zQcTZlnIpWJ34zLeue5M2Vai2d8GS0DJQw6gnWl6qKX1QBbAW8TroDTsZHo8lVwsHu3JTZ/41bcZhXi0qg8jomsxpAOBABP96FT8ct+EAzrKOHY58WnMcB626gq1VoGwiP76DZ/xmblwahdfojH/ZCyV/gol7iAGV/AlyJdYh1Rsbedxm9HoHUyxY5UYi0j1NzQwTAExbs+adWwK/8tjhWFY+FVisT3m/BehhjS/i9buBh9PyFwLsKnVlzrS5RZm/jTaz286dSfQnxzGL0W4OcMWto1c1rH70BTV5m5xxcX3zT30i1oLFFO4sDOHcDguLc97OXyBCh3n3d4etLkZuRsZAzt0aNnsv7/KqkQJp04d+G+m03EiWh1OiHsNNrugvRtUFIJDc33gTT/Fsy+LQcK7WTvYFIBfq+rQOz5hle6UMNa0u+at5Fwh5Ux3qdUvVA2FFVG433Heyz32nKlYUVuiwNC48LbOz1N2ZNM3pxSrCTYAPz1oqF/TgUfuedVfEcH9Erh5uicmLdunBEULRMPyoylXY0mZehaZWHN0VWqNWRY6n2KgctFwgS93Ue7K0Czpb3s4I3zwhv7y4g0BqQ/zrSKJ/A/0Z5wS5Z1AN7vIeagRU2asEYcj+8WLN1oXtSY3qmoM7PP5xw1uCA7nyr2ebiIKXyV8hv3q/cNniqiCsEb1YhfswVcTjb5mWiHOtFpvZCD6k/Q/gAa9ye+nhMlgnfdCg4G4PCtmnDDgnISY2a1od0t8Oy/4LTbmE9zlFgzFsN0WQQmGBevDw0oUb8HVqJH0w0/kpE+DjvlKmhwYMdQ98onX4TgfRyi088QyggyMnlAyFdsZPetzuEXEVqNJIVJh+RK8fqzCgEPqKxUn9HNuzKnfITNA+7Dn0w/Vy/7Ccp4QeMcr/aGpxYUrCM2Xt/MKAZwZEuTr5a86u2uwiLu420JNyKM1Or12d2SeISSwq/ILS/Bu7vRSUpZuor502camSfUBw5/Zzl0In3usLJg0JdhEhCkzlTl99YMMQm9OlzJqgo3ADynpiLscvsB+zF8LHv/4+eTzJ8ZuDKxBXGSQNm7qOhINJ0Mnm4nK68glk0jfJ5dlgkIeZOJ8dfANBZlAyElEOAT3urDX+vaI1hRcsNF/cLBUVCKYca7VE/8OQ9gA
def parentbag(childbag, bags_dict):
    bagset = set()
    
    def parentbag_r(childbag, bags_dict):
        nonlocal bagset
        for parent in bags_dict:            # iterate through the different bags
            content = bags_dict[parent]     # what bags can be in parent bag
            if childbag in content:         # if the requested bag can be in parent bag
                parentbag_r(parent, bags_dict)         # recursion to see what bag can hold the parent bag
                bagset.add(parent)          # add bag to set of bags allowed to (eventually) hold childbag
    
    parentbag_r(childbag, bags_dict)
    return bagset  

def main():
    bags = read_input(r'inputs\day7_input.txt')
        
    bags_dict = {}                             # initialize the dict
    for bag in bags:                           # populate the dictionary
        bag = re.sub(r'( bags?|\.)', '', bag)  # Remove text not required
        bag = bag.split(" contain ")           # split each entry into parent and child bag - note the spaces
        bags_dict[bag[0]] = bag[1]             # populate the dict. Key: parent, value: child    

    bagset = parentbag("shiny gold", bags_dict)
    print(f'Answer: {len(bagset)}')
    #Answer: 278

if __name__ == "__main__":
    main()