ACCEPTED_COINS = [25, 10, 5]

enteredAmount = input("Enter amount: ")

amount_payed = 0

def handle_payment(amount):
    global amount_payed
    amount = int(enteredAmount)

    check_amount(amount)
    
    while amount_payed < 50:
        print('Amount: ', amount_payed)
        requestPayment = input("Add more coins to purchase (50 coins required): ")
        next_amount = int(requestPayment)

        check_amount(next_amount)
        
    if amount_payed > 50:
        change_owed = amount_payed - 50
        return "Successfully purchase Coca-Cola bottle at 50 cents and we owe you " + str(change_owed) + " cents"
    else:
        return "Successfully purchase Coca-Cola bottle at 50 cents"
    

def check_amount(amount_entered):
    global amount_payed

    if amount_entered not in ACCEPTED_COINS:
        print('Amount: ', amount_payed)
        print("You can only use 25, 10 or 5 coins to pay!")
        requestPayment = input("Add more coins to purchase (50 coins required): ")
        next_amount = int(requestPayment)

        check_amount(next_amount)
    else:
        amount_payed += amount_entered
    


print(handle_payment(enteredAmount))
