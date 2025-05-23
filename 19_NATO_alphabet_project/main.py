import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_data_frame = pandas.DataFrame(data)

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
word = input("Enter a word: ").upper()
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_data_frame.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
output_list = [alphabet_dict[letter] for letter in word if alphabet_dict[letter]]
print(output_list)
