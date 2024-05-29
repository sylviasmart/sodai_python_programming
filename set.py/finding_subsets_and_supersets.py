# This is used when in two sets, one is a subset of the other i.e. one set contains all the elements of the other.
# The set which its elements is contained in the other set is called the subset.It is represented using the symbol <=
# The set that contains all the elements of the other set is called the subset. It is represented using the symbol >=
# Subset and superset are more like booleans, except no figure return except true or false
# use the value variable since you are printing out booleans

set1 = set([1,2,3,4])
set2 = set([2,3])
value = set2.issubset(set1)
print(value)
value = set1.issuperset(set2)
print(value)
print()

fruit_hamper1 = {'watermelon', 'pineapple', 'pawpaw', 'mango', 'cashew', 'orange'}
fruit_hamper2 = {'mango', 'orange'}
new_fruit_hamper = fruit_hamper1.issuperset(fruit_hamper2)
new_fruit_hamper2 = fruit_hamper2.issubset(fruit_hamper1)
print(new_fruit_hamper)
print(new_fruit_hamper2)
print()

# To represent using the subset symbol <= and the superset symbol >=
set1 = set([1,2,3,4])
set2 = set([2,3])
value = set2<=(set1)
print(value)
value = set1>=(set2)
print(value)
print()

fruit_hamper1 = {'watermelon', 'pineapple', 'pawpaw', 'mango', 'cashew', 'orange'}
fruit_hamper2 = {'mango', 'orange'}
new_fruit_hamper = fruit_hamper1>=(fruit_hamper2)
new_fruit_hamper2 = fruit_hamper2<=(fruit_hamper1)
print(new_fruit_hamper)
print(new_fruit_hamper2)