# CLASS: It is a user-defined data type, which consist of the data members and members functions, and can be accessed and used by creating 
# an instance of that class. It represents the set of properties or methods that are common to all the objects of one type. It is a 
# blueprint/template for an object. E.g.:  Class of cars. Cars might have different names and brands but all shares some common properties like
# 4 wheels, speed, limit, fuel level, brakes, mileage range etc. Here, the class is "Car" and the wheels, speed, etc its properties.
# A class defines the structure and behaviour that its object will have. In python, classes are created using the 'class' keyword.


# This illustration is used to define a class in python

# Our illustration blueprint is a 'speaker', you can use the blueprint to create multiple speakers. Each of these speaker that is created using
# the blueprint is an instance of the blueprint. Also, each speaker has its attributes such as color, model, and name. They will also have their
# methods showing a certain kind of behaviour such as volume up and volume down.

# To define a class, you have to use the 'class' keyword, provided in python, then followed by the name of the class and a colon:
# Just like in line 17

class ClassName:
    pass

# Using the above speaker illustration, we will create a class named 'speaker' in a file called 'define_speaker_class.py' and write our lines 
# of code.

class speaker:
    pass
speaker_one = speaker()
print(speaker_one)

#  In the above line 22, you have created a class called speaker without any attributes or methods. The keyword 'pass' does nothing and is
# usually used as a placeholder. In line24, you created an instance of the speaker class and assigned it to the variable 'speaker_one'. This 
# process is called INSTANTIATING AN OBJECT from a class. Line25 printed the 'speaker_one'. Now, running this code on the define_class.py
# in the terminal will print an output which is (<__main__.speaker object at 0x000002A47A56E890>). The following output shows the memory
# address where python stores the object on your computer. The memory address in your terminal output will be different from someone else.

# To create several more instances from the speaker class and they will be different from one another. To verify this, let's use the equality
# comparison (==) operator. In the define_class.py file, delete 'print(speaker_one)' and add the following to the bottom of your code.

speaker_two = speaker()

if speaker_one == speaker_two:
    print("speaker one is the same as speaker two")
else:
    print("speaker one is different from speaker two")

# If the above code is run, you will get the folowing output "speaker one is different from speaker two"

# CLASS AND INSTANCE ATTRIBUTES
# Here, i will be adding attributes to the 'speaker' class. Attributes being data stored within an object. While class attributes are common
# to all instances created from the class, instances attributes are unique to each instance. Adding attributes to the existing code, we have
# 'brand' is the class attribute with a value "Beatpill" assigned to it; while 'color' and 'model' are instances

class speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self.color = color
        self.model = model

# Class attributes are variables that belong to the class itself, rather than to individual instances of the class. The effect of class
# attributes is that all instances you create from your class will inherit and share that class attribute and it's value. In the above, every
# instance i create from 'speaker' class will share the same 'brand' value.
# Line 53 of my code defines an __init__ method, which takes in three parameters (self, color, and model). This method will be called anytime
# I create a new instance from 'speaker' class. The 'self' parameter is a reference to the 'speaker' class and it's a convention in python to
# always have it as the first parameter in a __init__ method. Line 54 and 55 set instance attributes, 'color' and 'model' to the 'speaker' class
# so, everytime i create a new instance from class, i have to provide arguments for 'color; and 'model' attributes. Not doing that will result
# in error. 

speaker_one = speaker("black", "85XB5")
speaker_two = speaker("red", "Y8F33")
print(f"Speaker one is {speaker_one.color} while speaker two is {speaker_two.color}")

# By adding the preceding code, I created two instances of the speaker class 'speaker_one' and 'speaker_two'. The arguments in each instance
# represent the values of their 'color; and 'model' attributes. I can now print a message that displays the color attributes of each object.
# When I run the above code my output will be "speaker one is black while speaker two is red". To see that both instances share the same brand
# class attributes, modify your print() function to this:

print(
    f"speaker one is {speaker_one.color} while speaker two is {speaker_two.color}",
    speaker_one.brand,
    speaker_two.brand,
    sep="\n",
)

# If the above code is run, the output will be "Beatpill" and "Beatpill"
# INSTANCE METHODS
# In addition to class and instance attributes, classes can also have methods AKA instance methods. They functions within a class that operate
# on instances of a class. To add instance to the existing code, do this;

class speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def power_on(self):
        print(f" Powering on {self.color} {self.model} speaker. ")

    def power_off(self):
        print(f"Powering off {self.color} {self.model} speaker. ")

speaker_one = speaker("black", "85XB5")
speaker_two = speaker("red", "Y8F33")

speaker_one.power_on()
speaker_two.power_off()

# In the above two instance method 'power_on()' and 'power_off()' have been added, just like the __init__ method, take 'self' as the first 
# argument. The power on prints a message indicating that the speaker of the given color is being powered on while the power_off does the 
# opposite. Line 103 and 104 was used to call the method

# ENCAPSULATION IN PYTHON
# Using the existing instance to encapsulate

class speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self._color = color
        self._model = model

    def power_on(self):
        print(f" Powering on {self._color} {self._model} speaker. ")

    def power_off(self):
        print(f"Powering off {self._color} {self._model} speaker. ")

    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        self._color = new_color

speaker_one = speaker("black", "85XB5")
speaker_one.power_on()

print(speaker_one.get_color())

speaker_one.set_color("white")
print(speaker_one.get_color())

# In the above, the 'color' and 'model' attributes are private attributes of the speaker class.

# Showing how INHERITANCE works on the above code, I will create another class "Smartspeaker" and make it inherit from the speaker class

class Smartspeaker(speaker):
    def __init__(self, color, model,voice_assistant):
        super().__init__(color, model)
        self._voice_assistant = voice_assistant
    
    def say_hello(self):
        print(f"Hello, I am {self._voice_assistant}")

# Creating an instance of the Smartspeaker class
smart_speaker = Smartspeaker("black", "XYZ123", "Alexa")
smart_speaker.power_on()
smart_speaker.say_hello()
# In the above code, the 'Smartspeaker' class is derived from the 'Speaker' class. The Smartspeaker class inherits the attributes and methods
# of the speaker class. The __init__ on 'Smartspeaker' calls the __init__ in 'speaker' ensuring it inherits its attributes (color, model) and 
# the smartspeaker's attribute 'voice_assistant' and new method 'say_hello'  was added. 
