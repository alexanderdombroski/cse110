import random as r

# Choose a difficulty and select a word based off of the difficulty.
print('\nWelcome to a food wordle game!')
difficulty = ''
while difficulty not in('easy', 'medium', 'hard'):
    difficulty = input('Type a difficulty--Easy, Medium, or Hard: ').lower()
if difficulty == 'easy':
    secret_word = r.choice(['apple','burger','fries','pizza','ham','turkey','fish','milk','soda','water','chicken','cheese','soup','egg','taco','wing','pear','candy','rice','salad','toast','sushi','cracker','grape','lemon','orange','pie','donut'])
elif difficulty == 'medium':
    secret_word = r.choice(['sandwich','chowder','lobster','pastromi','meatball','banana','burrito','chocolate','pasty','calzone','waffle','pancake','pineapple','pepper','cucumber','cabbage','lettuce','carrot','tomato','potato','curry','popcorn','cookie','brownie','crepe','scone','pumpkin','squash','yogurt'])
else:
    secret_word = r.choice(['lasagna','enchilada','quesadilla','dragonfruit','omlelette','taquito','cheeseburger','pomegranate','jalapeno','tostada','coleslaw','brookie','watermelon','zucchini','cauliflower','spaghetti','cheesecake','dumpling','macaroon'])

# Give hints based off guesses
number_of_guesses = 0
word_not_guessed = True
print(f"\nYour hint is: {len(secret_word) * '_ '} ({len(secret_word)} letters)")
while word_not_guessed:
    guess = input('\nWhat is your guess? ').lower()
    number_of_guesses += 1
    if guess == secret_word:
        print(f'\nGreat job! The secret word is {secret_word}')
        print(f'It took you {number_of_guesses} guesses.\n')
        word_not_guessed = False
    elif len(guess) == len(secret_word):
        hint = ''
        print('Your hint is:', end = ' ')
        for index, letter in enumerate(guess):
            if secret_word[index] == letter:
                print(letter.upper(), end = ' ')
            elif letter in secret_word:
                print(letter, end = ' ')
            else:
                print('_', end = ' ')
    else:
        print('Wrong number of letters. Make another guess.', end = '')