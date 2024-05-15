import random as r

play_again = True
while play_again == True:
    number_of_guesses = 0
    secret_number = r.randint(1, 100)
    print('\nI have a secret number between 1 and 100 inclusive.')
    guess = 0

    while guess != secret_number:
        number_of_guesses += 1
        guess = int(input('What is your guess? '))
        if guess == secret_number:
            print("You guessed it!")
            print(f'It took you {number_of_guesses} guesses.\n')
            answer = ''
            while answer not in('yes', 'no'):
                answer = input('Would you like to play again? ').lower()
            if answer == "no":
                play_again = False
        elif guess > secret_number:
            print('Guess lower.')
        else:
            print("Guess higher")

