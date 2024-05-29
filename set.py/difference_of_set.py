# This is used to remove an element from a set that is not contained in the comparing set. 
# It is also been represented with minus symbol -

set1 = set([1,3,5,7])
set2 = set([2,3,4,5])
set3 = set1.difference(set2)
print(set3)
set4 = set2.difference(set1)
print(set4)
print()
fruit_hamper1 = {'watermelon', 'pineapple', 'pawpaw', 'mango'}
fruit_hamper2 = {'cashew', 'mango', 'orange', 'pawpaw'}
new_fruit_hamper = fruit_hamper1.difference(fruit_hamper2)
new_fruit_hamper2 = fruit_hamper2.difference(fruit_hamper1)
print(new_fruit_hamper)
print(new_fruit_hamper2)
print()

# To represent using the minus symbol - 
set1 = set([1,3,5,7])
set2 = set([2,3,4,5])
set3 = set1-(set2)
print(set3)
set4 = set2-(set1)
print(set4)
print()
fruit_hamper1 = {'watermelon', 'pineapple', 'pawpaw', 'mango'}
fruit_hamper2 = {'cashew', 'mango', 'orange', 'pawpaw'}
new_fruit_hamper = fruit_hamper1-(fruit_hamper2)
new_fruit_hamper2 = fruit_hamper2-(fruit_hamper1)
print(new_fruit_hamper)
print(new_fruit_hamper2)