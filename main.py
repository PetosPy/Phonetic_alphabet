import pandas
#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Please insert a word you want to code: ").upper()
output = [phonetic_dict[letter] for letter in user_word]


print(phonetic_dict)
print(output)


