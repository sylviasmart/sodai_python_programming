# using the for loop for set

myset = set()
names = ['Onyinye', 'Kunle', 'Bolawei', 'Peter']
myset.update(names)
for i in myset:
    print(i)
for a in myset:
    print(a)
print(len(myset))
print()

myset = {'Onyinye', 'Kunle', 'Bolawei', 'Peter'}
if 'kemi' in myset:
    print('kemi is an element of the set')
else:
    print('kemi is not part of the set')
print()

fruits = {'strawberry', 'kiwi', 'apple', 'mango'}
for a in fruits:
    print(a)

fruits = {'strawberry', 'kiwi', 'apple', 'mango'}
if 'kiwi' in fruits:
    print('kiwi is fruit contained in the fruit list')
else:
    print('kiwi is not a fruit contained in the fruit list')

# using the f'