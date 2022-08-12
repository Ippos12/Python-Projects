user_name = input("Hey! What's your name!\n")
#variables unrelated to the actual game can just be random, e.g. elole
elole = input("Hi " + user_name + "!" + " Let's play some hangman if you're up for it?\n")
print("Amazing! Let's play!")
rules = input("So, let me explain how this works. You have 9 lives, and you have to guess a letter of a word that the computer randomly generates. If you guess wromg, you lose a life! Got it?\n")
print("Great! Let's begin!")

from random import choice
from re import L

possibleWords = ['hallowed', 'paste', 'moldy', 'harass', 'table', 'mindless', 'nation', 'divide', 'expert', 'acoustics', 'act', 'scarf', 'division', 'burst', 'tail', 'occur', 'recondite', 'servant', 'daffy', 'switch', 'work', 'back', 'neat', 'flowers', 'oven', 'abnormal', 'health', 'chance', 'tax', 'humdrum']
letters = list("abcdefghijkllmnopqrstuvqxyz")

while True:

    lives = 9
    answer = choice(possibleWords)
    answerList = list(answer)
    progress = list("_" * len(answer))
    guessedLetters = ""

    while True: 
        
        if lives == 1: print("You only have 1 life left. No pressure!")
        else: print("You have " + str(lives) +  " lives remaining.")

        print(progress)
        print(f"Previously guessed letters: {guessedLetters}")

        while True:

            guess = input("Input a guess.\n")
            if guess in letters: break
            elif guess in guessedLetters:
                 print("You already guessed that! Guess a different letter!")
            else: print("That's not a letter!")
        
        guessedLetters += guess
        instancesOfGuess = 0
        for i in answerList:
            if guess == i:
                listIndex = answerList.index(i)
                progress[listIndex] = guess
                instancesOfGuess += 1

        if instancesOfGuess > 1: print(f"The letter {guess} appears {instancesOfGuess} times!")
        elif instancesOfGuess == 1: print(f"The letter {guess} appears {instancesOfGuess} times")
        else:
            print(f"The letter {guess} does not appear. You lost a life D:.")
            lives -= 1
        
        if progress == answerList:
            print(f"You won + {user_name} + ! The word was {answer}.")
            break
        elif lives == 0:
            print("You ran out lives " + user_name + "!" +  " The word was " + answer + "!")
            break
    
    replay = input("Type 'e' to quit, type anything else to play again.\n")
    if replay == "e":
        break


