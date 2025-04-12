from operator import index
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            _index = alphabet.index(letter) + shift_amount
            _index %= len(alphabet)  # 0-25
            output_text += alphabet[_index]

    return output_text

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    if direction not in ('encode', 'decode'):
        print(f"Error: invalid direction '{direction}'!")
        continue

    text = input("Type your message:\n").lower().strip()

    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Error: Shift must be a number.")
        continue

    result = caesar(text, shift, direction)
    print(f"Here's the {direction}d result: {result}")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").strip().lower()
    if restart != 'yes':
        should_continue = False
        print("Goodbye!")
