# Global variables are those variables defined outside a function and are accessible throughout the program. 


# Illustration one
# Global variables in function
feedback = ""

def fruits():
    global feedback
    print("inside function", feedback)
    feedback = "I love yummy fruits"
fruits()
print("outside function: ", feedback)
print()

# Illustration two
greeting = "Good"

def greeting_morning():
    morning = "Morning"
    print(greeting, morning)
def greeting_name(name):
    print(greeting, name)
greeting_morning()
greeting_name("Sylvia")
