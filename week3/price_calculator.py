import math

#retrieve data about the meal
kids_meal_price = float(input("\nWhat is the price of a kid's meal?: "))
meal_price = float(input("What is the price of an adult's meal?: "))
kids = int(input('How many kids did you buy food for?: '))
adults = int(input('How many adults did you buy food for?: '))
tax = float(input('What is the sales tax rate?: '))/100

# Calculate the totals
subtotal = kids * kids_meal_price + adults * meal_price
taxtotal = subtotal * tax
total = subtotal + taxtotal

#print the totals
print(f'''
Subtotal: ${subtotal:.2f}
Sales Tax: ${taxtotal:.2f}
Total: ${total:.2f}
''')

# Ask for a tip
tip = float(input('What percentage amount would you like to tip?: ')) / 100
total = round((tip + 1) * total, 2)

# Ask for a donation to charity
charity_amount = round(math.ceil(total) - total, 2)
charity = str.lower(input(f'Would you like to round up {charity_amount * 100:.0f} cents for charity? (Yes/No): '))
if charity == 'yes':
    total = total + charity_amount

#recieve payment and calculate change
print(f'\nYour new total is ${total:.2f}.')
payment = float(input('What is the payment amount?: '))
print(f'Change: ${payment - total:.2f}\n')