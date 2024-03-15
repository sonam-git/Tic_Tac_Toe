# variable declaration
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
currentPlayer = 'X'
winner = None
gameRunning = True


# display board created
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("----------")


# player input functionality
def player_input(board):
    playerInput = int(input('Enter a number 1 - 9: '))
    if 1 <= playerInput <= 9 and board[playerInput - 1] == "-":
        board[playerInput - 1] = currentPlayer
    else:
        print("Opps! player is already in that spot!")


player_input(board)


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
