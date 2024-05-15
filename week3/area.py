import math
square_length = float(input('\nWhat is the length of a side of the square? '))
print(f'The area of the square is: {square_length ** 2}')

rectangle_length = float(input('What is th elength of a rectangle? '))
rectangle_width = float(input('What is the width of the rectangle? '))
print(f'The area of the rectangle is: {rectangle_length * rectangle_width}')

circle_radius = float(input('What is the radius of the circle? '))
print(f'The area of the circle is: {math.pi * circle_radius ** 2}\n')


# Stretch requirements

side = float(input('What is the side length? '))
print(f'The area of a square with the given length is {side ** 2}')
print(f'The area of a circle is {math.pi * side ** 2}')
print(f'The volume of a cube is {side ** 3}')
print(f'The area of a sphere is {4/3 * math.pi * side ** 3}')



square_length = float(input('\nWhat is the length of a side of the square in cm? '))
print(f'The area of the square is: {square_length ** 2} square cm or {(square_length/100)**2} square m')

rectangle_length = float(input('What is th elength of a rectangle in cm? '))
rectangle_width = float(input('What is the width of the rectangle in cm? '))
print(f'The area of the rectangle is: {rectangle_length * rectangle_width} square cm or {rectangle_width * rectangle_length / 10000} square m')

circle_radius = float(input('What is the radius of the circle in cm? '))
print(f'The area of the circle is: {math.pi * circle_radius ** 2} square cm or {math.pi * (circle_radius/100) ** 2} square m\n')