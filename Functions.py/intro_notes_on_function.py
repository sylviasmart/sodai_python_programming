# A function is a block of code which only runs when it is called upon, i.e., no results will be seen until..
# ... called upon. Input ===> function
# Also, function is also called a of black-box because we do not understand how it works internally, as we ..
# .. is given an instruction and an output is produced.
# A function contains the use of all the datatypes, loop, condition & branching, variables,etc.
# You can pass data into a function which is known as a parameter into a function.
# There are two types of functions; built-in function and user defined function

# Built-in functions: are in built functions already contained in python3. e.g., max, sum, min, print, type,..
# ... length, float, input,help, etc.
# User-defined functions: They are functions which a user create to help them out.
# Here, an programmer writes a line of code or function and gives it an instruction..
# ..eg. def print(x) ==> def = signifies the definition of the funtion; print = signifies the name of...
# .. of the function; (x) = signifies the parameter of the function.
# but in this case print(x); (x)==> acts as an argument here 
# Parameters are liken as place holders.They are the names used when defining a function, and into which..
# arguments will be mapped.
# while arguments are used when calling upon a function.

def print(x):
    print(x)

def my_func(name):
    print("Hello", name)
    a = 'Joshua'
    my_func(a)

# A function always return a value.
# When a function is in python interactive mode, you don't need the print function, the return function...
# .. works directly.
# e.g. input('Enter name'); =====> Enter name = Ada; =====> 'Ada'. Remember the input function being a...
# ...built in function gives an instruction that must produces and output, it is not put into a variable.
    
# When a function is not in python interactive mode, you need the print function to have an output.
# e.g. name = input("Enter name"); ====> Enter name = Ada; ======> print(name); =====> 'Ada'
# Here the function is encodes in a variable 'name', therefore a print order will be required.
