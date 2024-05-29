# To calculate the percentage of a numbers, divide the number by the whole and multiply by 100.
# To calculate the percentage using function, the small function calPercent() is used.

def calpercent(x,y,integar=False):
    percent = x/y*100

    if integar:
        return int(percent)
    return percent
print('Percentage:', calpercent(33,200))
print()

numbers = (15,50)
def calPercent(x,y,integar=False):
    percentage = x/y*100
    if integar:
        return int(percentage)
    return percentage
print('Precentage:', calPercent(15,50))
