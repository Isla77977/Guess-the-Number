import time
import os
import random

# Guessing game v8: Adding a scoreboard, tidying up code.
# pep8 version
# Author: Isla Adrian
# Date Started: 6/5/22

# Notes to self:
# It is unethical to use copywrited code.

# Allows these variables to be brought into definitions.

scorecount = 0
answer = 0
guess = 11
difficulty = 'N/A'
lives = 31415926535897932384626433832795028841971693993751058209749445923078164
str_name = 'N/A'


# Adds code that will allow for console clearing.
def clear_console():
    clear = 'clear'
    os.system(clear)


# Creates the answer.
def randomdef(answer):
    answer = 0
    if difficulty == 'easy':
        answer = random.randrange(1, 10)
    elif difficulty == 'medium':
        answer = random.randrange(1, 50)
    elif difficulty == 'hard':
        answer = random.randrange(1, 100)
    return answer


# Creates the lives.
def lifecount():
    lives = 100
    if difficulty == 'easy':
        lives = 4
    elif difficulty == 'medium':
        lives = 5
    elif difficulty == 'hard':
        lives = 6
    return(lives)


def scoreboard(scorecount):
    scorecount == 0
    return scorecount


# Definition that asks for the user's name.
def username(str_name):
    list_name = []
# Includes Error Catching.
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    str_name = input("Welcome! Please enter your name: \n").strip().title()
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    while True:
        if str_name == '':
            print('')
            print("ERROR - Please try again.")
            time.sleep(1)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("Welcome!")
            str_name = input("Please enter your name: \n").strip().title()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        elif len(str_name) < 2:
            print('')
            print("ERROR - Please try again.")
            time.sleep(1)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("Welcome!")
            str_name = input("Please enter your name: \n").strip().title()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        elif str_name.replace(' ', '').isalpha() is False:
            print('')
            print("ERROR - Please try again.")
            time.sleep(1)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("Welcome!")
            str_name = input("Please enter your name: \n").strip().title()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        else:
            time.sleep(0.7)
            clear_console()
            list_name.append(str_name)
            str_name = list_name[0]
            return str_name
            break


# The patterns with '+=+=+=+=' act as seperators.
# Makes it so all the code isn't just writing.

# Introduces the player to the game. Lets them to pick a difficulty.
def introduction(difficulty, str_name):
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("The game you will be playing is a Number Guessing Game.")
    print("Your task is to guess the correct number. ")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("The difficulty will decide how easy or hard the game is.")
    print("You must now pick a difficulty: |:| Easy, Medium, or Hard. |:|")
    difficulty = input('').strip().lower()
    while True:
        if difficulty == 'easy':
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            print("Okay, you picked {}.".format(str_name, difficulty.title()))
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            time.sleep(1.5)
            clear_console()
            return(difficulty)
            break
        elif difficulty == 'medium':
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            print("Okay, you picked {}.".format(str_name, difficulty.title()))
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            time.sleep(1.5)
            clear_console()
            return(difficulty)
            break
        elif difficulty == 'hard':
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            print("Okay, you picked {}.".format(str_name, difficulty.title()))
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            time.sleep(1.5)
            clear_console()
            return(difficulty)
            break
        else:
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("ERROR - Please type in a valid difficulty")
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            time.sleep(1)
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            print("Pick a difficulty: |:| Easy, Medium, or Hard. |:|")
            difficulty = input('').strip().lower()


# Definition that allows the 'easy' difficulty to be played.
def easy_difficulty(guess, answer, lives, str_name, scorecount):
    # Guess list allows any numbers the user has typed to be shown.
    guess_list = []
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    print("Your task is to guess a number from 1-10. Good luck!")
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    while guess != answer:
        try:
            guess = int(input("Guess: "))
            guess_list.append(guess)
