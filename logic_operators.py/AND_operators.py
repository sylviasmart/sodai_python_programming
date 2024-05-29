# Logic operators are used to combine multiple conditions together and evaluate them as a single boolean expression.
# The include 'and', 'or', and 'not'. It takes two operands to use this operators

# AND Operators
# 'and' operator returns true if both are true, otherwise returns false.
bluetooth_device = 100

if(bluetooth_device < 70) and (bluetooth_device > 95):
    print("bluetooth fully charged")
else:
    print("bluetooth battery low, please disconnect")
print()

# Illustration two 
gorcery_shopping_budget = 4000

if(gorcery_shopping_budget<3500) and (gorcery_shopping_budget>3950) and (gorcery_shopping_budget == 4000):
    print("Grocery shopping budget is duly met")
else:
    print("Grocery shopping budget might have to be restructured!!")
print()

# Illustration three
Annual_resident_rent = 1000

if(Annual_resident_rent<1500) and (Annual_resident_rent>900):
    print("My annual house rent budget has been met and can be catered for!!")
else:
    print("My annual house rent has exceeded the expectations and a second option might be opted for!!")