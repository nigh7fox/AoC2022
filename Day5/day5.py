def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted

def supplyCrateIsEmpty(stack):
    return len([s for s in stack if str(s).isspace()]) == len(stack) or len(stack) == 0

def getTopCrate(stack: list):
    stackFormatted = [s for s in stack if not str(s).isspace()]
    return stack[stack.index(stackFormatted[len(stackFormatted)-1])]

def getBottomCrate(stack: list):
    return stack[0]
        
def moveCrate(move, stacks: dict,version):
    tempStack = stacks
    for idx, amount in enumerate(range(1, move[0]+1)):
        fromStack: list = tempStack[move[1]]
        toStack: list = tempStack[move[2]]
        if (version == 1):
            crateToMove = getTopCrate(tempStack[move[1]])
        else:
            if (int(move[0]) > 1):
                crateToMove = tempStack[move[1]][0]
            else:
                crateToMove = getTopCrate(tempStack[move[1]])
        print('Moving %s from %a to %a' % (crateToMove, fromStack, toStack))
        if (' ' not in toStack):
            toStack.append(' ')
        toStack[toStack.index(' ')] = crateToMove
        chosenCrateIdxArr = [[idx, letters] for idx, letters in enumerate(fromStack) if letters == getTopCrate(fromStack)]
        chosenCrateIdx = 0
        if(version == 1):
            if (len(chosenCrateIdxArr) > 1):
                chosenCrateIdx = chosenCrateIdxArr[len(chosenCrateIdxArr)-1][0]
            else:
                chosenCrateIdx = fromStack.index(getTopCrate(fromStack))
        else:
            if (int(move[0]) > 1):
                chosenCrateIdx = 0
            else:
                if (len(chosenCrateIdxArr) > 1):
                    chosenCrateIdx = chosenCrateIdxArr[len(chosenCrateIdxArr)-1][0]
                else:
                    chosenCrateIdx = fromStack.index(getTopCrate(fromStack))
        # fromStack[chosenCrateIdx] = ' '
        fromStack.pop(chosenCrateIdx)
        tempStack[move[1]] = fromStack
        tempStack[move[2]] = toStack
    print(tempStack)
    return tempStack

def moveCrates(moves, stacks: dict, version):
    stackAfterMove = stacks
    for idx, move in enumerate(moves):
        moveSplit = move.split(' ')
        moveAmount = int(moveSplit[1])
        moveFromStack = int(moveSplit[3])
        moveToStack = int(moveSplit[5])
        moveCrate([moveAmount, moveFromStack, moveToStack], stackAfterMove, version)
    return stackAfterMove

def supplyStacks(input, version) -> dict:
    stacks = {}
    moves = []
    moveSplitterIdx = input.index('')
    moves = input[moveSplitterIdx+1:len(input)]
    grid = input[0:moveSplitterIdx-1]
    colStr = str(input[moveSplitterIdx-1]) # full string of column numbers or last array in grid
    colStrNoSpace = colStr.replace(' ', '') # without space 123
    colIndexes = [colStr.index(col) for col in colStrNoSpace] # indexes where columns values are found in string
    stackMax = int(colStrNoSpace[len(colStrNoSpace)-1]) # last value in column string
    print('Amount of stacks: %d' % (stackMax))
    for idx, col in enumerate(colIndexes):
        stacks[idx+1] = [rows[col] for rows in grid][::-1]
    return moveCrates(moves, stacks, version)

def getTopCrates(stackDict: dict):
    for k, v in stackDict.items():
        if supplyCrateIsEmpty(v) is False:
            print(getTopCrate(v), end='')

if __name__ == "__main__":
    # print(supplyStacks(readInput()))
    # getTopCrates(supplyStacks(readInput(), 1)) # WSFTMRHPP
    getTopCrates(supplyStacks(readInput(), 2)) # GSLCMFBRP