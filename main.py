# variable declaration
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-", ]
currentPlayer = 'X'
winner = None
gameRunning = True


# display board created
def printBoard(game_board):
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("----------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("----------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])
    print("----------")


# player input functionality
def playerInput(game_board):
    playerInp = int(input('Enter a number 1 - 9: '))
    if 1 <= playerInp <= 9 and game_board[playerInp - 1] == "-":
        game_board[playerInp - 1] = currentPlayer
    else:
        print("Opps! player is already in that spot!")


playerInput(game_board)


# check win function
# horizontal check
def checkHorizontal(game_board):
    global winner
    if game_board[0] == game_board[1] == game_board[2] and game_board[1] != "-":
        winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":
        winner = game_board[6]
        return True


# row check
def checkRow(game_board):
    global winner
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != "-":
        winner = game_board[1]
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "-":
        winner = game_board[2]
        return True


# diagonal check
def checkDag(game_board):
    global winner
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != "-":
        winner = game_board[2]
        return True


# tie check

def checkTie(game_board):
    if "-" not in game_board:
        printBoard(game_board)
        print("It is a tie!")
        gameRunning = False


def checkWin():
    if checkDag(game_board) or checkHorizontal(game_board) or checkRow(game_board):
        print(f"The winner is{winner}")


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'


while gameRunning:
    print(game_board)
    playerInput(game_board)
    checkWin()
    checkTie(game_board4)
    switchPlayer()
