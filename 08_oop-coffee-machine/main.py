from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ").strip().lower()
    if choice == 'off':
        print("Turning off the coffee machine. Goodbye! ☕")
        break
    elif choice == 'report':
        coffee_machine.report()
        money_machine.report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        menu_item = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_machine.make_coffee(menu_item)
