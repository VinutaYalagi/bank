import sys

def bank_account():
    name = input("Enter customer name: ")

    balance = float(input("Enter initial balance: "))

    print("\nCustomer Name:", name)
    print("Initial Balance: Rs.", balance)

    deposit = float(input("\nEnter amount to deposit: "))
    balance = balance + deposit

    print("Balance after deposit: Rs.", balance)

    withdraw = float(input("\nEnter amount to withdraw: "))

    if withdraw <= balance:
        balance = balance - withdraw
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")

    print("\nCustomer Name:", name)
    print("Updated Account Balance: Rs.", balance)

if __name__ == "__main__":
    bank_account()