# This illustration shows the conversion of tuples or list to set while trashing out duplicates.
# Set are data types that are programmed to automatically remove duplicates in elements.
# A set can be listed in a string, list, tuple, interger.

colour = ["Red", "Green", "Blue", "Red", "Grey", "Green"]
colour = set(colour)
print(set(colour))

colour = ("Red", "Green", "Blue", "Red", "Grey", "Green")
colour = set(colour)
print(set(colour))

# to sort set to produce the exact content of elements in a set when you pass more than one agrument
my_set = set(('one', 'two', 'three'))
print(my_set)

# otherwise the below code will print an error because more than one agrument was passed into the set
my_set = set('one', 'two', 'three')
print(my_set)

 