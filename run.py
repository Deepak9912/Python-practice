import random

print("Welcome to Rock paper scissor game")


def playGame():

    user_selection = input("Please select an option(rock, paper, scissor): ")

    possible_choice = ["rock", "paper", "scissor"]
    computer_selection = random.choice(possible_choice)

    if user_selection == computer_selection:
        print(f"\n You both chose {user_selection}, therefore its a tie")
    elif user_selection == "rock":
        if computer_selection == "scissor":
            print(f"\n rock smashes scissor, therefore you win")
        else:
            print(f"\n Paper covers roc, you lose")
    elif user_selection == "scissor":
        if computer_selection == "paper":
            print(f"\n Scissor cuts papaer, you win")
        else:
            print("\n Rock beats scissors, you lose")
    elif user_selection == "paper":
        if computer_selection == "rock":
            print("\n paper covers rock, you win")
        else:
            print("\n scissor cuts paper, you lose")

print(playGame())

