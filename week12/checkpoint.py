print()

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = ""
min_age = 999
for item in people:
    data = item.split()
    print(f'{data[0]} is {data[1]} years old.')
    min_age = min(int(data[1]), min_age)
    if int(data[1]) == min_age:
        youngest = data[0]

print(f"\n{youngest} is the youngest person with an age of {min_age}.\n")