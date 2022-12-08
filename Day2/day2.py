"""
    Games Rules:
    - Rock beats Scissors
    - Paper beats Rock
    - Scissors beats Paper
"""
winPts = 6
drawPts = 3
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

def readInput():
    with open('input.txt') as f:
        lines = f.readlines()
    linesFormatted = [x.strip('\n') for x in lines]
    return linesFormatted

def rockPaperScissors(input):

    rpsGrid = [x.split(" ") for x in input]
    score = {
        'playerA': 0,
        'playerB': 0
    }

    for playerAMove, playerBMove in rpsGrid:
        if (playerA[playerAMove] == playerB[playerBMove]):
            print("Draw.")
            score['playerB'] = score['playerB'] + playerB[playerBMove] + drawPts       
        match playerB[playerBMove]:
            case 1:
                if (playerA[playerAMove] == 2):
                    print('Rock loses to paper')
                    score['playerB'] = score['playerB'] + playerB[playerBMove]
                elif (playerA[playerAMove] == 3):
                    print('Rock beats Scissor')
                    score['playerB'] = score['playerB'] + playerB[playerBMove] + winPts
            case 2:
                if (playerA[playerAMove] == 1):
                    print('Paper beats rock')
                    score['playerB'] = score['playerB'] + playerB[playerBMove] + winPts
                elif (playerA[playerAMove] == 3):
                    print('Paper loses to Scissors')
                    score['playerB'] = score['playerB'] + playerB[playerBMove]
            case 3:
                if (playerA[playerAMove] == 1):
                    print('Scissors loses to rock')
                    score['playerB'] = score['playerB'] + playerB[playerBMove]
                elif (playerA[playerAMove] == 2):
                    print('Scissors beats paper')
                    score['playerB'] = score['playerB'] + playerB[playerBMove] + winPts
    return score['playerB']

def rockPaperScissorsV2(input):
    score = {
        'playerA': 0,
        'playerB': 0
    }
    rpsGrid = [x.split(" ") for x in input]
    for playerAMove, playerBMove in rpsGrid:
        match playerB[playerBMove]:
            case 1:
                print('Lose')
                if (playerA[playerAMove] == 1):
                    loseMove = 'Z'
                elif(playerA[playerAMove] == 2):
                    loseMove = 'X' 
                elif(playerA[playerAMove] == 3):
                    loseMove = 'Y'
                score['playerB'] = score['playerB'] + playerB[loseMove]
            case 2:
                print("Draw")
                score['playerB'] = score['playerB'] + playerA[playerAMove] + drawPts
            case 3:
                print("Win")
                if (playerA[playerAMove] == 1):
                    winMove = 'Y'
                elif(playerA[playerAMove] == 2):
                    winMove = 'Z'
                elif(playerA[playerAMove] == 3):
                    winMove = 'X'
                score['playerB'] = score['playerB'] + playerB[winMove] + winPts
    return score['playerB']

if __name__ == "__main__":
    # print(rockPaperScissors(readInput()))
    print(rockPaperScissorsV2(readInput()))