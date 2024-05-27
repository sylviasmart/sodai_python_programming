# EXPRESSION AND VARIABLES
# EXPRESSION: This is the combination of numbers, symbols, and other variables that produce a result when evaluated. In the below, illustration,
# I assigned a value 20 to the base variable and value 10 to the height variable and then assign the expression result to the area variable,and 
# use the print function to display the area of the traingle.

base = 20
height = 10
area = ((base*height)/2)
print(area)

# VARIABLES: They are names that we give to certain values in our program. When we create a variable in a code the computer reserves a chunk of
# memory to store that value. The process of storing a value in a variable is called an assisignment.


# Illustration one
salary = float(input("Enter salary: "))
bonus = float(input("Enter bonus: "))
pay = salary + bonus
print(pay)

# Illustration two
workmanship = float(input("Enter workmanship: "))
expenses_for_materials = float(input("Enter expenses for materials: "))
transportaion_and_logistics = float(input("Enter transportation and logistics: "))
risk_allowances = float(input("enter risk allowances: "))
pay = workmanship - expenses_for_materials - transportaion_and_logistics + risk_allowances
print(pay)

# Illustration three
salary = float(input("Enter salary: "))
feeding = float(input("Enter feeding allowances: "))
leave_benefits = float(input("Enter leave benefits:"))
pay = salary + feeding + leave_benefits
print(pay)

