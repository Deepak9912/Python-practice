"""
Battleship game using functions
"""
import random

computer_input = [[" "] * 8 for x in range(8)]
user_input = [[" "] * 8 for i in range(8)]

def printBoard(board):

    print(" A B C D E F G H")
    print(" +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
}

def create_ships(board):
    for i in range(5):
        ship.row, ship.column = random.randint(0, 7), random.randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

def get_ship_location():
    row = input("Enter a row of the ship: ")
    while row not in "1 2 3 4 5 6 7":
        print("wrong input, please try again")
        row = input("Enter a row again ")
    
    column = input("Enter a column of the ship: ")
    while column not in "A B C D E F G H":
        print("wrong input, please try again ")
        column = input("Enter a row again ")

def count_hit_ships():
    hit_ships = 0
    for row in board:
        for column in row:
            if column == "X":
                hit_ships += 1
    return hit_ships

def gameRun():
    turns = 10
    while turns > 0:
        print("Guess the battleship location")
        printBoard(user_input)
        row, column = get_ship_location()
        if computer_input[row][column] == "-":
            print("You already guessed that")
        elif user_input[row][column] == "X":
            print("success!")
            computer_input[row][column] == "X"
            turns -= 1
        else:
            print("try again!")
            computer_input[row][column] = "-"
            turns -1
        
        if count_hit_ships(computer_board) == 5:
            print("you win")
            break
        print("you have " + str(turns) + " turns left")
        
        if turns == 0:
            print("you ran out of turns")

gameRun()