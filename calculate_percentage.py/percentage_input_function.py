# To calculate the percentage of a numbers, divide the number by the whole and multiply by 100.

# To use the input() function, two inputs are required and stored in two variables x and y respectively.
# After the above has been done, the percentage can be checked.

def calPercent(x,y,integar=False):
    percent = x/y*100
    if integar:
        return int(percent)
    return percent
a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
print('Percentage:', calPercent(a,b))
# a and b (67, 150)
print()

# This would print out the output in an integar form because integar was posted true.
a = int(input('Enter the third number:'))
b = int(input('Enter the fourth number:'))
print('Percentage:', calPercent(a,b, integar=True))