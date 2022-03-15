#Guessing game v2: Adding difficulties and mini error catching as I go along.
import random
answer = 0
guess = 11
lives = 100
difficulty = 'N/A'
#Ask the user their name.
str_name = input("Welcome! Please enter your name: ").strip().title()
#Add difficulties
print("The game you will be playing is a Number Guessing Game. Your task is to guess the correct \nnumber. ")
print("Depending on what difficulty you choose, the game may be easier or harder.")
print("You must now pick a difficulty: Easy, Medium, or Hard.")
while difficulty != 'easy' or difficulty != 'medium' or difficulty != 'hard':
  difficulty = input("").strip().lower()
  if difficulty == 'easy':
    print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
    break
  elif difficulty == 'medium':
    print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
    break
  elif difficulty == 'hard':
    print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
    break
  else:
    print("ERROR - Please type in a valid difficulty")

#Allow user to start guessing.
if difficulty == 'easy':
  lives = 4
  answer = random.randrange(1, 10)
  print("Your task is to guess a number from 1-10. Good luck!")
  while guess != answer:
    guess = int(input("Guess: "))
#If they get it right end game, if they get it wrong continue game.
    if guess == answer:
      print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
      break
    else:
      print("INCORRECT")
      lives -= 1
    if lives <= 0:
      print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
      break
#Gives a hint as to whether the answer is higher or lower than the users guess.
    if guess < answer:
      print("The number is higher than {}.".format(guess))
    elif guess > answer:
      print("The number is smaller than {}".format(guess))
    elif guess == answer:
      print(" ")

#==========================================================================

if difficulty == 'medium':
  answer = random.randrange(1, 50)
  lives = 4
  print("Your task is to guess a number from 1-50. Good luck!")
  while guess != answer:
    guess = int(input("Guess: "))
#If they get it right end game, if they get it wrong continue game.
    if guess == answer:
      print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
      break
    else:
      print("INCORRECT")
      lives -= 1
    if lives <= 0:
      print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
      break
#Gives a hint as to whether the answer is higher or lower than the users guess.
    if guess < answer:
      print("The number is higher than {}.".format(guess))
    elif guess > answer:
      print("The number is smaller than {}".format(guess))
    elif guess == answer:
      print(" ")

#============================================================================

if difficulty == 'easy':
  answer = random.randrange(1, 100)
  lives = 6
  print("Your task is to guess a number from 1-100. Good luck!")
  while guess != answer:
    guess = int(input("Guess: "))
#If they get it right end game, if they get it wrong continue game.
    if guess == answer:
      print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
      break
    else:
      print("INCORRECT")
      lives -= 1
    if lives <= 0:
      print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
      break
#Gives a hint as to whether the answer is higher or lower than the users guess.
    if guess < answer:
      print("The number is higher than {}.".format(guess))
    elif guess > answer:
      print("The number is smaller than {}".format(guess))
    elif guess == answer:
      print(" ")

      
#Things to add:
# -Lives system ✔
# -Play again
# -Error catching
# -A way to clear past guesses (while still keeping guess list)
# -Guesses being displayed
# -Different difficulties
# -Add higher or lower ✔
# -Add definitions
    
