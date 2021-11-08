# Realizati un program care are ca scop crearea jocului X&0 în care un participant e uman
#   și celălalt este calculatorul. De asemenea, pentru alegerea unei căsuțe libere de către
#   calculator sau de către om aveți în vedere următoarele:
# - intrările sunt de la 1 la 9 astfel:
# 	1|2|3
# 	4|5|6
# 	7|8|9
# - poziția 5 este cea mai vânată
# - poziția 1 sau 3 sau 7 sau 9 reprezintă opțiunea a doua în cerință calculatorului.
#   Prima valorea disponibilă dintre acestea va fi marcată cu 0 de către calculator
# - în cazul în care toate acestea sunt ocupate se încearcă prima valoare rămasă libere dintre 2, 4, 6, 8
# - partea grafica se poate realiza cu ajutorul semnului |

from enum import Enum


class Player(Enum):
    COMPUTER = 0
    HUMAN = 1  # X


winner = None
filledPositions = 0
currentGame = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
wantedPosition = [5, 1, 3, 7, 9, 2, 4, 6, 8]


def gameWon(currentPlayer):
    global currentGame

    if currentPlayer == Player.COMPUTER:
        currentLetter = 'O'
    else:
        if currentPlayer == Player.HUMAN:
            currentLetter = 'X'
        else:
            return False

    if currentGame[0] == currentLetter and currentGame[1] == currentLetter and currentGame[2] == currentLetter:
        return True
    if currentGame[3] == currentLetter and currentGame[4] == currentLetter and currentGame[5] == currentLetter:
        return True
    if currentGame[6] == currentLetter and currentGame[7] == currentLetter and currentGame[8] == currentLetter:
        return True
    if currentGame[0] == currentLetter and currentGame[3] == currentLetter and currentGame[6] == currentLetter:
        return True
    if currentGame[1] == currentLetter and currentGame[4] == currentLetter and currentGame[7] == currentLetter:
        return True
    if currentGame[2] == currentLetter and currentGame[5] == currentLetter and currentGame[8] == currentLetter:
        return True
    if currentGame[0] == currentLetter and currentGame[4] == currentLetter and currentGame[8] == currentLetter:
        return True
    if currentGame[2] == currentLetter and currentGame[4] == currentLetter and currentGame[6] == currentLetter:
        return True

    return False

def drawBoard():
    global currentGame
    print("")
    for i in range(len(currentGame)):
        if i % 3 == 0:
            print("| ", end="")

        print(f" {currentGame[i]} |", end="")

        if i % 3 == 2:
            print("")

    print("")


whoStarts = input("Who starts? Computer or Human?")
while whoStarts != "Computer" and whoStarts != "Human":
    whoStarts = input("Invalid choice. Pick between Computer or Human.")

if whoStarts == "Computer":
    currentTurn = Player.COMPUTER
else:
    currentTurn = Player.HUMAN

while filledPositions < 9 and winner is None:
    if currentTurn == Player.COMPUTER:
        currentGame[wantedPosition[0] - 1] = 'O'
        wantedPosition.remove(wantedPosition[0])
        currentTurn = Player.HUMAN
    else:
        chosenPosition = int(input("Pick a position for X: "))
        while 1 > chosenPosition > 9:
            chosenPosition = int(input("Position must be between 1 and 9. Try again: "))
        currentGame[chosenPosition - 1] = 'X'
        wantedPosition.remove(chosenPosition)
        currentTurn = Player.COMPUTER

    filledPositions += 1

    if gameWon(currentTurn) is True:
        break
    else:
        drawBoard()

if gameWon(Player.HUMAN):
    print("You won the game! Congrats!")
else:
    if gameWon(Player.COMPUTER):
        print("You lost! The computer won.")
    else:
        if filledPositions == 9:
            print("Game has no winner.")
        else:
            print("Invalid game.")
