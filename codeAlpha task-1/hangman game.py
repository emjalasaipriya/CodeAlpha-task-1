import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print(" Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses:

    # Display the word with blanks
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print(" Congratulations! You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Guess a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print(" Correct guess!")
    else:
        wrong_guesses += 1
        print(" Wrong guess!")

else:
    print("\n Game Over!")
    print("The word was:", word)