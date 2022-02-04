import random

def guess():
  x = int(input("Enter the the max limit of this guessing game? (min is 1) :"))
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number:
      guess = int(input(f"Guess a number between 1 and {x} :"))
      if guess < random_number:
          print(" sorry, guess again. too low")
      elif guess > random_number:
          print("Sorry, guess again. Too high")
  print(f"yay, congrats. You have guessed the number {random_number}")

guess()
