import random


class Student:

    def __init__(self, age =16, name=None, reg_num=000, grade = 'SQL'):
        self.age = age
        self.name = name
        self.reg_num = reg_num
        self.grade = grade

    def add_age(self):
        self.age = self.age + 1
    
    def change_grade(self, grade='SQL'):
        self.grade = grade

names = ["Onyi", "Sylvia", "Kemi", "Seun", "Bolowei", "Izu"]
reg_nums = [111, 333, 222, 888, 777, 999, 444, 555, 666]
grades = ["PowerBI", "SQL", "Excel", "Tableau", "Python","Google sheets"]

students = []

for _ in range(100):
    age = random.randint(18,50)
    name = random.choice(names)
    reg_num = random.choice(reg_nums)
    grade = random.choice(grades)

    st = Student(age=age, name=names, reg_num=reg_nums, grade=grades)
    students.append(st)

print(len(students))


for i in students:
    print(i.name, i.age, i.reg_num, i.grade, sep=';')
