import random

def choose_word():
    # List of possible words
    words = ["python", "hangman", "programming", "developer", "keyboard"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    print("Welcome to Hangman!")
    
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    guessed_correctly = False
    
    while attempts > 0 and not guessed_correctly:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1
        
        if set(word) == guessed_letters:
            guessed_correctly = True
    
    if guessed_correctly:
        print(f"\nCongratulations! You've guessed the word: {word}")
    else:
        print(f"\nSorry, you've run out of attempts. The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()
