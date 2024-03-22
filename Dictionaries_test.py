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