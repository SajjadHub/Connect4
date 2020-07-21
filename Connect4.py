import numpy
import os
import copy
ROW_COUNT = 6
COLUMN_COUNT = 7


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
            board[5 - i][col] = int(player)
            break
    return board


class game():
    """
    Holds main functionality for Connect 4 game
    """
    def __init__(self):
        self.board = numpy.zeros((ROW_COUNT, COLUMN_COUNT), int)
        self.gameOver = False
        self.player1 = 1
        self.player2 = 2
        self.activePlayer = self.player1
        self.winner = None

    # Loop until the game is over or the board is full
    # One loop represents one player choice.
    # This activePlayer and the board represent the current game state
    def run(self):
        while not self.gameOver:
            os.system('clear')
            printBoard(self.board)
            notValid = True
            while notValid:
                col = int(input("Please choose a col from 0-6 to place your piece\n"))
                if col < 0 or col > 6:
                    break
                for i in self.board[:, col]:
                    if not i:
                        self.move(col)
                        notValid = False
                        break
                if not self.gameOver:
                    print("Invalid")

    def move(self, col):
        # Place the piece
        tempBoard = copy.deepcopy(self.board)
        self.board = dropPiece(tempBoard, col, self.activePlayer)

        # Check if that placed piece results in a connect 4
        if winning_move(self.board, self.activePlayer):
            os.system('clear')
            self.gameOver = True
            self.winner = self.activePlayer
            printBoard(self.board)
            print("Player {} has won!!!".format(self.activePlayer))
        else:
            # Switch players
            self.activePlayer = self.getNextPlayer()

    # Returns the next player
    def getNextPlayer(self):
        if self.activePlayer == self.player1:
            return self.player2
        else:
            return self.player1


# Lets play!
if __name__ == '__main__':
    normal = game()
    normal.run()
