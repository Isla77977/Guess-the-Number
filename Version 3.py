#A simpler version to help break down problems (possibly). Only option is easy, doesn't include error catching, definitions, or anything else of the sort.
import random
lives = 3
guess = 3948
answer = random.randint(1,10)

difficulty = input("What difficulty would you like?\n")
while difficulty != 'easy':
  difficulty = input("What difficulty would you like?\n")
while difficulty == 'easy':
  print("Your task is to guess a number from 1-10. Good luck!")
  while guess != answer:
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