#v2 of Guessing Game
#Author: Isla Adrian
#Date Started: 15/3/22
#DATES ARE NOT 100% ACCURATE - MOST ARE FROM THE DATE THEY WERE MOVED INTO A DIFFERENT FILE FOR ME TO WORK ON THE SAME MAIN.

#A simpler version to help break down problems (possibly). Only option is easy, doesn't include error catching, definitions, or anything else of the sort.
import random
lives = 3
guess = 3948
answer = random.randint(1,10)

while True:
  print("Your task is to guess a number from 1-10 with 3 lives. Good luck!")
  for i in range(3):
    guess = int(input("Guess: "))
#If they get it right end game, if they get it wrong continue game.
    if guess == answer:
      print("Congratulations, you guessed the correct number! It was {}.".format(answer))
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
  if lives <= 0 or guess == answer:
    break