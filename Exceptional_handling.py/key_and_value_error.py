# Key and value errors occurs when a key or value not existing in a function are being called upon.

# Illustration one
My_dict = {"name": "Sylvia", "age": 30}
value = My_dict["city"]
print(value)

# Illustration two
students = {
    "Sylvia": 27,
    "Peter": 30,
    "Seun": 27,
    "Pamela": 28,
    "Sey": 32,
    "Paulla": 22,
}
students["Sylvia"]
students["Paulla"]
students["Sey"]
students["Alma"]

# Note that when an error has been intercepted by any line of code with error the other lines following the line of code with error are
# automatically stopped from proceeding to run.

# Illustration three
info = input("What do you want to know about me? " )
             
My_dict = {"name": "Sylvia", "age": 30}
value = My_dict[f"{info}"]
print(value)

# The above illustration will print out an error if the enduser inputs an information not provided by the programmer, e.g. Address,
# complexion, height, etc. To fix this type of error use a try and except method (Corrected else exception clause)