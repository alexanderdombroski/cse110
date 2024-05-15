number = int(input('\nPlease type a positive number: '))
while number < 0:
    number = int(input('Please type a positive number: '))

print(f'The number is {number}\n')

answer = 'no'
while answer != 'yes':
    answer = input('May I have a piece of candy? ')
print('Thank you.\n')