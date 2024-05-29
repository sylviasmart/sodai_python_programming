# The main function is like an entry point of a program. It allows python interpreter to run all lines of code right from the first line.
# The execution of code starts from the starting line and goes line by line to the end.

# Illustration one

def message():
    print("I am Arthur", )
    print("King of Britons", )
def main():
    print("I have a message", )
    for i in message():
        print("I have a message for you")
main()

# Illustration two
# Passing more than two arguments into the main function
def show_sum(num1, num2):
    result = num1 + num2
    print(result)

def main():
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    result = number1 + number2
    print(result)

main()

# Illustrations three
def texas():
    birds = 5000
    print("Texas has", birds, "birds")
def california():
    birds = 8000
    print("California has", birds, "birds")
def main():
    texas()
    california()

main()

