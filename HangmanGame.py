import random

# List of predefined words
words = ["python", "coding", "computer", "developer", "program"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
attempts = 6

print("================================")
print("      HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.\n")

while attempts > 0:

    # Display guessed letters and underscores
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet.")
        continue

    # Check duplicate guess
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Remaining Attempts:", attempts)

# Game over condition
if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)