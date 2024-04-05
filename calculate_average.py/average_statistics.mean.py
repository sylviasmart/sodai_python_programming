# Statistics mean module is a built-in function for calculating different types of average such as mean,...
# mode, and median.
# # You import the statistics function by adding the following line of code at the beginning of....
# .....you script "from statistics import mean", or "import statistics"

# Calculating average using statistics.mean()
from statistics import mean 
num_list = [30, 55, 3, 10, 2]
average = mean(num_list)
print('Average:', round(average,3))
print()

from statistics import mean
numbers = [1, 999, 2, 1023, 223, 876, 32]
average = mean(numbers)
print('Average:', round(average,3))
print()

import statistics
numbers = [1, 2, 3, 4, 5]
average = statistics.mean(numbers)
print('The average of list is', average)
print()

