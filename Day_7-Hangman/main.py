import random
from replit import clear
from hangman_art import logo, drawing, hangman, winner
from hangman_words import word_list

print(logo)
print(
    "\nWelcome to the game of hangman! Guess the right word and save this man. Guess the wrong word and he will be closer to being hanged !")
chosen_word = random.choice(word_list)

end_of_game = False
lives = 0
word_length = len(chosen_word)

print(f"\n\npsstt, the word is: {chosen_word}")
all_guesses = []
display = []
for blank in chosen_word:
    display.append("_")
print(" ".join(display))

while end_of_game is False:

    guess = input("\nGuess a letter: ")

    clear()

    if guess in display:
        print(f"\nYou have already guessed the letter '{guess}'. Choose another letter !")

    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = guess

    if guess not in chosen_word:
        lives += 1
        if lives > 0:
            print(f"\nThe letter {guess} is not in the word. You lose a life.")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("\nYou win.")
        print(winner)

    if lives >= 6:
        end_of_game = True
        print("\nYou lose.")
        print("\n", hangman)

    if end_of_game != True and lives != 6:
        print(drawing[lives])