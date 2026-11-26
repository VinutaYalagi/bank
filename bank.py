import sys

def bank_account(name,balance,deposit,withdraw):
    

    print("\nCustomer Name:", name)
    print("Initial Balance: Rs.", balance)

    
    balance = balance + deposit

    print("Balance after deposit: Rs.", balance)
    if withdraw <= balance:
        balance = balance - withdraw
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")

    print("\nCustomer Name:", name)
    print("Updated Account Balance: Rs.", balance)

if __name__ == "__main__":
    if len(sys.argv) == 5:
        name = sys.argv[1]
        balance = float(sys.argv[2])
        deposit = float(sys.argv[3])
        withdraw = float(sys.argv[4])

    bank_account(name,balance,deposit,withdraw)
else:
    print("Please provide details")
