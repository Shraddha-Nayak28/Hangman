# 🕹️ Hangman Game (with Hints)

A terminal-based Hangman game written in Python. This version gives you a helpful hint (like a category) before you start guessing the word!

## 🚀 Features
- Random word selection from predefined word-hint pairs.
- User-friendly text interface.
- Displays a visual hangman as you make wrong guesses.
- Word categories provided as hints (e.g., "animal", "fruit", "programming language").

## 🧰 Requirements
- Python 3.x
No external packages are required.

## ▶️ How to Run
Just run the Python file in your terminal or any code editor that supports Python.

## 🧠How it works
The game randomly picks a word and its associated hint (like "fruit" or "planet"). You'll see blanks for each letter, and your goal is to figure out the word before the hangman is fully drawn.
If you guess a correct letter, it shows up in the word.
If you guess wrong, the hangman starts to appear and you only get 6 chances!

## ✏️ Customizing the Words
You can easily modify the word list by editing the dictionary in hangman.py. Just add new words and their respective categories like this:
word_hint_pairs = {
    'banana': 'fruit',
    'venus': 'planet',
    'java': 'programming language'
}
Feel free to make it your own!

## 🙌 Final Note
This is a fun little project to brush up on Python basics like loops, conditionals, and dictionaries. Great for beginners or anyone looking to kill a few minutes in the terminal.
Enjoy the game, and try not to get hanged! 😄
