import random

secret_word = random.choice(["one", "two", "three"])

number_of_guesses = 0

print("welcome")

print("Your hint is: ", end="")

for letter in secret_word:
    print("_ ", end="")

print()

notguess = True
while notguess:
    guess = input("What is your guess? ")
    number_of_guesses += 1
    
    if guess == secret_word:
        notguess = False
    elif len(guess) != len(secret_word):
        print("Sorry, wrong number of letters.")
    else:
        # The section we determine what letter are correct and/or in right position
        print("Your hint is: ", end="")
        for i, character in enumerate(guess):
            if character == secret_word[i]:
                print(character.upper(), end=" ")
            elif character in secret_word:
                print(character, end=" ")
            else:
                print("_", end=" ")
        print()


print("congrations, you are correct")

print(f"It took you {number_of_guesses} guesses")