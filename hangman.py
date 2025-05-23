import random

# Dictionary with words and their hints
word_hint_pairs = {
    'lion': 'animal',
    'tiger': 'animal',
    'elephant': 'animal',
    'apple': 'fruit',
    'banana': 'fruit',
    'grapes': 'fruit',
    'python': 'programming language',
    'java': 'programming language',
    'earth': 'planet',
    'venus': 'planet'
}

# Randomly choose a word and its hint
word, hint = random.choice(list(word_hint_pairs.items()))
word_letters = set(word)
guessed_letters = set()
wrong_guesses = 0
max_wrong = 6

hangman_stages = [
    '''
     -----
     |   |
         |
         |
         |
        ===''',
    '''
     -----
     |   |
     O   |
         |
         |
        ===''',
    '''
     -----
     |   |
     O   |
     |   |
         |
        ===''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
        ===''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
        ===''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
        ===''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
        ==='''
]

print("Welcome to Hangman!")
print(f"Hint: This word is a type of '{hint}'")

# Game loop
while wrong_guesses < max_wrong and word_letters:
    print(hangman_stages[wrong_guesses])
    current_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: ", ' '.join(current_word))
    print("Guessed letters:", ' '.join(sorted(guessed_letters)))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess.")

# End game message
if not word_letters:
    print("Congratulations! You guessed the word:", word)
else:
    print(hangman_stages[wrong_guesses])
    print("Game over. The word was:", word)