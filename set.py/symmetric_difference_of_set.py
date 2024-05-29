# This is used when two sets contain elements that are not shared by both sets.
# Here, all the contents of certain set (e.g. setA) that is not in the other set (setB), are joined together
# Symmetric difference of set does not include the intersection in both sets been compared.
# It is represented using the delta symbol ^

set1 = set([1,3,5,7])
set2 = set([2,3,4,5])
set3 = set1.symmetric_difference(set2)
print(set3)
print()

fruit_hamper1 = {'watermelon', 'pineapple', 'pawpaw', 'mango'}
fruit_hamper2 = {'cashew', 'mango', 'orange', 'pawpaw'}
new_fruit_hamper = fruit_hamper1.symmetric_difference(fruit_hamper2)
print(new_fruit_hamper)
print()

# To represent using the delta symbol ^
set1 = set([1,3,5,7])
set2 = set([2,3,4,5])
set3 = set1^(set2)
print(set3)
print()

fruit_hamper1 = {'watermelon', 'pineapple', 'pawpaw', 'mango'}
fruit_hamper2 = {'cashew', 'mango', 'orange', 'pawpaw'}
new_fruit_hamper = fruit_hamper1^(fruit_hamper2)
print(new_fruit_hamper)