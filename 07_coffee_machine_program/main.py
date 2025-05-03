from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_profit = 0

def check_resources (ingredients_dict):
    """
    :param ingredients_dict: dictionary
    Example: ingredients: {
            "water": 50,
            "coffee": 18,
        }
    :return: If drink ingredients enough True, else False
    """
    for ingredient in ingredients_dict:
        if resources[ingredient] < ingredients_dict[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    """
    :return: Total amount of coins inserted by the client, or False if the input is invalid.
    """
    print("Please insert coins.")
    try:
        total = int(input("How many quarters? (quarters = $0.25) 🟤  ")) * 0.25
        total += int(input("How many dimes? (dimes = $0.10) 🔵 ")) * 0.10
        total += int(input("How many nickles? (nickles = $0.05) 🟢 ")) * 0.05
        total += int(input("How many pennies? (pennies = $0.01) 🔴 ")) * 0.01
        total = round(total, 2)
        print(f"💵 Total inserted: ${total}")
        return total
    except ValueError:
            print("Invalid input. Please enter a number.")
            return False

def is_transaction_successful(customer_money, drink_cost):
    """
    :param customer_money: Total amount of coins inserted by the customer.
    :param drink_cost: The cost of the selected drink.
    :return: True if the total number of coins is enough, or False if not.
    """
    if customer_money < drink_cost:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round((customer_money - drink_cost), 2)
        if change:
            print(f"Here is ${change} dollars in change.")
        global money_profit
        money_profit += drink_cost
        return True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if choice == 'off':
        print("Turning off the coffee machine. Goodbye! ☕")
        break
    elif choice == 'report':
        print(f"Water: {resources['water']}ml,\n"
              f"Milk: {resources['milk']}ml,\n"
              f"Coffee: {resources['coffee']}g,\n"
              f"Money: ${money_profit}\n")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            print(f"{choice.capitalize()} cost: ${drink['cost']}")
            total_coins = process_coins()
            while not total_coins:
                total_coins = process_coins()
            if is_transaction_successful(total_coins, drink['cost']):
                for item in drink['ingredients']:
                    resources[item] -= drink['ingredients'][item]
                print(logo)
                print(f"Here is your {choice}. Enjoy!")
