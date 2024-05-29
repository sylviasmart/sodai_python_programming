# NESTED IF STATEMENTS

# A nested if is an if statemen that is the target of another statement. Nested if statements mean an if statement inside another if statement.
# This is skeletal structure of a nested if statement

# if condition1:
#     Executes when condition1 is true
#     if condition2:
#          Executes when condition2 is true
#    if Block is ending here
# if Block is ending here


# Illustration one

number = 5
number2 = 10

if number > 0:
    print("POSITIVE NUMBER")
    if number2 > 5:
        print("ANOTHER POSITIVE NUMBER")
print()