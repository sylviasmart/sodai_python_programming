# Add function is used to add new elements to a set. It done using the function .add() 
# Unlike in set we use .add(); while list does .append(). It looks similar

programming_languages = {'Python', 'HTML', 'Powerbi', 'C++', 'C', 'SQL'}
List_of_programming_languages = programming_languages.add('Javascript')
print(programming_languages)
print()

names_of_facilitators = {'Izundu Ekeh',
                         'Igiran Bolowei',
                         'Esther Balogun',
                         'Alozie Sylvia'
                         }
new_names_of_facilitators = names_of_facilitators.add('Peter Alozie')
print(names_of_facilitators)
print()

# To add items from another set into the current set, use the .update() and pass the to add set as argument or to add mutiple elements into an existing set
fruits_set = {"apple", "cherry", "banana"}
tropical_set = {"Pineapple", "mango", "pawpaw"}
fruits_set.update(tropical_set)
print(fruits_set)
print()

names_of_facilitators = {'Izundu Ekeh','Igiran Bolowei','Esther Balogun'}
names_of_students = {'Alozie Sylvia', 'Peter Alozie', 'Seun Dada', 'Onyinye'}
names_of_facilitators.update(names_of_students)
print(names_of_facilitators)
print()