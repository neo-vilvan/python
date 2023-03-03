import random

attempts_list = []

def score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))

def game():
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Y/N) ".format(player_name))

    score()

    while wanna_play.lower() in ["yes", "y"]:
        total_guessed_number = list(range(1, 11))
        random_number = random.randint(1, 10)
        attempts = 0

        while True:
            try:
                guess = 0
                guess = int(input(f"Pick a number between {total_guessed_number}: "))
                if guess in total_guessed_number:
                    total_guessed_number.remove(guess)
                if guess < 1 or guess > 10:
                    raise ValueError("Please guess a number within the given range")
            except ValueError as err:
                print("Oh no!, that is not a valid value. Try again...")
                print("({})".format(err))
            else:
                attempts += 1
                if guess == random_number:
                    print("Nice! You got it!")
                    attempts_list.append(attempts)
                    print("It took you {} attempts".format(attempts))
                    play_again = input("Would you like to play again? (Enter Yes/No) ")
                    score()
                    if play_again.lower() in ["no", "n"]:
                        print("That's cool, have a good one!")
                        return
                    break
                elif guess > random_number:
                    print("It's lower")
                elif guess < random_number:
                    print("It's higher")

if __name__ == '__main__':
    game()
