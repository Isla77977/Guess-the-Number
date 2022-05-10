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

int_scorecount = 0
int_answer = 0
int_guess = 11
str_mode = 'N/A'
int_lives = 314159265358979323846264338327950288419716939937510
str_name = 'N/A'


# Adds code that will allow for console clearing.
def clear_console():
    clear = 'clear'
    os.system(clear)


# Creates the answer.
def randomdef(int_answer):
    int_answer = 0
    if str_mode == 'easy':
        int_answer = random.randrange(1, 10)
    elif str_mode == 'medium':
        int_answer = random.randrange(1, 50)
    elif str_mode == 'hard':
        int_answer = random.randrange(1, 100)
    return int_answer


# Creates the lives.
def lifecount():
    int_lives = 100
    if str_mode == 'easy':
        int_lives = 4
    elif str_mode == 'medium':
        int_lives = 5
    elif str_mode == 'hard':
        int_lives = 6
    return(int_lives)


def scoreboard(int_scorecount):
    int_scorecount == 0
    return int_scorecount


# Definition that asks for the user's name.
def username(str_name):
    list_name = []
# Includes Error Catching.
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Welcome!")
    str_name = input("Please enter your name: \n").strip().title()
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
def introduction(str_mode, str_name):
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("The game you will be playing is a Number Guessing Game.")
    print("Your task is to guess the correct number. ")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("The difficulty will decide how easy or hard the game is.")
    print("You must now pick a difficulty: |:| Easy, Medium, or Hard. |:|")
    str_mode = input('').strip().lower()
    while True:
        if str_mode == 'easy':
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            print("You picked {}.".format(str_mode.title()))
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            time.sleep(1.5)
            clear_console()
            return(str_mode)
            break
        elif str_mode == 'medium':
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            print("You picked {}.".format(str_mode.title()))
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            time.sleep(1.5)
            clear_console()
            return(str_mode)
            break
        elif str_mode == 'hard':
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            print("You picked {}.".format(str_mode.title()))
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            time.sleep(1.5)
            clear_console()
            return(str_mode)
            break
        else:
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("ERROR - Please type in a valid difficulty")
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            time.sleep(1)
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
            print("Pick a difficulty: |:| Easy, Medium, or Hard. |:|")
            str_mode = input('').strip().lower()


# Definition that allows the 'easy' difficulty to be played.
def easy_mode(int_guess, int_answer, int_lives, str_name, int_scorecount):
    # Guess list allows any numbers the user has typed to be shown.
    guess_list = []
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    print("Your task is to guess a number from 1-10. Good luck!")
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    while int_guess != int_answer:
        try:
            int_guess = int(input("Guess: "))
            guess_list.append(int_guess)
