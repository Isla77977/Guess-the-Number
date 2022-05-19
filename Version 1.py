
#Guessing game v1:
#Author: Isla Adrian
#Date Started: 15/3/22
#DATES ARE NOT 100% ACCURATE - MOST ARE FROM THE DATE THEY WERE MOVED INTO A DIFFERENT FILE FOR ME TO WORK ON THE SAME MAIN.

#Import random creates a randomizer that will give a number when it's used right.
import random
#These make it so the game runs since they're different (refer to line 15-20)
answer = 0
guess = 11
#Asks the user their name and stores it in a variable.
str_name = input("Welcome! Please enter your name: ")
#Creates Random Number Generator using the 'random' that was imported earlier.
answer = random.randrange(0, 10)
#Allows user to guess as long as their guess is not the same as the answer.
print("Okay, your task is to guess a number from 0-10. Good luck!")
while guess != answer:
  guess = int(input("Guess: "))
  #If they get it right end game. If they get it wrong, continue game.
  if guess == answer:
    print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
    break
  else:
    print("INCORRECT")

#No error catching, difficulties, lives.