#Guessing game v2: Adding the Lives System and Higher or Lower
import random
answer = 0
guess = 11
lives = 3
#Ask the user their name.
str_name = input("Welcome! Please enter your name: ").strip().title()
#Create Random Number Generator.
answer = random.randrange(1, 10)
#Allow user to start guessing.
print("Okay, your task is to guess a number from 1-10. Good luck!")
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
