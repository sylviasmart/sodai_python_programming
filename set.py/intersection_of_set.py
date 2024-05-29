# This is used to find the similarities between two sets i.e. what two sets share in common. 
# it can also be represente with symbol &

set1 = set([1,3,5,7])
set2 = set([2,3,4,5])
set3 = set1.intersection(set2)
print(set3)
print()
fruit_hamper1 = {'watermelon', 'pineapple', 'pawpaw', 'mango'}
fruit_hamper2 = {'cashew', 'mango', 'orange', 'pawpaw'}
new_fruit_hamper = fruit_hamper1.intersection(fruit_hamper2)
new_fruit_hamper2 = fruit_hamper2.intersection(fruit_hamper1)
print(new_fruit_hamper)
print(new_fruit_hamper2)
print()

# To represent using the symbol Amperstand (&)
set1 = set([1,3,5,7])
set2 = set([2,3,4,5])
set3 = set1&(set2)
print(set3)
print()
fruit_hamper1 = {'watermelon', 'pineapple', 'pawpaw', 'mango'}
fruit_hamper2 = {'cashew', 'mango', 'orange', 'pawpaw'}
new_fruit_hamper = fruit_hamper1&(fruit_hamper2)
new_fruit_hamper2 = fruit_hamper2&(fruit_hamper1)
print(new_fruit_hamper)
print(new_fruit_hamper2)