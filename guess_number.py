import random

computer_number = random.randint(1, 10)
max_guesses = 4
guess = 0

for num_guesses in range(max_guesses):
    while True:
        guess = int(input("Guess your number (between 1 and 10): "))
        if guess < 1 or guess > 10:
            print("Invalid input. Your guess must be between 1 and 10.")
        else:
            break
        
    if guess < computer_number:
        print("Your guess is too low.")
    elif guess > computer_number:
        print("Your guess is too high.")
    else:
        print(f"Congratulations! You guessed correctly in {num_guesses + 1} tries.")
        break

if guess != computer_number:
    print(f"Sorry, you failed. The number was {computer_number}.")




  