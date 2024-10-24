ACCEPTED_COINS = [25, 10, 5]

enteredAmount = input("Enter amount: ")

amount_payed = 0

def handle_payment(amount):
    global amount_payed
    amount = int(enteredAmount)

    if amount not in ACCEPTED_COINS:
        return "You can only use 25, 10 or 5 coins to pay!"
    
    amount_payed += amount

    while amount_payed < 50:
        requestPayment = input("Continue adding more coins to purchase: ")
        next_amount = int(requestPayment)

        if next_amount not in ACCEPTED_COINS:
            return "You can only use 25, 10 or 5 coins to pay!"
    
        amount_payed += next_amount 
    
    if amount_payed > 50:
        change_owed = amount_payed - 50
        return "Successfully purchase Coca-Cola bottle at 50 cents and we owe you " + str(change_owed) + " cents"
    else:
        return "Successfully purchase Coca-Cola bottle at 50 cents"
    


print(handle_payment(enteredAmount))
