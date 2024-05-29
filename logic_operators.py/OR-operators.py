# Logic operators are used to combine multiple conditions together and evaluate them as a single boolean expression.
# The include 'and', 'or', and 'not'. It takes two operands to use this operators

# OR operators
# 'or' operator is used to combine two or more conditions in a logic expression.
# It returns true if atleast one conditions is true.

album_year = 1990
if(album_year < 1980) or (album_year > 1989):
    print("album made in 70's or 90's")
else:
    print("album made in 1980's")
print()

# Illustration two
bluetooth_device = 100
if(bluetooth_device < 70) or (bluetooth_device > 95):
    print("bluetooth fully charged")
else:
    print("bluetooth battery low, please disconnect")
print()

# Illustration three
duration_of_cologne = 48
if(duration_of_cologne > 24) or (duration_of_cologne < 48) or (duration_of_cologne == 24):
    print("Cologne is original and long-lasting")
else:
    print("Cologne is likely to be fake or possess inferior production materials")
print()