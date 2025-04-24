import random
import hangman_words 
from hangman_arts import logo,stages
from os import system

print(logo)

chosen_word = random.choice(hangman_words.word_list)
print("The chosen word is ", chosen_word )


display = []
for _ in chosen_word:
    display += "_"
lives = 6
end_of_game = False    
while not end_of_game:
    system('cls')
    guess = input("Guess the letter: ").lower()
    
    if guess in display:
        print(f"You already guessed {guess} letter")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not inn world you lose a life")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    if '_' not in display:
        end_of_game = True
        print('you win')
    
