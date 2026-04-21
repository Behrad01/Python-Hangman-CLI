import random

# defining a list of words
hangman_words = [
    "APPLE", "BANANA", "BRAIN", "CLOUD", "CYCLONE", "DIAMOND", "DREAM", "EAGLE", 
    "ELEPHANT", "FALCON", "FLAME", "GRASS", "GUITAR", "HAMMER", "HONEY", "ICICLE", 
    "IGUANA", "JACKET", "JOKER", "KANGAROO", "KITE", "LEMON", "LIGHTER", "MONSTER", 
    "MOON", "NECKLACE", "NIGHT", "OCEAN", "OCTOPUS", "PEARL", "PUMPKIN", "QUEEN", 
    "QUARTZ", "RAINBOW", "RIVER", "SILENCE", "STARS", "TIGER", "TORNADO", "UMBRA", 
    "UNICORN", "VIOLIN", "VOLCANO", "WHALE", "WINDOW", "XEROX", "XYLOPHONE", "YACHT", 
    "YELLOW", "ZEBRA"
]

# defining the main function
def main():
    random_word = random.choice(hangman_words)   # generating random word
    random_word_length = len(random_word)   # calculating random word length
    lives = 6    # defining number of lives
    guessed_letters = []   # defining an empty list of guessed letters

    # storing each letter of the random word in a list
    random_word_letters = []
    for letter in random_word:
        random_word_letters.append(letter)

    listed_word = ['_'] * random_word_length   # defining a list formatted value of word

    print(('-' * 10) + ' Hangman ' + ('-' * 10))   # part of game CLI
    # starting game
    while True:
        word = ''.join(listed_word)   # variable for current word

        # printing current game information
        print(f'\nWord: {word}')
        print(f'Guessed letters: {', '.join(guessed_letters)}')
        print(f'Lives remaining: {lives}\n')

        # calculating win if random word is guessed
        if word == random_word:
            print(f'You won! The correct word was {random_word}.')
            break   # finishing the game
        
        # calculating loss if lives reaches 0
        if lives == 0:
            print(f'You lost! The correct word was {random_word}.')
            break  # finishing the game
        
        # catching user input
        user_input = input('Guess a letter: ').upper()

        # annoucing if the same letter is guessed twice
        if user_input in guessed_letters:
            print(f'You already guessed {user_input}.')
            continue
        
        # actions if guess is in random word letters
        if user_input in random_word_letters:
            print(f'\nLetter {user_input} exists!\n')

            # updating 'word' variable
            for i in range(len(random_word)):
                if user_input == random_word[i]:
                    listed_word[i] = user_input

        # actions if guess is not correct
        else:
            print(f"Letter {user_input} doesn't exist!\n")
            lives -= 1   # decreasing remaining lives
        guessed_letters.append(user_input)   # adding guessed letter to the guessed letters list

        print('-' * 29 + '\n')   # part of game CLI

# running game function
if __name__ == '__main__':
    main()
