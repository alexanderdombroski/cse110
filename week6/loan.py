print('\nRate the following on a scale of 1-10:')
loan = int(input('How large is the loan? ' ))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

if loan >= 5:
    if credit >= 7 and income >= 7:
        decision = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            decision = True
        else:
            decision = False
    else: decision = False
elif credit < 4:
    decision = False
else:
    if income >= 7 or down_payment >= 7:
        decision = True
    elif income >= 4 and down_payment >= 4:
        decision = True
    else:
        decision = False

if decision:
    print("\nLet's sign some paperwork for that loan.\n")
else:
    print("\nSorry we can't approve this loan for you.\n")