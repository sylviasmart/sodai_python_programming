# The f'string is a variable known as "Format". This function allows you ti interpolate.
# Interpolation: To insert or introduce (a comment, passage, etc) into (a conversation, text.)
# Also; To estimate a value of a function between the value already known or determined.


# Illustration one
def main():
    # Get two numbers
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))

    # Divide num1 by num2 and display the result
    result = num1/num2
    print(num1, 'divided by', num2, 'is', result)
    print(f'The division of ', num1, 'and', num2, 'is')

# call the main function
main()