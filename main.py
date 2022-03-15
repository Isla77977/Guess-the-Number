#Guessing game v1:
import random
answer = 0
guess = 11
#Ask the user their name.
str_name = input("Welcome! Please enter your name: ")
#Create Random Number Generator.
answer = random.randrange(0, 10)
#Allow user to start guessing.
print("Okay, your task is to guess a number from 0-10. Good luck!")
while guess != answer:
  guess = int(input("Guess: "))
  #If they get it right end game, if they get it wrong continue game.
  if guess == answer:
    print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
    break
  else:
    print("INCORRECT")
