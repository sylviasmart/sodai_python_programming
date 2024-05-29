# METHODS: They are functions defined within a class that define the behaviour of objects. They can perform various operations, 
# manipulate data, and interact with other objects.

# In the first below illustration, the list type has a method for sorting values in a list which is called 'sort'.
# Calling upon the '.sort()' method changes the data contained in the object.

ratings = [10, 9, 6, 5, 10, 8, 9, 6, 2]
ratings.sort()
print(ratings)

# In the above illustration the '.sort()' method was used to change the data contained in the object of the list. Another method such as
# '.reverse()' can be used the reverse the current order of the items in the list.

ratings = [10, 9, 6, 5, 10, 8, 9, 6, 2]
ratings.reverse()
print(ratings)