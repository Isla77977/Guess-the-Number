#Guessing game v3: Adding difficulties, definitions and mini error catching as I go along.
#Author: Isla Adrian
#Date Started: 5/4/22
#DATES ARE NOT 100% ACCURATE - MOST ARE FROM THE DATE THEY WERE MOVED INTO A DIFFERENT FILE FOR ME TO WORK ON THE SAME MAIN.

answer = 0
guess = 11
difficulty = 'N/A'
lives = 3948
str_name = 'N/A'
import random


str_name = input("Welcome! Please enter your name: \n").strip().title()
print("The game you will be playing is a guessing game. Your objective is to guess the number.")
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
if difficulty == 'easy':
  answer = random.randrange(1, 10)
elif difficulty == 'medium':
  answer = random.randrange(1, 50)
elif difficulty == 'hard':
  answer = random.randrange(1, 100)


if difficulty == 'easy':
  lives = 4
elif difficulty == 'medium':
  lives = 5
elif difficulty == 'hard':
  lives = 6


#Allow user to start guessing.
if difficulty == 'easy':
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
elif difficulty == 'medium':
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
elif difficulty == 'hard':
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





#Things to add:
# -Lives system ✔
# -Play again
# -Error catching 
# -A way to clear past guesses (while still keeping guess list)
# -Guesses being displayed
# -Different difficulties
# -Add higher or lower 
# -Add definitions 
# -End Score (points)



#CHECK WITH PEP8 - ADD RETURNS