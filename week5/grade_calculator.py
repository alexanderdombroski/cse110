# Team Activity

grade = int(input('\nWhat is your grade percentage? '))

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

grade_digit = grade % 10
if letter != 'F':
    if grade_digit >= 7:
        grade_modifier = '+'
    elif grade_digit <= 3:
        grade_modifier = '-'
    else:
        grade_modifier = ''
else:
    grade_modifier = ''


print(f"You have a {letter+grade_modifier}.")

if grade >= 70:
    print('You are passing the course... for now!')
else:
    print('Your failing. Find a tutor. You can do it!')

