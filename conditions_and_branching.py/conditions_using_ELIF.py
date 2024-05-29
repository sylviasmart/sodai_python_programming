# Conditon are specific criteria that must be met for a set of instructions to be meet. It is used to determine which set to instructions to 
# execute. Branching is the process of using conditions to examine which set of instructions to execute.
# Here, if one condition is met, one set of instruction will be executed but if the conditions are not met then a different set of instruction 
# will be printed. Here are the operators that can be used; 'if', 'elif', and 'else'or'if-else'


# Branching in python using 'IF_ELIF-ELSE' and 'ELIF'
# This is similar to the if statements, an elif statement starts with the 'elif' keyword, followed by a comparison to be evaluated. This is
# followed by a colon (:), and then the code block on the next line, indented to the right. An 'elif' statement must follow an if statement,
# and will only be evaluated if the 'if statement' was evaluated as False.


# Illustration one

age = 15
if (age > 18):
    print('You are eligble to be in senior secondary school')
elif (age < 2):
    print('Senior secondary  not merited')
else: 
    print('You are not eligible to be in senior secondary school')
print()

# Illustration two

age = 1
if (age > 18):
    print('You are eligble to be in senior secondary school')
elif (age < 2):
    print('Senior secondary  not merited')
elif (age <= 18):
    print('You are not eligible to be in senior secondary school')

# Illustration three

cumulative_grade_point = 1.5
if (cumulative_grade_point > 4.5):
    print('Your eligible to graduate with a first class certificate')
elif(cumulative_grade_point < 2.0):
    print('Your cumulative grade is poor and will qualify only for lower class grade')
elif(cumulative_grade_point <= 1.5):
    print('You are not eligble for graduation and issuance of certificate')
print()

# Illustration four

number = int(input())
if number > 0:
    print("POSITIVE NUMBER")
elif number < 0:
    print("NEGATIVE NUMBER")
else:
    print("ZERO")
print()
