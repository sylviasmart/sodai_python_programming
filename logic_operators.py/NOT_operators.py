# Logic operators are used to combine multiple conditions together and evaluate them as a single boolean expression.
# The include 'and', 'or', and 'not'. It takes two operands to use this operators

# NOT Operators
# 'not' is an operator that reverses the boolean value of an expression.
# It can be used with any expression that evaluate to true or false.

dog_barks = True
if not dog_barks:
    print('Dogs do not bark')
else:
    print('Dogs bark always')
print()

# Illustration two
a = 10
b = 20
if not a > b:
    print('a is not greater than b')
else:
    print('a is greater than b')
print()

# Illustration three
bridal_dress_color_is_white = True
if not bridal_dress_color_is_white:
    print("Brides will not be allowed to wed wearing colored gown that isn't white!!")
else:
    print("Brides will enjoy smooth wedding rights when putting on white colored gowns!!")
print()

# Illustration four
Ama_shoe_size = 41
Anna_shoe_size = 37
if not Ama_shoe_size > Anna_shoe_size:
    print("Anna's shoe size is not greater than Ama's shoe size")
else:
    print(f" Ama has literally a plus size feet of  {Ama_shoe_size}, which makes Anna not her perfect fit")
print()

Ama_shoe_size = 41
Anna_shoe_size = 37
if not Ama_shoe_size < Anna_shoe_size:
    print(f" Anna is a small_sized footed individual with shoe size of  {Anna_shoe_size}, which makes Ama not her perfect fit")
else:
    print("Anna's shoe size is not greater than Ama's shoe size")