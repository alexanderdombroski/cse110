# Testing Rounding
number1 = 0.005
number2 = 1.005
number3 = 2.005
number4 = 3.005

print('two digits')
# round each number
print(f'{number1} --> {round(number1,2)}')
print(f'{number2} --> {round(number2,2)}')
print(f'{number3} --> {round(number3,2)}')
print(f'{number4} --> {round(number4,2)}')

print('integer')
# format each number as a rounded number
print(f'{number1} --> {number1:.0f}')
print(f'{number2} --> {number2:.0f}')
print(f'{number3} --> {number3:.0f}')
print(f'{number4} --> {number4:.0f}')

print()
# Big Number formatting
big_number = 1234567890
print(f'Scientific Notation: {big_number:.5e}')
print(f'number seperating: {big_number:,}')

