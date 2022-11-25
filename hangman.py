import random
import string

words = ["office", "glass", "phone", "wire"]

def get_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hanman():
    word = get_word(words)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    lives  = 6

    while len(word_letters) > 0 and lives > 0:

        print(f'you have {lives} lives left and guessed letters ', ' '.join(used_letters))

        # to show the current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word ', ' '.join(word_list))

        user_input = input("Please type a letter: ").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
                print('')
            else:
                lives = lives-1
                print(f'your letter {user_input} is not in word')
        elif user_input in used_letters:
            print("you already guessed it")
        else:
            print("invalid input")

    if lives == 0:
        print(f"you lose, correct word is {word}")
    else:
        print("you guessed the word right")

if __name__ == '__main__':
    hanman()