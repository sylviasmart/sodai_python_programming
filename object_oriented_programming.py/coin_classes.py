# CLASS: It is a user-defined data type, which consist of the data members and members functions, and can be accessed and used by creating 
# an instance of that class. It represents the set of properties or methods that are common to all the objects of one type. It is a 
# blueprint/template for an object. E.g.:  Class of cars. Cars might have different names and brands but all shares some common properties like
# 4 wheels, speed, limit, fuel level, brakes, mileage range etc. Here, the class is "Car" and the wheels, speed, etc its properties.
# A class defines the structure and behaviour that its object will have. In python, classes are created using the 'class' keyword.


# In the first below illustration, __init__(means initializing method because its objects data attributes), toss, and get_sideup are methods 
# of the class Coin (wh at we call variables in regular functions).
# They are have the method parameter variable called (self). Now, remember that a 'method' operates on a specific object data attributes.
# When a method is executed, it must have a way of knowing which objects data attributes it is suppose to operate on. hence, the use of the
# parameter 'self', when a method is called upon, the python makes the self parameter reference the specific object that the method is
# supposed to operate on.


import random


class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup
    
def main():
    my_coin = Coin()
    print('This side is up:', my_coin.get_sideup())
    print('I am tossing the coin ....')
    my_coin.toss()
    print('This side is up:', my_coin.get_sideup())

main()


kobo = Coin()
penny = Coin()
cents = Coin()

print("Before tossing")
print(kobo.get_sideup())
print(penny.get_sideup())
print(cents.get_sideup())

kobo.toss
penny.toss

print("After tossing")
print(kobo.get_sideup())
print(penny.get_sideup())
print(cents.get_sideup())