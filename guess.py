"""
guess the number picked by computer
"""
import random

def computer_guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"guess a number between 0 and {x}: "))
        if guess < random_number:
            print("Sorry, too low")
        elif guess > random_number:
            print("sorry, too high")
    
    print(f'you guessed the right number {random_number} correctly.')

computer_guess(9)