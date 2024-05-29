# Logic operators are used to combine multiple conditions together and evaluate them as a single boolean expression.
# The include 'and', 'or', and 'not'. It takes two operands to use this operators

# AND & OR Operators
# This the combination of both the OR and AND operators
a_carton_of_noodles = 40
two_cartons_of_noodles = 80
if(a_carton_of_noodles < 80) or (two_cartons_of_noodles < 100) and (two_cartons_of_noodles == 80):
    print("Available for sale")
else:
    print("Commodities is currently unavialable for sales and consumption")
print()

# Illustration two
duration_of_cologne = 48
if(duration_of_cologne > 24) and (duration_of_cologne < 48) or (duration_of_cologne == 24):
    print("Cologne is original and long-lasting")
else:
    print("Cologne is likely to be fake or possess inferior production materials")
print()

# Illustration three
gorcery_shopping_budget = 4000

if(gorcery_shopping_budget<3500) and (gorcery_shopping_budget>3950) or (gorcery_shopping_budget == 4000):
    print("Grocery shopping budget is duly met")
else:
    print("Grocery shopping budget might have to be restructured!!")
print()

# Illustration four
Annual_resident_rent = 1000

if(Annual_resident_rent<500) or (Annual_resident_rent>1200) and (Annual_resident_rent == 1000):
    print("My annual house rent budget has been met and can be catered for!!")
else:
    print("My annual house rent has exceeded the expectations and a second option might be opted for!!")