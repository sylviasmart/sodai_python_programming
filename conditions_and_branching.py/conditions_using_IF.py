# Conditon are specific criteria that must be met for a set of instructions to be meet. It is used to determine which set to instructions to 
# execute. 
# Branching is the process of using conditions to examine which set of instructions to execute.
# Here, if one condition is met, one set of instruction will be executed but if the conditions are not metthen a different set of instruction 
# will be printed.Here are the operators that can be used; 'if', 'elif', and 'else'or'if-else'


# Branching in python using IF STATEMENTS
# You can use an if statement to evaluate a comparison. You start with the keyword, followed by our comparison and end the line with a colon
# (:). The body of the if statement is then indented to the right. If the comparison is True, the code inside the if body is executed. If the
# comparison evaluates to False, then the code block is skipped and will not be run. But when you want the code block to do something different
#  if the evaluation is False, the 'elif' and 'else' statement will come in handy.

# Illustration one

age = 15
if (age > 18):
    print('You are not eligble to be in senior secondary school')
print('Enjoy your new class')
print()

# Illustration two

age = 19
if (age > 18):
    print('You are eligble to be in senior secondary school')
print('Enjoy your new class')
print()

# Illustration three

cumulative_grade_point = 5.0
if (cumulative_grade_point > 4.5):
    print('You are eligble and qualify for a first class certification')
print()