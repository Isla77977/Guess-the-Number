# Guessing game v9: Shorten code (merge difficulties).
# Author: Isla Adrian
# Date Started: 10/5/22

# Notes to self:
# It is unethical to use copywrited code.

# Allows these variables to be brought into definitions.

import time
import os
import random
int_scorecount = 0
int_answer = 0
int_guess = 0
str_mode = 'N/A'
int_lives = 0
str_name = 'N/A'
int_text = 0
guess_list = []
list_name = []


# Adds code that will allow for console clearing.
def clear_console():
    clear = 'clear'
    os.system(clear)


# Highest number for the range (1-10, 1-50, 1-100)
def range(int_text):
    if str_mode == 'easy':
        int_textd = '10'
    elif str_mode == 'medium':
        int_textd = '50'
    elif str_mode == 'hard':
        int_textd = '100'
    int_text = int(int_textd)
    return int_text


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
            time.sleep(1)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("ERROR - Please try again.")
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            time.sleep(1.5)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            str_name = input("Please enter your name: \n").strip().title()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        elif len(str_name) <= 2:
            time.sleep(1)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("ERROR - Please try again.")
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            time.sleep(1.5)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            str_name = input("Please enter your name: \n").strip().title()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        elif str_name.replace(' ', '').isalpha() is False:
            time.sleep(1)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("ERROR - Please try again.")
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            time.sleep(1.5)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            str_name = input("Please enter your name: \n").strip().title()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        else:
            time.sleep(0.7)
            clear_console()
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("Do you confirm you want this as your name?")
            print("Please enter 'Yes' or 'No'.")
            print('')
            print("'"+ str_name +"'")
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            int_text = input("").strip().lower()
            if int_text == 'yes':
                time.sleep(0.7)
                clear_console()
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                print("Okay, you may continue.")
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                time.sleep(1)
                clear_console()
                list_name.append(str_name)
                str_name = list_name[0]
                return str_name
                break
            else:
                time.sleep(1)
                clear_console()
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                print("Alright, you may pick a new name.")
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                time.sleep(0.7)
                clear_console()
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                str_name = input("Please enter your name: \n").strip().title()
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                time.sleep(0.7)
                clear_console()


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
        if str_mode == 'easy' or str_mode == 'medium' or str_mode == 'hard':
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
def game(int_guess, int_answer, int_lives, str_name, int_scorecount, int_text):
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    print("You must guess a number from 1-{}. Good luck!".format(int_text))
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
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                print("Your final score was {}.".format(int_scorecount))
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                time.sleep(1)
                break
            while True:
                if int_guess > int_text or int_guess < 1:
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
                time.sleep(1)
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


# All the definitions that keep the game running.
# The 'while True' allows for the play-again code to work properly.
clear_console()
str_name = username(str_name)
str_mode = introduction(str_mode, str_name)

while True:
    guess_list = []
    int_text = range(int_text)
    int_lives = lifecount()
    int_answer = randomdef(int_answer)
    int_scorecount = scoreboard(int_scorecount)
    game(int_guess, int_answer, int_lives, str_name, int_scorecount, int_text)
# Play Again code.
    time.sleep(1.5)
    clear_console()
    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
    print("{}, would you like to play again?".format(str_name))
    print("Please answer with 'Yes' or 'No'")
    play_again = input("").strip().lower()
    while True:
        if play_again == 'no':
            time.sleep(0.7)
            clear_console()
            print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            print("Goodbye then. Play again another time!")
            print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            time.sleep(1)
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
            while True:
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print("Pick a difficulty: |:| Easy, Medium, or Hard. |:|")
                str_mode = input('').strip().lower()
                clear_console()
                # Seperate lines for the same code so pep8 doesn't get mad.
                if str_mode == 'easy':
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("Alright, good luck!")
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    time.sleep(2)
                    clear_console()
                    break
                elif str_mode == 'medium':
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("Alright, good luck!")
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    time.sleep(2)
                    clear_console()
                    break
                elif str_mode == 'hard':
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("Alright, good luck!")
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    time.sleep(2)
                    clear_console()
                    break
                else:
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    print("ERROR - Please enter a valid difficulty. ")
                    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
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
# All done!
