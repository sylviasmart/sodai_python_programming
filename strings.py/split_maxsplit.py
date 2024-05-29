# We use maxsplit parameter of function to limit the number of splits that can be performed on a string.

grocery = 'Milk#Chicken#Bread#Butter'
print(grocery.split('#', 1))
print(grocery.split('#', 2))
print(grocery.split('#', 5))
print(grocery.split('#', 0))
