# The reduce and lambda function can be used to find the average function of a list of numbers.
# You have to first import the reduce function from the functoolc module as it is not inbuilt in python3.
# You import the reduce and lambda function by adding the following line of code at the beginning of....
# .....you script "From functools import reduce"
# Create the list of numbers for which you want to calculate the average.
# Use the reduce function along with lambda function to iterate the list and compure the sum of the numbers.
# Divide the sum by length of the list to the average.
# Print or store the average for further use.

from functools import reduce
my_list = [1, 2, 3, 4, 5]
average = reduce(lambda x, y: x + y, my_list)/len(my_list)
print(average)