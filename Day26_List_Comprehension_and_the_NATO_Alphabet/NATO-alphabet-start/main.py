import pandas

data = pandas.read_csv("Python/Day26_List_Comprehension_and_the_NATO_Alphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv")
print(data.to_dict())
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
print()
phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print()
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter]  for letter in word]
print(output_list)