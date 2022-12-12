def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted

def startOfPacketMarket(input, charSlice):
    marker = 0
    for idx, dsBuffer in enumerate(input):
        for idxChar, bufferChar in enumerate(dsBuffer):
            dsBufferSetLength = len(set(dsBuffer[idxChar:idxChar+charSlice])) # remove duplicates
            if (dsBufferSetLength > (charSlice-1) and marker == 0): # 4 characters with 1 double = 3 unique characters
                marker = idxChar + charSlice
                print('Marker at position: %d' % (marker))
        marker = 0
    return marker

if __name__ == "__main__":
    # v1 = startOfPacketMarket(readInput(), 4)
    v2 = startOfPacketMarket(readInput(), 14)