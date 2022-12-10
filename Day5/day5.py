def readInput():
    with open('example_input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted


def supplyStacks(input):
    stacks = {}
    moves = []
    moveSplitterIdx = input.index('')
    moves = input[moveSplitterIdx+1:len(input)]
    grid = input[0:moveSplitterIdx]
    colStr = str(grid[len(grid)-1]) # full string of column numbers or last array in grid
    colStrNoSpace = colStr.replace(' ', '') # without space 123
    colIndexes = [colStr.index(col) for col in colStrNoSpace] # indexes where columns values are found in string
    stackMax = int(colStrNoSpace[len(colStrNoSpace)-1]) # last value in column string
    print('Amount of stacks: %d' % (stackMax))
    print(colIndexes)
    for idx, col in enumerate(colIndexes):
        print(col)
        stacks[idx] = [rows[col] for rows in grid]

    return stacks

if __name__ == "__main__":
    print(supplyStacks(readInput()))