accounts = []
balances = []

print("\nEnter the names and balances of bank accounts (type: quit when done)")
account = ""
while account != "Quit":
    account = input("What is the name of this account? ").capitalize()
    if account !="Quit":
        balance = float(input("What is the balance? "))
        accounts.append(account)
        balances.append(balance)

def account_info():
    print("\nAccount Information:")
    for i in range(len(accounts)):
        print(f"{i}. {accounts[i]} - {balances[i]:.2f}")
    print(f"\nTotal: ${sum(balances):.2f}")
    print(f"Average: ${sum(balances) / len(balances):.2f}")

account_info()
update = "yes"
while update.lower() != "no":
    update = input("\nDo you want to update an account? ").lower()
    if update != "no":
        account_index = int(input("What account index do you want to update? "))
        balances[account_index] = float(input("What is the new amount? "))
        account_info()