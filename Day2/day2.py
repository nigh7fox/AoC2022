def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted

def compareRows(arr):
    return 0

def rockPaperScissors(input):
    """
        Games Rules:
        - Rock beats Scissors
        - Paper beats Rock
        - Scissors beats Paper
    """
    rpsGrid = [x.split(" ") for x in input]
    playerA = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    playerB = {
        'X': 1, # Rock
        'Y': 2, # Paper
        'Z': 3  # Scissor
    }
    score = {
        'playerA': 0,
        'playerB': 0
    }
    winPts = 6
    drawPts = 3

    for playerAMove, playerBMove in rpsGrid:
        print('PlayerA: %s - PlayerB: %s' % (playerA[playerAMove], playerB[playerBMove]))
        if (playerA[playerAMove] == playerB[playerBMove]):
            print("Draw.")
            score['playerB'] = score['playerB'] + playerB[playerBMove] + drawPts
        # DRY FIX THIS
        elif (playerB[playerBMove] is 1):
            if (playerA[playerAMove] is 2):
                print('Rock loses to paper')
                score['playerB'] = score['playerB'] + playerB[playerBMove]
            elif (playerA[playerAMove] is 3):
                print('Rock beats scissor')
                score['playerB'] = score['playerB'] + playerB[playerBMove] + winPts
        elif (playerB[playerBMove] is 2):
            if (playerA[playerAMove] is 1):
                print('Paper beats rock')
                score['playerB'] = score['playerB'] + playerB[playerBMove] + winPts
            elif (playerA[playerAMove] is 3):
                print('Paper loses to scissors')
                score['playerB'] = score['playerB'] + playerB[playerBMove]
        elif (playerB[playerBMove] is 3):
            if (playerA[playerAMove] is 1):
                print('Scissors loses to rock')
                score['playerB'] = score['playerB'] + playerB[playerBMove]
            elif (playerA[playerAMove] is 2):
                print('Scissors beats paper')
                score['playerB'] = score['playerB'] + playerB[playerBMove] + winPts
    return score['playerB']

if __name__ == "__main__":
    print(rockPaperScissors(readInput()))