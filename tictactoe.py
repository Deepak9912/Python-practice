import random


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = "X"
winnner = None
gameRunning = True


#To print the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# to display user input
def displayUserInput(board):
    inp = int(input("Please select any number between 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Opps wrong input")

# to check win, lose or tie
def horizontalCell(board):
    global winnner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def verticalCell(board):
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[6]
        return True

def dignalCell(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# to check win
def checkWin():
    global gameRunning
    if horizontalCell(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif verticalCell(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif dignalCell(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

# to check if there is a tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Opps! its a tie")
        gameRunning = False


# to switch the played
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# compluter play
def compluter(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# while loop to the game
while gameRunning:
    printBoard(board)
    displayUserInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    compluter(board)
    checkWin()
    checkTie(board)