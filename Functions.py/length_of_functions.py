# Length is an inbuilt function used for checking the length of an element of a variable.
# It is also used in functions to check the length of its elements contained my a function.


# Illustration one

def new_func(name):
    name = 'Amarachi'
    print(len(name))
    return len(name)
    
    # The above is used when in interactive mode 
print()

# Illustration two

def word_length(word):
    word = 'Abracadabra'
    print(len(word))
