# The operator functions such as 'if' and 'else' can be used to test strings.
# Since the if and else operators are used, the true given statement or false given statement are returned.
# Note that: If represents a true statement while Else represents a false statement

sentences = 'The young 24 BOUA aircraft is red'
if sentences.isdigit():
    print('the sentences contains digits')
if sentences.isalpha():
    print('the sentences contains alphabets')
if sentences.isalnum():
    print('the sentence contains alphabets and numbers')
if sentences.islower():
    print('the sentences is made up of lower class letters')
if sentences.isupper():
    print('the sentences contains uppercase letters')
if sentences.isspace():
    print('the sentences contains whitepaces')
else:
    print('All contains all the elements of test')

print()
string = 'sylvia2024'
if string.isdigit ():
    print('string contains only digit')
else:
    print('string does not contain only digit')