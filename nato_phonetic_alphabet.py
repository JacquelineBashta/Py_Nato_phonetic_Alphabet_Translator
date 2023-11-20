import pandas as pd

valid_languages = ["en", "de"]
lang = ""
while lang not in valid_languages:
    lang = input(
        "Please choose 'en' for english or 'de' for german:  ").lower()


df = pd.read_csv(f"nato_phonetic_alphabet_{lang}.csv")
nato_d = {row.letter: row.code for (index, row) in df.iterrows()}


user_input = input("Enter a Word: ")

out = [nato_d[letter.upper()] for letter in user_input]

print(out)
