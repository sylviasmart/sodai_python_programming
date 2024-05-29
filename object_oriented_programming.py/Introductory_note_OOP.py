# Object oriented programming is a popular programming style in many languages such as python, C++, Javascript, SQL, C, PowerBI, Excel, etc.
# It is a programming paradigm that revolves around the concept of objects, which can contain data (attributes or properties) and code 
# (methods or functions). It is a popular approach used for organizing and designing software due to its modularity, reuseability, and 
# maintainability.

# OOP aims to implement real-world entities like inheritance, hiding, polymorphism, etc in programming. The main aim of OOP is binding together
# the data and the functions that operate on them so that no other part of the code can access this data except that function.

# The types of OOP
# CLASS: It is a user-defined data type, which consist of the data members and members functions, and can be accessed and used by creating 
# an instance of that class. It represents the set of properties or methods that are common to all the objects of one type. It is a 
# blueprint for an object. E.g.:  Class of cars. Cars might have different names and brands but all shares some common properties like
# 4 wheels, speed, limit, mileage range etc. Here, the class is "Car" and the wheels, speed, etc its properties.

# OBJECT: It is a basic unit of OOP and represents the real-life entities. An object is an instance of a class. When a class is defined,
# no memory is allocated but when it is instantiated (i.e. an object is created) memory is allocated. Object has an identity, state, and
# behaviour. The IDENTITY is what the class is known as; STATE is the attributes or data that describe the object; BEHAVIOUR is the actions
# or methods that the objects can perform.
# They contain data and code to manipulate data. They can interact without having to know details of each others data or code,
# it is sufficient to know the type of message accepted and type of response returned by the objects. E.g.: "Dog" is a real-life object;
# which has some xteristics like colour, age, breed; bark, sleep, and eat.

# METHODS: They are similar to functions but are also classified according to their purpose in the class design. It accepts parameters as
# arguments, manipulates these, and then produces an output when the method is called on an object. Methods often operates on attributes.
# 

# ATTRIBUTES: They are data members inside a class or object that represent the different features of the class, they are also being refered to
# as characteristics of the class that can be accessed from other objects or differentiate a class from other classes. E.g A car attribute
# includes; tyre, seats, doors, license plate, wheel, handle, make, headlight, year, etc.


# The four pillars of OOP
# DATA ABSTRACTION: It is one of the most important and essential features of OOP. This refers to providing only essential information about
# the data to the outside world, hiding the background details or implementation. E.g: A man driving a car. He knows that pressing the 
# accelerator will increase the speed of the car or applying brakes will stop the car; but he does know how on pressing the accelerator the
# speed is increasing or about the inner mechanism of the car or the implementation of the accelerator, brakes, etc in the car.

# ENCAPSULATION: It is the wrapping up of data under a single unit. it is the mechanism that binds together code and the data it manipulates.
# Here, the variables or data of a class are hidden from any other class and can be accessed only through any memebr function of their class in
# which they are declared. It is also known as Data hiding. E.g: In real-life example, A company that has different sectors like accounts,
# sales, finance sector. The finance sector handles all financial transaction and keeps all the data relate to it; same way the sales sector,
# handles all the sales related actitities and keeps its records. It a situation arises and for some reason a finance official needs the data
# from the sales sector in a particular month; he is not allowed to directly access those data or information but instead he will go through
# an official in the sales sector and request such information. Here, all sectors are solely responsible for their data. Note that, it heavily
# dependent on abstraction to function.

# INHERITANCE: It is an important pillar of OOP. It is the capability of a class to derive properties and xteristics from another class.
# Here, when we write a class, we inherit properties from other classes; we do not need to write all the properties and functions again and
# again, as these can be inherited from another class that possess it. Inheritance allows the user to reuse the code whenever possible and 
# reduce its redundancy.

# POLYMORPHISM: This word means "Having different forms". It is further defined as the ability of a message to be displayed in more than one
# form. E.g: An individual can have different xteristics. Like a man at the same time is a father, a husband, an employee. So the same person
# possess different behaviour in different situation. Polymorphism allows 'subclass' to have methods with the same names as methods in their
# 'superclasses'. It gives the ability for a progran to call the correct method depending on the type of object that is used to call it.
# Furthermore, Polymorphism occurs when objects changes their behaviour based on the class they derive from. This usually occurs when objects
# belongs to the same inheritanc tree and the child's method are overloading their parents.

# DYNAMIC BINDING: Here, a code to be executed in response to the functiom call is declined at runtime. DB means that the code associated with
# a given procedure call is not known until the time of the call at run time. DB is one of the main advantages of inheritance is that some
# derived class "D" has all the members of its base class "B". Once D is not hiding any of the public members of B in any context where a B
# could be used. It is also known as a subtype polymorphism.

# MESSAGE PASSING: It is a form of communication used in OOP as well as parallel programming. Objects communicate with one another by
# sending and recieving information to each other. A message for an object is a request for execution of a procedure and therefore will
# invoke a function in the recieving object that generates the desired result. It involves specifying the name of the object, the name of
# the function and the the information to be sent.


# CLASSES AND OBJECTS
# METHODS: They are functions defined within a class that define the behaviour of objects. They can perform various operations, 
# manipulate data, and interact with other objects.

# PROPERTIES: It is also known as attributes or fields. They are data members of a class. They store the xteristics or data assocaited with
# an object.

# CLASS DECLARATION: Classes are declared using the class keyword followed by the class name and a block of attributes and methods.

# OBJECT INSTANTIATION: Objects are created using the class constructor. Each object occupies its own memory space and can access class
# methods and attributes.