import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_data_frame = pandas.DataFrame(data)
# alphabet_dict => NATO dictionary in format: {"A": "Alfa", "B": "Bravo"}
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_data_frame.iterrows()}
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [alphabet_dict[letter] for letter in word if alphabet_dict[letter]]
        print(output_list)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

generate_phonetic()
