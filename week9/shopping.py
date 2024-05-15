print("\nWelcome to the Shopping Cart Program!")
print('''
 _        ,
(_\______/________
   \-|-|/|-|-|-|-|/
    \==/-|-|-|-|-/
     \/|-|-|-|,-'
      \--|--''
       \_j________
       (_)     (_)
''')


items = []
prices = []

mode = 2
while mode != 5:
    input("\nPress ENTER to continue\n")
    print("Please select one of the following: ")
    print("1. Add Items")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit")
    mode_input = input("Please type the number of an action: ")
    mode = int(mode_input if mode_input.isnumeric() else 4)
    
    if mode == 1:
        items_to_add = int(input("\nHow many items would you like to add? "))
        for i in range(items_to_add):
            items.append(input("What item would you like to add? ").capitalize())
            prices.append(float(input("How much does it cost? ")))
            print(f"'{items[-1]}' has been added to the list.")
    elif mode == 2 or mode == 3:
        print("\nYour cart contains:")
        for i in range(len(items)):
            print(f"{i + 1}. {items[i]}: ${prices[i]:.02f}")
        if mode == 3 and len(items) > 0:
            remove = int(input('\nWhich item would you like to remove? '))
            if remove <= len(items):
                print(f"{items[remove - 1]} has been removed from the cart.")
                del items[remove - 1]
                del prices[remove - 1]
            else:
                print(f"There is no item with a {remove} behind it.")
    else:
        print(f"\nYour total is ${sum(prices):.2f}.")

print("Thank you for shopping with us. Goodbye\n")