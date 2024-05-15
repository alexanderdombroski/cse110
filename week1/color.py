#yn=yes/no and fc=favorite color
yn='no'
while yn.lower() != 'yes':
    fc = input('What is your favorite color?: ')
    yn = input('Are you sure that '+fc+' is your favorite color? (yes or no): ')
    print('ok.')
print('Your favorite color is '+fc+'!')