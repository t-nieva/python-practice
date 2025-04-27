import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
max_score = 21

def get_cards_computer(computer_cards_list, cards_list):
    score = sum(computer_cards_list)
    while score < 17:
        computer_cards_list.append(random.choice(cards_list))
        score = sum(computer_cards_list)
    return computer_cards_list

def blackjack(player_cards_list, computer_cards_list):
    player_score = sum(player_cards_list)
    comp_score = sum(computer_cards_list)
    if player_score == 21 and comp_score < 21:
        print(f"Blackjack! You win!\n")
        return True
    elif comp_score == 21 and player_score < 21:
        print(f"Blackjack! You lose!!!\n")
        return True
    else:
        return False

def print_current_score(player_cards_list, computer_cards_list):
    print(f"Your cards: {player_cards_list}, current score: {sum(player_cards_list)}\n"
          f"Computer first card: {computer_cards_list[0]}\n")

def print_finale_score(player_cards_list, computer_cards_list):
    print(f"Your final hand: {player_cards_list}, final score: {sum(player_cards_list)}\n"
          f"Computer's final hand: {computer_cards_list}, final score: {sum(computer_cards_list)}\n")

def winner_check(player_cards_list, computer_cards_list):
    player_score = sum(player_cards_list)
    comp_score = sum(computer_cards_list)

    if comp_score < player_score:
        print("You are win!!!")
        return True
    elif comp_score > player_score:
        print("You went over. You lose.")
        return True
    elif player_score == comp_score:
        print("Push!")
        return True
    return False

# Check for Ace: it can be counted as 11 or 1 point,
# depending on what is more advantageous for the player to avoid going over 21.
def ace_check(player_cards_list):
    score = sum(player_cards_list)
    for card in player_cards_list:
        index = player_cards_list.index(card)
        if card == 11 and score > 21:
            player_cards_list[index] = 1
            score = sum(player_cards_list)
    if score > 21:
        return False
    else:
        return True

while True:
    player_cards = []
    computer_cards = []
    times = 2
    start = input(f"Do you want play a game of Blackjack? Type 'y' or 'n': \n")
    if start != 'y':
        break

    while times:
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        times -= 1

    print_current_score(player_cards, computer_cards)

    while True:
        # Blackjack
        if blackjack(player_cards, computer_cards):
            print_finale_score(player_cards, computer_cards)
            break

        gamer_score = sum(player_cards)
        # If a player scores more than 21, he loses immediately, regardless of the dealer.
        if gamer_score > 21:
            if not ace_check(player_cards):
                print(f"Your score is over 21.\n"
                      f"You went over. You lose.\n")
                print_finale_score(player_cards, computer_cards)
                break

        to_get_card = input(f"Type 'y' to get another card, type 'n' to pass: \n")
        if to_get_card != 'y':
            computer_cards = get_cards_computer(computer_cards, cards)
            computer_score = sum(computer_cards)

            if computer_score > 21:
                print(f"Computer score is over 21.\n"
                      f"You are win!!!\n")
            else:
                winner_check(player_cards, computer_cards)

            print_finale_score(player_cards, computer_cards)
            break
        player_cards.append(random.choice(cards))
        print_current_score(player_cards, computer_cards)
