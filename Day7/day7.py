answerV1 = 0
folderFileSizes = {}
def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted

def calculateDirectoriesTotal(fileSizeDict: dict, currentDirString):
    for pathName, filesDict in fileSizeDict.items():
        pathSum = sum([int(fileSize) for fileSize in filesDict.values()])
        if (pathName in folderFileSizes and pathName == currentDirString):
            folderFileSizes[currentDirString] = folderFileSizes[currentDirString] + pathSum
        elif (pathName not in folderFileSizes):
            folderFileSizes[pathName] = pathSum
            for pName, pTotal in folderFileSizes.items():
                if (pName == pathName):
                    pass
                elif (str(pathName).startswith(pName)):
                    folderFileSizes[pName] = folderFileSizes[pName] + pathSum


def changeDirectory(cmd, cd: list, currentLsOuput, directoryData: dict):
    currentDirectory = cd
    cdLocation = cmd[2]
    if (cdLocation == '..'):
        if (len(currentDirectory) != 1):
            currentDirectory.pop(len(currentDirectory)-1)
        else:
            print('Already at top directory')
    else:
        currentDirString = ''.join(currentDirectory)
        currentDirectoryList = [dir for dir in currentLsOuput if str(dir).startswith('dir')]
        directoryNameList = [dirName.split(' ')[1] for dirName in currentDirectoryList]
        newPath = currentDirString + cdLocation
        if (cdLocation != currentDirectory[len(currentDirectory)-1] or cdLocation in directoryNameList or len(currentDirString) - len(cdLocation) != 0):
            currentDirectoryFolders = directoryData[currentDirString]
            if (cdLocation in directoryNameList or currentDirectoryFolders.get(cdLocation) == 'dir'):
                currentDirectory.append(cdLocation)
                # print('Changing directory from %s to %s' % (currentDirectory[len(currentDirectory)-1], cdLocation))
            else:
                print('Directory not found')
        # else:
            # print('Already at that location')
    return currentDirectory


def listDirectory(input, lsIdx):
    currentLs = input[lsIdx+1:len(input)]
    lsOutputEndIdx = 0
    for idx, cmd in enumerate(currentLs):
        if (str(cmd).startswith('$')):
            lsOutputEndIdx = idx
            break
        else:
            lsOutputEndIdx = len(currentLs)
    return currentLs[0:lsOutputEndIdx]

def directorySize(input):
    directoryDict = {}
    filesDict = {}
    currentDirectory = ['/']
    currentListDirectory = []
    directorySizeSum = 0
    directorySizeSumV2 = 0
    for idx, shellLine in enumerate(input):
        tempDirDict = {}
        tempDirFilesDict = {}
        if (str(shellLine).startswith('$')):
            command = str(shellLine).split(' ')
            if (command[1] == 'cd'):
                changeDirectory(command, currentDirectory, currentListDirectory, directoryDict)
            else:
                # print('Listing Directory')
                currentListDirectory = listDirectory(input, idx)
                currentDirString = ''.join(currentDirectory)
                lsFiles = [fileData.split(' ') for fileData in currentListDirectory]
                for fileInfo in lsFiles:
                    if (fileInfo[0] == 'dir'):
                        if (directoryDict.get(currentDirString) != 'dir'):
                            tempDirDict[fileInfo[1]] = fileInfo[0]
                    else:
                        tempDirFilesDict[str(fileInfo[1])] = fileInfo[0]
                directoryDict[currentDirString] = tempDirDict
                filesDict[currentDirString] = tempDirFilesDict
                answerV1 = calculateDirectoriesTotal(filesDict, currentDirString)
    TOTAL_DISK_SPACE = 70000000 - int(folderFileSizes['/'])
    MAX_DISK_SPACE = 70000000
    MIN_DISK_SPACE = 30000000
    tmpTotal = 0
    for total in folderFileSizes.values():
        if (total < 100000):
            directorySizeSum += total
        if ((TOTAL_DISK_SPACE + total) > MIN_DISK_SPACE and (TOTAL_DISK_SPACE + total) < MAX_DISK_SPACE):
            if (total > 0 or total < directorySizeSumV2):
                directorySizeSumV2 = total

    # V2
    print('Free space %d' % (TOTAL_DISK_SPACE))
    print('V1 Total %d' % (directorySizeSum))
    print('V2 Total %d' % (directorySizeSumV2))
    return directorySizeSum

if __name__ == "__main__":
    directorySize(readInput()) # 1642503