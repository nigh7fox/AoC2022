def readInput():
    with open('example_input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted

def startOfPacketMarket(input):
    for dsBuffer in input:
        print(dsBuffer)
    return input

if __name__ == "__main__":
    startOfPacketMarket(readInput())