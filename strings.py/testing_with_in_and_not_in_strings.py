# The operator functions such as 'in' and 'notin' can be used to test strings.
# Since operators are used it makes it a boolean as true given statement or false given statement are returned.
# Note that: If represents a true statement while Else represents a false statement


# The following shows the 'in' operator function 
text = 'Four score and seven years ago'
if 'seven' in text:
    print('the string "seven" was found')
else:
    print('the string "seven" was not found')
print()

text = 'Four score and eight years ago'
if 'seven' in text:
    print('the string "seven" was found')
else:
    print('the string "seven" was not found')
print()

colours = 'A box of six colours contain colour red, green, white, peach, liliac, brown'
if 'yellow' in colours:
    print('The box contains colour "yellow"')
else:
    print('The colour "yellow" was not found in the box')
print()

races = 'The world contains people with skin colours white, black, brown, yellow, etc.'
if 'green' in races:
    print('They are likely to be aliens')
else:
    print('It is not biologically possible')
print()

# The following shows the 'not in' operator functions
text = 'Four score and seven years ago'
if 'seven' not in text:
    print('the string "seven" was not found')
else:
    print('the string "seven" does not exist')
print()

text = 'Four score and eight years ago'
if 'seven' not in text:
    print('the string "seven" was not found')
else:
    print('the string "seven" does not exist in the text')
print()

colours = 'A box of six colours contain colour red, green, white, peach, liliac, brown'
if 'yellow' not in colours:
    print('The box does not contain colour "yellow"')
else:
    print('The colour "yellow" does not likely exist in the box')
print()

races = 'The world contains people with skin colours white, black, brown, yellow, etc.'
if 'green' not in races:
    print('They are likely to be human beings')
else:
    print('It is very possible for aliens to be more imagination')
print()
