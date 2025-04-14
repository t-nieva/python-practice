from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return n1 / n2

math_operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

def calculator():
    while True:
        # Get first number
        try:
            num1 = float(input("What's the first number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # To continue
        while True:
            # Show available operations
            for symbol in math_operations:
                print(symbol)
            operation = input("Pick the operation: ").strip()
            if operation not in math_operations:
                print("Invalid operation selected.")
                continue
            # Get next number
            try:
                num2 = float(input("What's the next number?: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            result = math_operations[operation](num1, num2)
            if result is None:
                break

            print(f"{num1} {operation} {num2} = {result}")
            # Ask to continue
            continue_calc = input(
                f"Type 'y' to continue calculating with {result},\n"
                f"or 'n' to start a new calculation,\n"
                f"or 'q' to quit: ").strip().lower()

            if continue_calc == 'y':
                num1 = result
            elif continue_calc == 'n':
                print("\n" * 20)
                break
            elif continue_calc == 'q':
                print("Goodbye!")
                return
            else:
                print("Unknown command. Exiting.")
                return

calculator()
