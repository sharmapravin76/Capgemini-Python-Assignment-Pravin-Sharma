account_balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
if withdraw_amount <= account_balance and withdraw_amount % 100 == 0:
    print("Withdrawal successful")
else:
    print("Invalid withdrawal request")