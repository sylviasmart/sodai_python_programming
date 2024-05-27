# Dictionaries is a data type in python programming. It contains items, elements, and members.
# It is a compound data type and is represented using curly brackets {}.
# It is made of a key word and a value (which can either be a meaning or number).
# The keys must be immutable and unique; while numbers can be immutable, mutable, and duplicates.

# Illustration one
students = {
    'Nkechi':80,
    'Seun': 89,
    'Seun Dada': 90,
    'Amarachi': 50,
}
print(students)
# In the above the names serves as the key; while the number serves as values.
print()

# Illustraion two
dict = {
    'key1':1, 
    'key2': 2, 
    'key3': [3, 2, 1], 
    'key4': (True, 4, 'Ayo')
    }
print(dict)
print()

# Illustration three
students = {'Ama':10, 'Jide':20, 'Tony':30, 'Seun':40, 'Bashiru':50, 'Ayo':60, 'Sylvia':70}
print(students)
for i in students.items():
    print(i)

for x in students.keys():
    print(x)

for b in students.values():
    print(b)
print(students.values())
print(students['Sylvia'])
print(students)
print(range(len(students)))
print()
