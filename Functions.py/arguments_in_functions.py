# Arguments are used when calling upon a function/
# There are two types of arguments
# Positional arguments and keyword arguments; positional argument are associated with parameters are placed..
# .. based on their position while keyword argument, here argument associated with parameters are placed ..
# .. specifically to certain parameter(s).
# Parameters are associated with defining a function while arguments are associated with calling a function.

# Positional argument
def function1(a,b,c):
    print("First argument is :",a)
    print("Second argument is :",b)
    print("Third argument is :", c)
    return a * b + c
function1(10,20,30)
print()

# Keyword arguments
def function2(a,b,c):
    print("First argument is :",a)
    print("Second argument is :",b)
    print("Third argument is :", c)
    return a * b + c
function2(a = 30, b = 10, c = 20)
print()


# Passing arguments and parameters into a main function (multiple arguments into a function)
def get_name_and_age():
    name = 'Sylvia'
    age = 25
    return name, age
person_name, person_age = get_name_and_age()
print(person_name, person_age)
print()

# def show_main(number):

# Combining both positional argument and keyword argument
def function3(a,b,c):
    print("First argument is :",a)
    print("Second argument is :",b)
    print("Third argument is :", c)
    return a * b + c
function3(10, a = 30, c = 20)
# The above statement will produce an error, why?
# Looking at the code you will see that we have missed the order of positional and keyword argument.