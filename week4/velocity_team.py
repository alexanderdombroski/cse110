import math

print('\nWelcome to the velocity calculater. Please input the following:\n')

# retrieve inputs
m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

# Calculate

c = 1/2 * p * A * C
v = math.sqrt(m * g / c) * (1 - math.e ** (math.sqrt(m * g * c) / m * -t))
v_terminal = math.sqrt(m * g / c)

# Output
print(f'\nThe inner value of c is: {c:.3f}')
print(f'The velocity after {t:.1f} is: {v:.3f} m/s')
print(f'Terminal velocity without air resistance is {v_terminal:.3f} m/s\n')