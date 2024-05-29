# using in operators in set

myset = set()
names = ['Onyinye', 'Kunle', 'Bolawei', 'Peter']
myset.update(names)
print(myset)
print('kemi' in myset)
print('kunle' in myset)
print('Kunle' in names)
# or
val = "kunle" in myset
print(val)

print()
fruits = {'strawberry', 'kiwi', 'apple', 'mango'}
for a in fruits:
    print(a)
print('apple' in fruits)
print('watermelon' in fruits)
print('kiwi' in fruits)

# using the not in operators in set
myset = set()
names = ['Onyinye', 'Kunle', 'Bolawei', 'Peter']
myset.update(names)
print(myset)
print('kemi' not in myset)
print('kunle' not in myset)
# or
val = "kunle" not in myset
print(val)

print()
fruits = {'strawberry', 'kiwi', 'apple', 'mango'}
for a in fruits:
    print(a)
print('pineapple' not in fruits)
print('strawberry' not in fruits)
print('kiwi' not in fruits)