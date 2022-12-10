def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.split('\n') for x in lines]
    linesFormatted = [y[0] for y in linesFormatted]
    linesFormatted = [z.split(",") for z in linesFormatted]
    return linesFormatted

def campCleanup(input, v2):
    elveOneAssignments = []
    elveTwoAssignments = []
    overlappingAssignments = 0
    schedule = [x for x in range(0,100)]
    for idx, assignments in enumerate(input):
        elveOne = assignments[0].split('-')      
        elveTwo = assignments[1].split('-')      
        elveOneAssignments.append(schedule[int(elveOne[0]):int(elveOne[1])+1])
        elveTwoAssignments.append(schedule[int(elveTwo[0]):int(elveTwo[1])+1])
    for idx, assignments in enumerate(elveOneAssignments):
        assignmentsLengthOne = len(elveOneAssignments[idx])
        assignmentsLengthTwo = len(elveTwoAssignments[idx])
        # v2 is the second part of the excersize
        if (v2):
            overlapFound = False
            if (assignmentsLengthOne > assignmentsLengthTwo):
                for assignment in elveTwoAssignments[idx]:
                    if (assignment in elveOneAssignments[idx]):
                        overlapFound = True
            elif (assignmentsLengthOne < assignmentsLengthTwo):
                for assignment in elveOneAssignments[idx]:
                    if (assignment in elveTwoAssignments[idx]):
                        overlapFound = True
            else:
                for assignment in elveOneAssignments[idx]:
                    if (elveOneAssignments[idx] == elveTwoAssignments[idx]):
                        overlapFound = True
                    else:
                        for assignments in elveOneAssignments[idx]:
                            if (assignments in elveTwoAssignments[idx]):
                                overlapFound = True
        else:
            overlapFound = True
            if (assignmentsLengthOne > assignmentsLengthTwo):
                for assignment in elveTwoAssignments[idx]:
                    if (assignment not in elveOneAssignments[idx]):
                        overlapFound = False
            elif (assignmentsLengthOne < assignmentsLengthTwo):
                for assignment in elveOneAssignments[idx]:
                    if (assignment not in elveTwoAssignments[idx]):
                        overlapFound = False
            else:
                for assignment in elveOneAssignments[idx]:
                    if (elveOneAssignments[idx] != elveTwoAssignments[idx]):
                        overlapFound = False
            print('overlap: %s | idx: %d | lengthOne: %d | lengthTwo: %d' % (overlapFound, idx, assignmentsLengthOne, assignmentsLengthTwo))
        if (overlapFound):
            overlappingAssignments += 1
    return overlappingAssignments

if __name__ == "__main__":
    print(campCleanup(readInput(), True))