# Withdraw function
def withdraw(balance, amount):
    if amount <= 0:
        print("Invalid amount")
        return balance
    if amount > balance:
        print("Insufficient balance")
        return balance
    if amount % 500 != 0:
        print("Amount must be multiple of 500")
        return balance
    balance = balance - amount
    print("Withdrawal successful")
    return balance
pin = input("Enter your PIN: ")
if pin != "1234":
    print("Wrong PIN.")
else:
    balance = int(input("Enter your balance: "))
    while True:
        amount = int(input("Enter amount to withdraw: "))
        if amount == 0:
            print("Thank you!")
            break
        balance = withdraw(balance, amount)
        print("Remaining balance:", balance)