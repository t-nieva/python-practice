import art

print(art.gavel_art)
print("Welcome to the Secret Auction program!\n")

def find_max_bid (bidders_dict):
    max_bid = 0
    winner_name = ''
    for key in bidders_dict:
        if bidders_dict[key] > max_bid:
            max_bid = bidders_dict[key]
            winner_name = key
    print(f"The winner is {winner_name} with a bid of ${max_bid}")

bidders = {}
add_bidder = True
while add_bidder:
    # Question 1
    while True:
        name = input("What is your name?: ").strip().capitalize()
        if name not in bidders:
            break
        print(f"Duplicate name: {name}. Please, enter another name.")

    # Question 2
    try:
        bid = int(input("What is your bid?: $"))
        bidders[name] = bid
    except ValueError:
        print("Error: Bid must be a number.")

    # Question 3
    while True:
        other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.: ").lower()
        if other_bidder == 'no':
            find_max_bid(bidders)
            add_bidder = False
            break
        elif other_bidder == 'yes':
            print("\n" * 50)
            break
        else:
            print("Error: Type 'yes' or 'no'.")
