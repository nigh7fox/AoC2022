import string
from collections import Counter

def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted

def itemWeight(letter):
    alphabetLowercase = list(string.ascii_lowercase)
    alphabetUppercase = list(string.ascii_uppercase)
    if (str(letter).islower()):
        return int(alphabetLowercase.index(letter) + 1)
    return int(alphabetUppercase.index(letter) + 27)

def totalWeight(sackDict):
    answer = 0
    for value in sackDict.values():
        for key in value.keys():
            answer += key
    return answer


def rugsack(input):
    compartmentWeight = {}
    for idx, sack in enumerate(input):
        firstCompartment = sack[0:int(len(sack)/2)]
        secondCompartment = sack[int(len(sack)/2):len(sack)]
        # Part 1
        compartmentWeight[idx] = Counter([itemWeight(letters) for letters in sack if letters in firstCompartment and letters in secondCompartment])
    return totalWeight(compartmentWeight)

def rugSackThrees(input):
    uniqueItems = []
    for idx, sack in enumerate(input):
        uniqueBags = set(sack)
        if (idx % 3 == 0):
            for items in uniqueBags:
                if (items in input[idx+1]) and (items in input[idx+2]):
                    uniqueItems.append(itemWeight(items))
    return sum(uniqueItems)

if __name__ == "__main__":
    # print(rugsack(readInput()))
    print(rugSackThrees(readInput()))