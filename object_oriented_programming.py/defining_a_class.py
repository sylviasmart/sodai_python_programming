# In python, you can create classes using the 'class' keyword.

# CREATING CLASS: When a class is created, specifty the 'attributes9data' and 'mthods(functions)' that objects of that class will have.
# For instance, a 'Car' class with attributes such as color, and speed, etc. along with methods like accelerate, etc.
# Object in python can be tangible (like a car) or abstract (like a childs grade). It posses two mian xteristics which are state & behaviour
# State describes the object xteristics while behavioris the action or method that the object can perform. Here. methods are function that belong
# to objects and can change the object's state or perform specific operation.

# INSTANTIATING OBJECTS: Once a class have been defined, an individual objects(instances) based on that class is created. Each object is 
# independent and has its own set of attributes and methods. To create an object, use the class name followed by a parenthesis.

# INTERACTING WITH OBJECTS: Objects are interacted with by calling their methods or accessing their attributes using dot notation. For instance,
# Hair object name my_hair, you can set its color with =====> my_hair.color = 'Orange' and curl the hair with my_hair.curly(), if there's a curly
# method defined in the class.

# STRUCTURE OF CLASSES
# Class declaration (class ClassName); The 'class' keyword is sued to declare a class in python; 'ClassName' is the name of the class,
# typically following Camelcase nameing conventions. 
# =============>  class ClassName:

# CLASS ATTRIBUTES: They are variables shared among all class instances(objects); They are defined within the class but outside of any methods
# class ClassName:
#     class_attribute = value

# CONSTRUCTOR METHOD: The __init__ method is a special method known as the constructor;. It initializes the instance attributes (also called
# instance variables) when an object is created;. The 'self' parameter is the first parameter of the constructor, referring to the instance
# being created;. 'attribute1' and 'attribute2', and so on are parameters passed to the constructor when creating an object;. Inside the
# constructor, 'self.attribute1', 'self.attribute2' and so on are used to assign values to instance attributes.

# class ClassName:
#     class_attribute = Value

#     def __init__(self, attribute1, attribute2,....):
#         pass

# INSTANCE ATTRIBUTES: They are variables that store data specifically to each class instance;. They are initialized within the __init__
# method using the self keyword followed by the attribute name;. These attributes hold unique data for each object created from the class

# class ClassName:
#     class_attribute = Value

#     def __init__(self, attribute1, attribute2,....):
#     self.attribute1 = attribute1
#     self.attribute2 = attribute2

# INSTANCE METHODS: They are functions defined within the class;. They operate on the instance's data (instance attributes) and can perform
# actions specific to instances. The 'self' parameter is required in instance methods, allowing them to access instance attributes and call
# other methods within the class.

# class ClassName:
#     class_attribute = Value

#     def __init__(self, attribute1, attribute2,....):
#           self.attribute1 = attribute1
#           self.attribute2 = attribute2

# instance methods

    # def method1(self, parameter1, parameter2,....):
    #     pass

# Using the same steps you can define multiple instance methods

#     class_attribute = Value

#     def __init__(self, attribute1, attribute2,....):
#           self.attribute1 = attribute1
#           self.attribute2 = attribute2
    # def method1(self, parameter1, parameter2,....):
    #     pass
    # def method2(self, parameter1, parameter2,....):
    #     pass

# CREATING OBJECT(INSTANCES): To createobject(instances) of the class, call theclass like a function and provide arguments the
# constructor requires;. Each object is a distinct instance of the class, with its own instance attributes and the ability to call
# methods defined in the class.
# object1 = ClassName(arg1, arg2,...)
# object2 = ClassName(arg1, arg2,...)

# CALLING METHODS ON OBJECTS USING DOT NOTATION: The methods 'method1' and 'method2' are defined in the ClassName class, and calling them on
# 'object1' and 'object2' respectively;. Pass values 'parameter1_value' and 'parameter2_value' are arguments to these methods. These arguments
# are used within the method's logic. To achieve this, use the dot notation =====> object.method() to invoke the method on the object directly.
# result1 = object1.method1(parameter1_value, parameter2_value,...) ====> Here, we call method1 on object1.

# ACCESSING OBJECT ATTRIBUTES: Here, accessing an object's attribute is done using dot notation ==> attribute_value = object1.attribute1 
# retrives the value of the attribute 'attribute1' from 'object1' and assigns it to the variable 'attribute_value'.

# attribute_value = object1.attribute1

# MODIFYING OBJECT ATTRIBUTES: WE modify an object's attribute using dot notation ====> object1.attribute2 = new_value sets the attribute
# 'attribute2' of 'object1' to the new value 'new_value'

# ACCESSING CLASS ATTRIBUTES (SHARED BY ALL INSTANCES): Finally, access a class attribut shared by all class instances

# class_attribute_value = ClassName. class_attribute

# accesses the class attribute 'class_attribute' from the ClassName class and assigns its value to the variable 'class_attribute_value'
