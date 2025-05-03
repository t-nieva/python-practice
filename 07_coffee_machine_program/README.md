# ☕ Coffee Machine Program
This is a simple command-line coffee machine simulator written in Python. 
It allows users to order drinks (espresso, latte, cappuccino), pay with virtual coins, 
and track remaining resources and money earned.

## 📋 Features

- Three drink options: **espresso**, **latte**, and **cappuccino**
- Resource tracking: water, milk, coffee
- Coin-based payment system (quarters, dimes, nickles, pennies)
- Input validation for coin entries
- Change calculation and refunding if payment is insufficient
- `report` command to check remaining resources and earnings
- `off` command to turn off the machine

## Requirements

1. **📝 Prompt user**
   - Ask: “What would you like? (espresso/latte/cappuccino):”
   - Check the user’s input to decide what to do next.
   -  The prompt should show every time an action has completed (e.g. after dispensing a drink), to serve the next customer.

2. **🔌 Turn off the Coffee Machine** by entering “off” to the prompt.
   - Entering `off` should shut down the machine.
   - Only `maintainers` should use the secret word `off`.
   - Program execution should end when `off` is entered.

3. **📋 Print report**
   - Entering `report` should display the current resource values, for example:
     ```
     Water: 100ml 
     Milk: 50ml  
     Coffee: 76g  
     Money: $2.5
     ```

4. **🧪 Check resources sufficient?**
   - On drink selection, check if enough resources are available.
   - If not enough water/milk/coffee:
     - Display: “Sorry there is not enough [resource].”
   - Do not continue to make the drink if any resource is insufficient.

5. **💵 Process coins**
   - If resources are sufficient, prompt user to insert coins.
   - Coin values:
     - 🟤 Quarters = $0.25  
     - 🔵 Dimes = $0.10  
     - 🟢 Nickels = $0.05  
     - 🔴 Pennies = $0.01
   - 🧮 Calculate total inserted. Example:
     ```
     1 quarter, 2 dimes, 1 nickel, 2 pennies =  
     0.25 + (0.10 × 2) + 0.05 + (0.01 × 2) = $0.52
     ```

6. **💰 Check transaction successful?**
   - 🙁 If inserted money < drink cost:
     - Display: “Sorry that's not enough money. Money refunded.”
   - 😃 If inserted money ≥ drink cost:
     - Add drink cost to machine profit.
     - Next `report` should reflect the updated money value.
     - If too much money inserted:
       - Return change, e.g.: “Here is $2.45 dollars in change.”
       - Round to 2 decimal places.

7. **☕ Make Coffee**
   - 🎯 If transaction successful and enough resources:
     - ➖ Deduct ingredients from machine.
     - Example before purchasing latte:
       ```
       Water: 300ml  
       Milk: 200ml  
       Coffee: 100g  
       Money: $0
       ```
     - Example after purchasing latte:
       ```
       Water: 100ml  
       Milk: 50ml  
       Coffee: 76g  
       Money: $2.5
       ```
     - 🎉 Display message: “Here is your latte. Enjoy!” (or other drink name).
