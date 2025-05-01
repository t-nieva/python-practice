from art import logo, vs
from game_data import data
import random

def get_data(account):
    """
    Formats and returns a string with a person's name, description, and country.
    """
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(user_answer, a_followers,b_followers):
    """
    :param user_answer: 'A' or 'B' — the user's guess
    :param a_followers: Follower count of account A
    :param b_followers: Follower count of account B
    :return: True if the guess is correct, False otherwise
    """
    if a_followers > b_followers:
        return user_answer == "A"
    else:
        return user_answer == "B"

print(logo)
score = 0
account_b = random.choice(data)
while True:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {get_data(account_a)}")
    print(vs)
    print(f"Against B: {get_data(account_b)}\n")
    answer = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    print(f"\n" * 20)
    print(logo)
    if check_answer(answer, account_a['follower_count'], account_b['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
