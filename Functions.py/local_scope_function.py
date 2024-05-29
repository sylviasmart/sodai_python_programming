# Local scope in python are variables that are defined inside a function and their scope is limited to that function only.
# Local scope are accessible only inside the function in which it was initialized, i.e. it's not accessible outside the function.

# Local scope 
# Illustration one

def fruits():
    feedback = "I love yummy fruits"
    print(feedback)
fruits()
print()

def get_name():
    name = input("Enter your name:")

def main():
    name = "Kemi"
    get_name()
    print("Hello", name)

main()


# 
# Illustration two
def texas():
    birds = 5000
    print("Texas has", birds, "birds")

def california():
    birds = 8000
    print("California has", birds, "birds")

def main():
    texas()
    california()

main()