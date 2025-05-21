PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt", mode='r') as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt", mode='r') as letter:
    template = letter.read()
    for name in names:
        name = name.strip()
        new_letter = template.replace(PLACEHOLDER, name)
        with open(f"./Output/Ready_to_send/letter_to_{name}.docx", mode='w') as file:
            file.write(new_letter)
