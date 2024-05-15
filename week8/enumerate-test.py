
# print(enumerate("Hello World"))
# print(list(enumerate("Hello World"))) # This seems to be the default datatype the enumerate uses during a for loop
# print(dict(enumerate("Hello World")))

number_dict = dict({'one': 1, 'two': 2, 'three': 3}).items() # If you remove the .items() it won't work.
for key, item in number_dict: 
    print(f'{key} = {item}')

print()

for key, item in [(1, 'a'), (2, 'b'), (3, 'a')]:
    print(f'{key} = {item}')

print()

for key, item in [[1, 'a'], [2, 'b'], [3, 'a']]: # Works with lists in lists or tuples in lists
    print(f'{key} = {item}')

# for i, letter in enumerate("Hello World"):
#     print(f"The letter {letter} is at position {i}")

# print()

# for i, letter in dict(enumerate("Hello World")).items():
#     print(f"The letter {letter} is at position {i}")

''' 
Enumerate uses the syntax of a dictionary items list: (dict.items()) in a for loop
during a print, it does not.
Both of these methods create a list of tuples
'''