# Guessing game v6: Displaying previous guesses, clearing console.
#It is unethical to use copywrited code.
#Allows these variables to be brought into definitions.
answer = 0
guess = 11
difficulty = 'N/A'
lives = 314159265358979323846264338327950288419716939937510
str_name = 'N/A'
import time

#Adds code that will allow for console clearing.
def clear_console():
  import os
  clear = 'clear'
  os.system(clear)

#Definition that asks for the user's name.
def username(str_name):
  list_name = []
# Ask the user their name. Includes Error Catching for anything smaller than 2 letters, nothing at all, and special characters/numbers are invalid.
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



#Definition that introduces the player to the game properly. Allows them to pick a difficulty.
def introduction(difficulty, str_name):
# Add difficulties
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

#Creates the answer, that depending on whether the difficulty is easy, medium, or hard.
def randomdef(answer):
  import random
  answer = 0
  if difficulty == 'easy':
    answer = random.randrange(1, 10)
  elif difficulty == 'medium':
    answer = random.randrange(1, 50)
  elif difficulty == 'hard':
    answer = random.randrange(1, 100)
  return answer

#Creates the lives the user will have depending on whether the difficulty is easy, medium, or hard.
def lifecount():
  lives = 100
  if difficulty == 'easy':
    lives = 4
  elif difficulty == 'medium':
    lives = 5
  elif difficulty == 'hard':
    lives = 6
  return(lives)

  
#Definition that allows the 'easy' difficulty to be played.
def easy_difficulty(guess, answer, lives, str_name):
  guess_list = []
  print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
  print("Your task is to guess a number from 1-10. Good luck!")
  print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
  while guess != answer:
    try:
      guess = int(input("Guess: "))
      guess_list.append(guess)
# If they get it right end game, if they get it wrong continue game.
      if guess == answer:
        print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        break
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break
# Gives a hint as to whether the answer is higher or lower than the users guess.
      if guess < answer:
        print("The number is higher than {}.".format(guess))
        time.sleep(2)
        clear_console()
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("{} guesses remaining.".format(lives))
        print("Previous guesses:")
        print(guess_list)
        print("The number is higher than {}.".format(guess))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
      elif guess > answer:
        print("The number is smaller than {}".format(guess))
        time.sleep(2)
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

      
#Definition that allows the 'medium' difficulty to be played.
def medium_difficulty(guess, answer, lives, str_name):
  guess_list = []
  print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
  print("Your task is to guess a number from 1-50. Good luck!")
  print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
  while guess != answer:
    try:
      guess = int(input("Guess: "))
      guess_list.append(guess)
# If they get it right end game, if they get it wrong continue game.
      if guess == answer:
        print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        break
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break
# Gives a hint as to whether the answer is higher or lower than the users guess.
      if guess < answer:
        print("The number is higher than {}.".format(guess))
        time.sleep(2)
        clear_console()
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("{} guesses remaining.".format(lives))
        print("Previous guesses:")
        print(guess_list)
        print("The number is higher than {}.".format(guess))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
      elif guess > answer:
        print("The number is smaller than {}".format(guess))
        time.sleep(2)
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

      
#Definition that allows the 'hard' difficulty to be played.
def hard_difficulty(guess, answer, lives, str_name):
  guess_list = []
  print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
  print("Your task is to guess a number from 1-100. Good luck!")
  print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
  while guess != answer:
    try:
      guess = int(input("Guess: "))
      guess_list.append(guess)
# If they get it right end game, if they get it wrong continue game.
      if guess == answer:
        print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
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
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        break
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break
# Gives a hint as to whether the answer is higher or lower than the users guess.
      if guess < answer:
        print("The number is higher than {}.".format(guess))
        time.sleep(2)
        clear_console()
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        print("{} guesses remaining.".format(lives))
        print("Previous guesses:")
        print(guess_list)
        print("The number is higher than {}.".format(guess))
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
      elif guess > answer:
        print("The number is smaller than {}".format(guess))
        time.sleep(2)
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


clear_console()
str_name = username(str_name)
difficulty = introduction(difficulty, str_name)
lives = lifecount()
answer = randomdef(answer)
if difficulty == 'easy':
  easy_difficulty(guess, answer, lives, str_name)
elif difficulty == 'medium':
  medium_difficulty(guess, answer, lives, str_name)
elif difficulty == 'hard':
  hard_difficulty(guess, answer, lives, str_name)


# Things to add:
# - Lives system ✔
# - Play again
# - Error catching ✔
# - A way to clear past guesses (while still keeping guess list) ✔
# - Guesses being displayed ✔
# - Different difficulties ✔
# - Add higher or lower ✔
# - Add definitions ✔
# - End Score (points)

