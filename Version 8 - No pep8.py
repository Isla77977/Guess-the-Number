# Guessing game v8: Adding a scoreboard, tidying up code. 
# Maybe follow pep8 to do indents of a multiple of 4. I feel like it would be a bit too spaced out and figuring out what parts of code go where would be confusing.
# Author: Isla Adrian
# Date Started: 3/5/22
# DATES ARE NOT 100% ACCURATE - MOST ARE FROM THE DATE THEY WERE MOVED INTO A DIFFERENT FILE FOR ME TO WORK ON THE SAME MAIN. This one is though.

# Notes to self:
# It is unethical to use copywrited code.

# Allows these variables to be brought into definitions.

scorecount = 0
answer = 0
guess = 11
difficulty = 'N/A'
lives = 31415926535897932384626433832795028841971693993751058209749445923078164
str_name = 'N/A'
import time
import os
import random

# Adds code that will allow for console clearing.
def clear_console():
  clear = 'clear'
  os.system(clear)


# Creates the answer, using ranges to give a fair number whether the difficulty is easy, medium, or hard.
def randomdef(answer):
  answer = 0
  if difficulty == 'easy':
    answer = random.randrange(1, 10)
  elif difficulty == 'medium':
    answer = random.randrange(1, 50)
  elif difficulty == 'hard':
    answer = random.randrange(1, 100)
  return answer

# Creates the lives the user will have depending on whether the difficulty is easy, medium, or hard.
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
# Includes Error Catching for anything smaller than 2 letters, nothing at all, and special characters/numbers, making them invalid.
  print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
  str_name = input("Welcome! Please enter your name: \n").strip().title()
  print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
  while True:
    if str_name == '' or len(str_name) < 2 or str_name.replace(' ', '').isalpha() == False:
      print('')
      print("ERROR - Please try again.")
      time.sleep(1)
      clear_console()
      print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
      str_name = input("Welcome! Please enter your name: \n").strip().title()
      print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    else:
      time.sleep(0.7)
      clear_console()
      list_name.append(str_name)
      str_name = list_name[0]
      return str_name
      break

# The patterns with '+=+=+=+=' act as seperators for different sentences/segments of the game. 
# Makes it so all the code isn't just writing and actually includes some sort of imagery (in a way).

# Definition that introduces the player to the game properly. Allows them to pick a difficulty.
def introduction(difficulty, str_name):
  print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
  print("The game you will be playing is a Number Guessing Game. Your task is to guess the correct \nnumber. ")
  print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
  print("Depending on what difficulty you choose, the game may be easier or harder.")
  print("You must now pick a difficulty: |:| Easy, Medium, or Hard. |:|")
  difficulty = input('').strip().lower()
  while True:
    if difficulty == 'easy':
      clear_console()
      print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
      print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
      print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
      time.sleep(1.5)
      clear_console()
      return(difficulty)
      break
    elif difficulty == 'medium':
      clear_console()
      print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
      print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
      print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
      time.sleep(1.5)
      clear_console()
      return(difficulty)
      break
    elif difficulty == 'hard':
      clear_console()
      print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
      print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
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
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("Your final score was {}.".format(scorecount))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        time.sleep(2)
        clear_console()
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("Your final score was {}.".format(scorecount))
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        time.sleep(2)
        clear_console()
        break
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break
# Gives a hint as to whether the answer is higher or lower than the users guess.
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
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
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("Your final score was {}.".format(scorecount))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        time.sleep(2)
        break
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        time.sleep(2)
        clear_console()
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("Your final score was {}.".format(scorecount))
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        time.sleep(2)
        clear_console()
        break
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break
# Gives a hint as to whether the answer is higher or lower than the users guess.
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
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
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("Your final score was {}.".format(scorecount))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        time.sleep(2)
        clear_console()
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("Your final score was {}.".format(scorecount))
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        time.sleep(2)
        clear_console()
        break
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break
# Gives a hint as to whether the answer is higher or lower than the users guess.
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




# All the definitions that keep the game running. The 'while True' allows for the play-again code to work properly.
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
  print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
  play_again = input("{}, would you like to play again? Please answer with 'Yes' or 'No': ".format(str_name)).strip().lower()
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
      print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
      print("Pick a difficulty: |:| Easy, Medium, or Hard. |:|")
      difficulty = input('').strip().lower()
      time.sleep(1)
      clear_console()
      break
# Error catching in case someone decides to type anything other than 'yes' or 'no'.
    else:
      time.sleep(0.7)
      clear_console()
      print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
      print("ERROR - Please enter 'Yes' or 'No'. ")
      print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
      time.sleep(1)
      clear_console()
      print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
      play_again = input("Would you like to play again? Answer with 'Yes' or 'No': ".format(str_name)).strip().lower()
      print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
      if play_again != 'yes' and play_again != 'no':
        time.sleep(0.7)
        clear_console()
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("ERROR - Please enter 'Yes' or 'No'. ")
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        time.sleep(1)
        clear_console()
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        play_again = input("Would you like to play again? Answer with 'Yes' or 'No': ").strip().lower()
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
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
# - End Score (points)

