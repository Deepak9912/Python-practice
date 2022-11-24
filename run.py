import random
import string

random_word = ["speak", "food", "education", "phone", "water", "computer"]

def get_word(random_word):
    word = random.choice(random_word)

    while "-" in word or " " in word:
        word = random.choice(random_word)
    return word.upper()

def game():
    word = get_word(random_word)
    word_letters = set(word) # to get random letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters already guessed


    while len(word_letters) > 0:
        print('you have used the letters ', ' '.join(used_letters))

        # to show the current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_input = input("please type a letter: ").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        elif user_input in used_letters:
            print("you have already guessed that letter")
        else:
            print("Not a valid input")

if __name__ == '__main__':
    game()