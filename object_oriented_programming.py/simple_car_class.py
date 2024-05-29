# CLASS: It is a user-defined data type, which consist of the data members and members functions, and can be accessed and used by creating 
# an instance of that class. It represents the set of properties or methods that are common to all the objects of one type. It is a 
# blueprint/template for an object. E.g.:  Class of cars. Cars might have different names and brands but all shares some common properties like
# 4 wheels, speed, limit, fuel level, brakes, mileage range etc. Here, the class is "Car" and the wheels, speed, etc its properties.
# A class defines the structure and behaviour that its object will have. In python, classes are created using the 'class' keyword.


# In the below illustration, __init__(means initializing method because its objects data attributes), accelerate, and get_speed are methods 
# of the class Car (what we call variables in regular functions).
# They are have the method parameter variable called (self, make, model, color, speed). Now, remember that a 'method' operates on a specific 
# object data attributes.
# When a method is executed, it must have a way of knowing which objects data attributes it is suppose to operate on. hence, the use of the
# parameter 'self', when a method is called upon, the python makes the self parameter reference the specific object that the method is
# supposed to operate on.

# A Simple Car Illustration 
class Car:
    max_speed = 120

    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed
    
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed
    
    def get_speed(self):
        return self.speed
    
# To Instantiate two objects of the car class and ecah their characteristics
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")
# using the acceleration method, the speedof the car1 will be increased by 30km/h and car2 by 20km/h
car1.accelerate(30)
car2.accelerate(20)
# To display the cars currentspeed by utilizing the get_speed method.
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()}")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()}")