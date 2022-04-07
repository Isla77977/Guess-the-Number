# Guessing game v5: Trying to make the code better, may try to fix definitions again.
answer = 0
guess = 11
difficulty = 'N/A'
lives = 314159265358979323846264338327950288419716939937510
str_name = 'N/A'


def introduction(difficulty):
# Ask the user their name.
  str_name = input("Welcome! Please enter your name: \n").strip().title()
  while True:
    if str_name == '' or len(str_name) < 2 or str_name.replace(' ', '').isalpha() == False:
      print('')
      print("ERROR - Please try again:\n")
      str_name = input("Please enter your name: ")
    else:
      break
    return str_name

# Add difficulties
  print("The game you will be playing is a Number Guessing Game. Your task is to guess the correct \nnumber. ")
  print("Depending on what difficulty you choose, the game may be easier or harder.")
  print("You must now pick a difficulty: Easy, Medium, or Hard.")
  while difficulty != 'easy' or difficulty != 'medium' or difficulty != 'hard':
    difficulty = input("").strip().lower()
    if difficulty == 'easy':
      print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
      return(difficulty)
      break
    elif difficulty == 'medium':
      print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
      return(difficulty)
      break
    elif difficulty == 'hard':
      print("Okay {}, you picked {}.".format(str_name, difficulty.title()))
      return(difficulty)
      break
    else:
      print("ERROR - Please type in a valid difficulty")


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


def lifecount():
  lives = 100
  if difficulty == 'easy':
    lives = 4
  elif difficulty == 'medium':
    lives = 5
  elif difficulty == 'hard':
    lives = 6
  return(lives)




def easy_difficulty(guess, answer, lives, str_name):
  print("Your task is to guess a number from 1-10. Good luck!")
  while guess != answer:
    guess = int(input("Guess: "))
# If they get it right end game, if they get it wrong continue game.
    if guess == answer:
      print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
      break
    else:
      print("INCORRECT")
      lives -= 1
    if lives <= 0:
      print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
      break
# Gives a hint as to whether the answer is higher or lower than the users guess.
    if guess < answer:
      print("The number is higher than {}.".format(guess))
    elif guess > answer:
      print("The number is smaller than {}".format(guess))
    elif guess == answer:
      print(" ")
        
def medium_difficulty(guess, answer, lives, str_name):
  print("Your task is to guess a number from 1-50. Good luck!")
  while guess != answer:
    guess = int(input("Guess: "))
# If they get it right end game, if they get it wrong continue game.
    if guess == answer:
      print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
      break
    else:
      print("INCORRECT")
      lives -= 1
    if lives <= 0:
      print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
      break
# Gives a hint as to whether the answer is higher or lower than the users guess.
    if guess < answer:
      print("The number is higher than {}.".format(guess))
    elif guess > answer:
      print("The number is smaller than {}".format(guess))
    elif guess == answer:
      print(" ")

def hard_difficulty(guess, answer, lives, str_name):
  print("Your task is to guess a number from 1-100. Good luck!")
  while guess != answer:
    guess = int(input("Guess: "))
# If they get it right end game, if they get it wrong continue game.
    if guess == answer:
      print("Congratulations, {}. You guessed the correct number! It was {}.".format(str_name, answer))
      break
    else:
     print("INCORRECT")
     lives -= 1
     if lives <= 0:
       print("I'm sorry, you have run out of lives. The correct number was {}".format(answer))
       break
# Gives a hint as to whether the answer is higher or lower than the users guess.
    if guess < answer:
      print("The number is higher than {}.".format(guess))
    elif guess > answer:
      print("The number is smaller than {}".format(guess))
    elif guess == answer:
      print(" ")


difficulty = introduction(difficulty)
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
# - Error catching
# - A way to clear past guesses (while still keeping guess list)
# - Guesses being displayed
# - Different difficulties ✔
# - Add higher or lower ✔
# - Add definitions ✔
# - End Score (points)

