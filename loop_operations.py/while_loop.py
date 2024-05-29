# Loop is a function that is used to run operations over and over or rather continously until the given...
# .. instruction or order is met. 

# WhHILE LOOP: It is used to execute a block of statements repeatedly until a given condition is satisfied. While loop falls under the category
#  of 'indefinite iteration'. Indefinite iteration means that the number of times the loop is executed is not specified explicity in advance.

# Illustration one

num = 2
while num < 3:
    num = num + 1
print()

# Illustration two

num = 5
while num < 3:
    num = num + 1
print()

# Illustration three

while 2 > 3:
    print('Heyyyyyy')
print()

# Illustration four
squares = ["orange", "orange", "purple", "orange", "blue"]
print(squares)
new_squares = []
a = 0
while squares [a] == "orange":
    new_squares.append(squares[a])
    a = a + 1
print(new_squares)