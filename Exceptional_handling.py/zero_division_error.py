# In exception handling we are dealing with how to fix errors by identifying the errors and its causes.

# Zero-division error are errors caused by using zero(0) as a denominator in mathematical equation.

# Illustration one

def main():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    
    result = num1/num2
        
    print(num1, 'divided by', num2, 'is', result)
main()


# Illustration two
# Using the if-else statement to solve zerodivision error

def main():
    for _ in range(2):
        print("=", end ="")
        print()
        print("Please do not enter 0 as the second number!!!!")
        
        for _ in range(2):
            print("=", end="")
        print()

    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    
    if num2 == 0:
        print("Cannot divide by Zero!")
    else:
        result = num1/num2
        
        print(f'The division of {num1} by {num2} = {result}')
main()

# In the above code an instruction has already been given to the end user of this code not to use zero to divide else zerodivision error shall
# occur.


# Illustration three
# Another way of solving the above illustration still using an if statement

def main():
    
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    
    # if num2 is not 0, divide num1 by num2 and display the result
    if num2 !=0:
        result = num1/num2
        print(num1, 'divided by', num2, 'is', result)
    else:
        print('Cannot divide by zero')

main()  
