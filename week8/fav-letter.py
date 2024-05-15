fav_number = int(input('\nWhat is your favorite number? '))

for index, letter in enumerate('commitment is awesome.    '):
    if index / fav_number == index // fav_number:
        letter = letter.capitalize()
    print(letter, end="")

print()