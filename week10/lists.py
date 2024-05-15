item = ''
shopping = []
print("Please enter the items of the shopping list (type: quit to finish): ")
while item.lower() !="quit":
    item = input("Item: ").capitalize()
    if item.lower() !="quit":
        shopping.append(item)

for item in shopping:
    print(item)

for i in range(len(shopping)):
    print(f"{i}. {shopping[i]}")

change_index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping[change_index] = new_item.capitalize()

for i in range(len(shopping)):
    print(f"{i}. {shopping[i]}")