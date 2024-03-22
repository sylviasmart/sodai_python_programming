account_balance = float(input('Account balance: '))
withdraw_amount = float(input('Withdraw amount: '))
if account_balance >= withdraw_amount:
    print('Dispense cash')
    new_balance = account_balance - withdraw_amount
    print('New balance:', new_balance)
else:
    print('Insufficient fund')