def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted

def calourieCounting(input):
    elveCalArr = []
    elveCals = {}
    elveCount = 1
    elveMax = 0
    step = 0
    for idx, val in enumerate(input):
        if val == '':
            elveCals[elveCount] = sum([int(cal) for cal in input[step:idx]])
            step = idx + 1
            elveCount += 1
        if (step != len(input)):
            elveCals[elveCount] = sum([int(x) for x in input[step:len(input)] if x != ''])
    
    for key, value in elveCals.items():
        if (value > elveMax):
            elveMax = value

    sortedElves = sorted(elveCals.items(), key=lambda x: x[1], reverse=True)
    
    for key, value in sortedElves:
        elveCalArr.append(value)
    elveMax = sum(elveCalArr[0:3])
    print(elveCalArr[0:3])
    return elveMax

if __name__ == "__main__":
    print(calourieCounting(readInput()))
