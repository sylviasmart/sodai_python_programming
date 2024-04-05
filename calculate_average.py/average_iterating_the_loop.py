# Average functions involves utilizing a for loop to iterate through the list of numbers & accumulate their sum.
# 

# Average function using iterating loop
def average(numbers):
    if len(numbers):
        return None
    else:
        total = 0
        for num in numbers:
            total += num
        return total/len(numbers)
    list = [1, 5, 6, 8]
    print('The average of list is', average(list))
     