# If they get it right end game, if they get it wrong, it continues the game.
            if int_guess == int_answer:
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Congratulations, {}. You got it!".format(str_name))
                print("It was {}.".format(int_answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                if int_lives == 4:
                    int_scorecount += 10000
                elif int_lives == 3:
                    int_scorecount += 7000
                elif int_lives == 2:
                    int_scorecount += 5500
                elif int_lives == 1:
                    int_scorecount += 3000
                time.sleep(1.5)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(int_scorecount))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(2)
                break
            while True:
                if int_guess > 10 or int_guess < 0:
                    int_scorecount -= 500
                    guess_list.pop()
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("ERROR - Please try again.")
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    time.sleep(1)
                    clear_console()
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    if int_lives > 1:
                        print("{} guesses remaining.".format(int_lives))
                    else:
                        print("{} guess remaining.".format(int_lives))
                    print("Previous guesses:")
                    print(guess_list)
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    int_guess = int(input("Guess: "))
                    int_guess
                    guess_list.append(int_guess)
                else:
                    break
            if int_guess != int_answer:
                print('+=+=+=+=+=+=+=+')
                print("INCORRECT")
                print('+=+=+=+=+=+=+=+')
                int_lives -= 1
            if int_lives <= 0:
                time.sleep(1)
                clear_console()
# If you run out of lives, you lose and the game ends.
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("I'm sorry, you have run out of lives.")
                print("The correct number was {}".format(int_answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(2)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(int_scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                clear_console()
                break

            if int_guess < int_answer:
                # Gives hint as to whether the answer is higher or lower.
                int_scorecount += 1000
                print("The number is higher than {}.".format(int_guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                if int_lives > 1:
                    print("{} guesses remaining.".format(int_lives))
                else:
                    print("{} guess remaining.".format(int_lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is higher than {}.".format(int_guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif int_guess > int_answer:
                int_scorecount += 1000
                print("The number is smaller than {}".format(int_guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                if int_lives > 1:
                    print("{} guesses remaining.".format(int_lives))
                else:
                    print("{} guess remaining.".format(int_lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is smaller than {}.".format(int_guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif int_guess == int_answer:
                print(" ")
        except ValueError:
            int_scorecount -= 500
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("ERROR - Please try again.")
            time.sleep(1)
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            if int_lives > 1:
                print("{} guesses remaining.".format(int_lives))
            else:
                print("{} guess remaining.".format(int_lives))
            print("Previous guesses:")
            print(guess_list)
            print('')
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')


# Definition that allows the 'medium' difficulty to be played.
def medium_mode(int_guess, int_answer, int_lives, str_name, int_scorecount):
    guess_list = []
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    print("Your task is to guess a number from 1-50. Good luck!")
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    while int_guess != int_answer:
        try:
            int_guess = int(input("Guess: "))
            guess_list.append(int_guess)
# If they get it right end game, if they get it wrong, it continues the game.
            if int_guess == int_answer:
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Congratulations, {}. You got it!".format(str_name))
                print("It was {}.".format(int_answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                if int_lives == 5:
                    int_scorecount += 12000
                elif int_lives == 4:
                    int_scorecount += 10000
                elif int_lives == 3:
                    int_scorecount += 7000
                elif int_lives == 2:
                    int_scorecount += 5500
                elif int_lives == 1:
                    int_scorecount += 3000
                time.sleep(1.5)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(int_scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                break
            while True:
                if int_guess > 50 or int_guess < 0:
                    int_scorecount -= 500
                    guess_list.pop()
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("ERROR - Please try again.")
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    time.sleep(1)
                    clear_console()
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    if int_lives > 1:
                        print("{} guesses remaining.".format(int_lives))
                    else:
                        print("{} guess remaining.".format(int_lives))
                    print("Previous guesses:")
                    print(guess_list)
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    int_guess = int(input("Guess: "))
                    int_guess
                    guess_list.append(int_guess)
                else:
                    break
            if int_guess != int_answer:
                print('+=+=+=+=+=+=+=+')
            print("INCORRECT")
            print('+=+=+=+=+=+=+=+')
            int_lives -= 1
            if int_lives <= 0:
                time.sleep(1)
                clear_console()
# If you run out of lives, you lose and the game ends.
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("I'm sorry, you have run out of lives.")
                print("The correct number was {}".format(int_answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(2)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(int_scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                clear_console()
                break
# Gives hint as to whether the answer is higher or lower than the users guess.
            if int_guess < int_answer:
                int_scorecount += 1000
                print("The number is higher than {}.".format(int_guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                if int_lives > 1:
                    print("{} guesses remaining.".format(int_lives))
                else:
                    print("{} guess remaining.".format(int_lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is higher than {}.".format(int_guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif int_guess > int_answer:
                int_scorecount += 1000
                print("The number is smaller than {}".format(int_guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                if int_lives > 1:
                    print("{} guesses remaining.".format(int_lives))
                else:
                    print("{} guess remaining.".format(int_lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is smaller than {}.".format(int_guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif int_guess == int_answer:
                print(" ")
        except ValueError:
            int_scorecount -= 500
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("ERROR - Please try again.")
            time.sleep(1)
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            if int_lives > 1:
                print("{} guesses remaining.".format(int_lives))
            else:
                print("{} guess remaining.".format(int_lives))
            print("Previous guesses:")
            print(guess_list)
            print('')
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')


# Definition that allows the 'hard' difficulty to be played.
def hard_mode(int_guess, int_answer, int_lives, str_name, int_scorecount):
    guess_list = []
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    print("Your task is to guess a number from 1-100. Good luck!")
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    while int_guess != int_answer:
        try:
            int_guess = int(input("Guess: "))
            guess_list.append(int_guess)
# If they get it right end game, if they get it wrong, it continues the game.
            if int_guess == int_answer:
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Congratulations, {}. You got it!".format(str_name))
                print("It was {}.".format(int_answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                if int_lives == 6:
                    int_scorecount += 15000
                elif int_lives == 5:
                    int_scorecount += 12000
                elif int_lives == 4:
                    int_scorecount += 10000
                elif int_lives == 3:
                    int_scorecount += 7000
                elif int_lives == 2:
                    int_scorecount += 5500
                elif int_lives == 1:
                    int_scorecount += 3000
                time.sleep(1.5)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(int_scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                break
            while True:
                if int_guess > 100 or int_guess < 0:
                    int_scorecount -= 500
                    guess_list.pop()
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("ERROR - Please try again.")
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    time.sleep(1)
                    clear_console()
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    if int_lives > 1:
                        print("{} guesses remaining.".format(int_lives))
                    else:
                        print("{} guess remaining.".format(int_lives))
                    print("Previous guesses:")
                    print(guess_list)
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    int_guess = int(input("Guess: "))
                    int_guess
                    guess_list.append(int_guess)
                else:
                    break
            if int_guess != int_answer:
                print('+=+=+=+=+=+=+=+')
                print("INCORRECT")
                print('+=+=+=+=+=+=+=+')
                int_lives -= 1
            if int_lives <= 0:
                time.sleep(1)
                clear_console()
# If you run out of lives, you lose and the game ends.
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                print("I'm sorry, you have run out of lives.")
                print("The correct number was {}".format(int_answer))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(2)
                clear_console()
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(int_scorecount))
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                time.sleep(2)
                clear_console()
                break

# Gives hint as to whether the answer is higher or lower than the users guess.
            if int_guess < int_answer:
                int_scorecount += 1000
                print("The number is higher than {}.".format(int_guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                if int_lives > 1:
                    print("{} guesses remaining.".format(int_lives))
                else:
                    print("{} guess remaining.".format(int_lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is higher than {}.".format(int_guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif int_guess > int_answer:
                int_scorecount += 1000
                print("The number is smaller than {}".format(int_guess))
                time.sleep(1)
                clear_console()
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                if int_lives > 1:
                    print("{} guesses remaining.".format(int_lives))
                else:
                    print("{} guess remaining.".format(int_lives))
                print("Previous guesses:")
                print(guess_list)
                print("The number is smaller than {}.".format(int_guess))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            elif int_guess == int_answer:
                print(" ")
        except ValueError:
            int_scorecount -= 500
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("ERROR - Please try again.")
            time.sleep(1)
            clear_console()
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            if int_lives > 1:
                print("{} guesses remaining.".format(int_lives))
            else:
                print("{} guess remaining.".format(int_lives))
            print("Previous guesses:")
            print(guess_list)
            print('')
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')


# All the definitions that keep the game running.
# The 'while True' allows for the play-again code to work properly.
clear_console()
str_name = username(str_name)
str_mode = introduction(str_mode, str_name)
while True:
    int_lives = lifecount()
    int_answer = randomdef(int_answer)
    int_scorecount = scoreboard(int_scorecount)
    if str_mode == 'easy':
        easy_mode(int_guess, int_answer, int_lives, str_name, int_scorecount)
        time.sleep(1)
        clear_console()
    elif str_mode == 'medium':
        medium_mode(int_guess, int_answer, int_lives, str_name, int_scorecount)
        time.sleep(1)
        clear_console()
    elif str_mode == 'hard':
        hard_mode(int_guess, int_answer, int_lives, str_name, int_scorecount)
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
            str_mode = input('').strip().lower()
            time.sleep(1)
            clear_console()
            break
# Error catching.
        else:
            while play_again != 'yes' and play_again != 'no':
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
                if play_again == 'yes' or play_again == 'no':
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
