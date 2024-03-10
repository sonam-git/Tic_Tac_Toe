board = ["X","O","X",
         "O","X","O",
         "X","O","X",]


#display board created
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("----------")
print_board(board)