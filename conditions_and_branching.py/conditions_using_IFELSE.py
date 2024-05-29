# Conditon are specific criteria that must be met for a set of instructions to be meet. It is used to determine which set to instructions to 
# execute. Branching is the process of using conditions to examine which set of instructions to execute.
# Here, if one condition is met, one set of instruction will be executed but if the conditions are not met then a different set of instruction 
# will be printed. Here are the operators that can be used; 'if', 'elif', and 'else'or'if-else'


# Branching in python using the 'IF-ELSE' STATEMENT
# The 'else' statement follows an 'if' block and is composed of the keyword else followed by a colon (:). The body of the else statement is
# indented to the right and will be executed if the above 'if statement' does not execute.



# Illustration one

age = 17
if (age > 18):
    print('You are eligble to be in senior secondary school')
else:
    print('You are not eligible to be in senior secondary school')
print('Enjoy your new class')
print()

# Illustration two

account_balance = float(input('Account balance: '))
withdraw_amount = float(input('Withdraw amount: '))
if account_balance >= withdraw_amount:
    print('Dispense cash')
    new_balance = account_balance - withdraw_amount
    print('New balance:', new_balance)
else:
    print('Insufficient fund')
print()

# Illustration three

solar_energy = float(input("Enter full battery of solar after charging: "))
used_energy = float(input("Enter the amount of solar energy used after charge: "))
if solar_energy >= used_energy:
    print('Ability to still discharge electricty')
    new_energy = solar_energy - used_energy
    print('New Energy: ', new_energy)
else:
    print('Low battery and unable to discharge electricty')
print ()

# Illustration four

number = int(input())
if number > 0:
    print("POSITIVE NUMBER")
else:
    print("ZERO OR NEGATIVE NUMBER")