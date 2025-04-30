import random
from logo import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def compare_numbers(num_to_guess, player_num):
    if player_num > num_to_guess:
        print("Too high. Guess again.\n")
        return False
    elif player_num < num_to_guess:
        print("Too low. Guess again.\n")
        return False
    else:
        print(f"You got it! The answer was: {number_to_guess}")
        return True

def set_difficulty(level):
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

print(logo)
number_to_guess = random.randint(1, 100)
result = ''
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n")
attempts = set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': " ))
while attempts:
    print(f"You have {attempts} remaining to guess the number.")
    try:
        player_number = int(input("Make a guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    attempts -= 1
    result = compare_numbers(number_to_guess, player_number)
    if result:
        break
if attempts == 0 and result == False:
    print("You've run out of guesses. Refresh the page to run again.")




