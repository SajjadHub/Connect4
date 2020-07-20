import numpy
ROW_COUNT = 6
COLUMN_COUNT = 7


def dropPiece(board, col, player):
    """
    Function to place a piece in the lowest available row in the chosen column
    """
    boardCol = board[:, col]
    # Iterate through the col backwards
    for i, spot in enumerate(boardCol[::-1]):
        if spot:
            pass
        # if the whole col is full then return an error message
        # TODO: Allow the user to place in different col
        elif spot and i == 5:
            print("This coloumn is full, choose another")
        else:
            board[5 - i][col] = player
            break
    return board


# Copied from KeithGalli/Connect4-Python
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def printBoard(board):
    # Print the board every move
    for row in board:
        for spot in row:
            print(spot, end=" ")
        print("\n")


def game():
    """
    Holds main functionality for Connect 4 game
    """
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT), int)
    gameOver = False
    player1 = 1
    player2 = 2
    activePlayer = player1

    # Loop until the game is over or the board is full
    # One loop represents one player choice.
    # This activePlayer and the board represent the current game state
    while not gameOver:
        printBoard(board)

        col = int(input("Please choose a col from 0-6 to place your piece\n"))

        # Place the piece
        board = dropPiece(board, col, activePlayer)

        # Check if that placed piece results in a connect 4
        if winning_move(board, activePlayer):
            print("Player {} has won!!!".format(activePlayer))
            gameOver = True
            printBoard(board)
            break

        # Switch players at the end of the round
        if activePlayer == player1:
            activePlayer = player2
        else:
            activePlayer = player1


# Lets play!
if __name__ == '__main__':
    game()
