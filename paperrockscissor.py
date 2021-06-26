import random


def conv_prs(x):
    if x == 0:
        return "paper"
    elif x == 1:
        return "rock"
    elif x == 2:
        return "Scissor"


computer_guess = random.randint(0, 2)
human_guess = int(input("enter 0 for paper, 1 for rock, 2 for scissor: "))
print(f"Computer guess: {conv_prs(computer_guess)} \nHuman guess: {conv_prs(human_guess)}")


def rockpaperscissor(human_guess, computer_guess):
    if human_guess == computer_guess:
        return "It's a Tie"
    elif human_guess == 0 and computer_guess == 1:
        return "Human win"
    elif human_guess == 0 and computer_guess == 2:
        return "Computer win"
    elif human_guess == 1 and computer_guess == 2:
        return "Human win"
    else:
        return "invalid number entered"



print(rockpaperscissor(human_guess, computer_guess))
