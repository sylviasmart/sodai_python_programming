# This is use to combine mutiple set values together. it can also be denoted with the symbol |

set1 = set()
names = ['Onyinye', 'Kunle', 'Bolewei', 'Peter']
set1.update(names)
print(set1)
print()
set2 = set()
numbers = [1,2,3,4]
set2.update(numbers)
print(set2)
print()
set3 = set1.union(set2)
set4 = set2.union(set1)
print(set3)
print(set4)

print()
# using the pipe symbol which also represents the union
set1 = set()
names = ['Onyinye', 'Kunle', 'Bolewei', 'Peter']
set1.update(names)
print(set1)
print()
set2 = set()
numbers = [1,2,3,4]
set2.update(numbers)
print(set2)
print()
set3 = set1|(set2)
set4 = set2|(set1)
print(set3)
print(set4)