# If they get it right end game, if they get it wrong, it continues the game.
            if guess == answer:
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Congratulations, {}. You got it!".format(str_name))
                print("It was {}.".format(answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                if lives == 4:
                    scorecount += 10000
                elif lives == 3:
                    scorecount += 7000
                elif lives == 2:
                    scorecount += 5500
                elif lives == 1:
                    scorecount += 3000
                time.sleep(1.5)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(scorecount))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(2)
                break
            else:
                print('+=+=+=+=+=+=+=+')
                print("INCORRECT")
                print('+=+=+=+=+=+=+=+')
                lives -= 1
            if lives <= 0:
                time.sleep(1)
                clear_console()
# If you run out of lives, you lose and the game ends.
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("I'm sorry, you have run out of lives.")
                print("The correct number was {}".format(answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(2)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                clear_console()
                break

# Gives hint as to whether the answer is higher or lower than the users guess.
            if guess < answer:
                scorecount += 1000
                print("The number is higher than {}.".format(guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("{} guesses remaining.".format(lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is higher than {}.".format(guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif guess > answer:
                scorecount += 1000
                print("The number is smaller than {}".format(guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("{} guesses remaining.".format(lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is smaller than {}.".format(guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif guess == answer:
                print(" ")
        except ValueError:
            scorecount -= 500
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("ERROR - Please try again.")
            time.sleep(1)
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("{} guesses remaining.".format(lives))
            print("Previous guesses:")
            print(guess_list)
            print('')
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')


# Definition that allows the 'medium' difficulty to be played.
def medium_difficulty(guess, answer, lives, str_name, scorecount):
    guess_list = []
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    print("Your task is to guess a number from 1-50. Good luck!")
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    while guess != answer:
        try:
            guess = int(input("Guess: "))
            guess_list.append(guess)
# If they get it right end game, if they get it wrong, it continues the game.
            if guess == answer:
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Congratulations, {}. You got it!".format(str_name))
                print("It was {}.".format(answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                if lives == 5:
                    scorecount += 12000
                elif lives == 4:
                    scorecount += 10000
                elif lives == 3:
                    scorecount += 7000
                elif lives == 2:
                    scorecount += 5500
                elif lives == 1:
                    scorecount += 3000
                time.sleep(1.5)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                break
            else:
                print('+=+=+=+=+=+=+=+')
                print("INCORRECT")
                print('+=+=+=+=+=+=+=+')
                lives -= 1
                if lives <= 0:
                    time.sleep(1)
                    clear_console()
# If you run out of lives, you lose and the game ends.
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("I'm sorry, you have run out of lives.")
                    print("The correct number was {}".format(answer))
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    time.sleep(2)
                    clear_console()
                    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                    print("Your final score was {}.".format(scorecount))
                    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                    time.sleep(2)
                    clear_console()
                    break
# Gives hint as to whether the answer is higher or lower than the users guess.
                if guess < answer:
                    scorecount += 1000
                    print("The number is higher than {}.".format(guess))
                    time.sleep(1)
                    clear_console()
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("{} guesses remaining.".format(lives))
                    print("Previous guesses:")
                    print(guess_list)
                    print("The number is higher than {}.".format(guess))
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                elif guess > answer:
                    scorecount += 1000
                    print("The number is smaller than {}".format(guess))
                    time.sleep(1)
                    clear_console()
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("{} guesses remaining.".format(lives))
                    print("Previous guesses:")
                    print(guess_list)
                    print("The number is smaller than {}.".format(guess))
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                elif guess == answer:
                    print(" ")
        except ValueError:
            scorecount -= 500
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("ERROR - Please try again.")
        time.sleep(1)
        clear_console()
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("{} guesses remaining.".format(lives))
        print("Previous guesses:")
        print(guess_list)
        print('')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')


# Definition that allows the 'hard' difficulty to be played.
def hard_difficulty(guess, answer, lives, str_name, scorecount):
    guess_list = []
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    print("Your task is to guess a number from 1-100. Good luck!")
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    while guess != answer:
        try:
            guess = int(input("Guess: "))
            guess_list.append(guess)
# If they get it right end game, if they get it wrong, it continues the game.
            if guess == answer:
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Congratulations, {}. You got it!".format(str_name))
                print("It was {}.".format(answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                if lives == 6:
                    scorecount += 15000
                elif lives == 5:
                    scorecount += 12000
                elif lives == 4:
                    scorecount += 10000
                elif lives == 3:
                    scorecount += 7000
                elif lives == 2:
                    scorecount += 5500
                elif lives == 1:
                    scorecount += 3000
                time.sleep(1.5)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                break
            else:
                print('+=+=+=+=+=+=+=+')
                print("INCORRECT")
                print('+=+=+=+=+=+=+=+')
                lives -= 1
            if lives <= 0:
                time.sleep(1)
                clear_console()
# If you run out of lives, you lose and the game ends.
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("I'm sorry, you have run out of lives.")
                print("The correct number was {}".format(answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(2)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                clear_console()
                break

# Gives hint as to whether the answer is higher or lower than the users guess.
            if guess < answer:
                scorecount += 1000
                print("The number is higher than {}.".format(guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("{} guesses remaining.".format(lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is higher than {}.".format(guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif guess > answer:
                scorecount += 1000
                print("The number is smaller than {}".format(guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("{} guesses remaining.".format(lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is smaller than {}.".format(guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif guess == answer:
                print(" ")
        except ValueError:
            scorecount -= 500
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("ERROR - Please try again.")
            time.sleep(1)
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("{} guesses remaining.".format(lives))
            print("Previous guesses:")
            print(guess_list)
            print('')
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')


# All the definitions that keep the game running.
# The 'while True' allows for the play-again code to work properly.
clear_console()
str_name = username(str_name)
difficulty = introduction(difficulty, str_name)
while True:
    lives = lifecount()
    answer = randomdef(answer)
    scorecount = scoreboard(scorecount)
    if difficulty == 'easy':
        easy_difficulty(guess, answer, lives, str_name, scorecount)
        time.sleep(1)
        clear_console()
    elif difficulty == 'medium':
        medium_difficulty(guess, answer, lives, str_name, scorecount)
        time.sleep(1)
        clear_console()
    elif difficulty == 'hard':
        hard_difficulty(guess, answer, lives, str_name, scorecount)
        time.sleep(1)
        clear_console()
# Play-Again code.
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("{}, would you like to play again?".format(str_name))
        print("Please answer with 'Yes' or 'No'")
        play_again = input("").strip().lower()
        while True:
            if play_again == 'no':
                time.sleep(0.7)
                clear_console()
                print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("Goodbye then. Play again another time!")
                print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(1.5)
                clear_console()
                break

            elif play_again == 'yes':
                time.sleep(0.7)
                clear_console()
                print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("Alright, good luck!")
                print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(2)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Pick a difficulty: |:| Easy, Medium, or Hard. |:|")
                difficulty = input('').strip().lower()
                time.sleep(1)
                clear_console()
                break
# Error catching.
            else:
                time.sleep(0.7)
                clear_console()
                print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("ERROR - Please enter 'Yes' or 'No'. ")
                print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(1)
                clear_console()
                print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Would you like to play again?")
                print("Please answer with 'Yes' or 'No'.")
                play_again = input("").strip().lower()
                print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                if play_again != 'yes' and play_again != 'no':
                    time.sleep(0.7)
                    clear_console()
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("ERROR - Please enter 'Yes' or 'No'. ")
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    time.sleep(1)
                    clear_console()
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                    print("Would you like to play again?")
                    print("Please answer with 'Yes' or 'No'.")
                    play_again = input("").strip().lower()
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                else:
                    if play_again == 'yes':
                        time.sleep(1)
                        clear_console()
                        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                        print("Alright, good luck!")
                        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                        time.sleep(1.5)
                        clear_console()
                        break
                    else:
                        time.sleep(1)
                        clear_console()
                        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                        print("Goodbye then. Play again another time!")
                        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                        time.sleep(1.5)
                        clear_console()
                        break

        if play_again == 'no':
            break


# Things to add:
# - Lives system ✔
# - Play again ✔
# - Error catching ✔
# - A way to clear past guesses (while still keeping guess list) ✔
# - Guesses being displayed ✔
# - Different difficulties ✔
# - Add higher or lower ✔
# - Add definitions ✔
# - End Score (points) ✔
