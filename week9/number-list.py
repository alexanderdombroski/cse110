print('Enter a list of numbers, type 0 when finished.')
numbers = []
number = 1
while number:
    number = int(input('Enter number: '))
    if number:
        numbers.append(number)

number_sum = 0
for number in numbers:
    number_sum += number
print(f"\nThe sum is: {number_sum}") # sum()
print(f"The average is: {number_sum / len(numbers):.3f}")

largest_number = 0
for number in numbers:
    largest_number = number if number > largest_number else largest_number
print(f"\nThe largest number is: {largest_number}")
# print(max(numbers))


smallest_number = 10 ** 10
for number in numbers:
    smallest_number = number if number < smallest_number and number > 0 else smallest_number
print(f"The smallest positive number is: {smallest_number}")
# print(min(numbers))

print(f"\nThe sorted list is:")
numbers.sort()
for number in numbers:
    print(number)