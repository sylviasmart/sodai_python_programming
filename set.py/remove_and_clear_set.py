# Remove is a function used to remove an elementfrom a set. It is represented as .remove()
names_of_facilitators = {'Izundu Ekeh',
                         'Igiran Bolowei',
                         'Esther Balogun',
                         'Alozie Sylvia'
                         }
new_names_of_facilitators = names_of_facilitators.remove('Alozie Sylvia')
print('new_names_of_facilitators set;', names_of_facilitators)
print()

subject_for_secondary = {'Maths', 'Biology', 'Chemistry', 'Physics', 'English', 'Data processing', 'Economics'}
List_of_subject_for_secondary = subject_for_secondary.remove('Maths')
print('List_of_subject_for_secondary;', subject_for_secondary)
print()


# Clear is a function used to clear all the contents of a set. It is represented as .clear()
subject_for_secondary = {'Maths', 'Biology', 'Chemistry', 'Physics', 'English', 'Data processing', 'Economics'}
List_of_subject_for_secondary = subject_for_secondary.clear()
print(subject_for_secondary)

print()
names_of_facilitators = {'Izundu Ekeh',
                         'Igiran Bolowei',
                         'Esther Balogun',
                         'Alozie Sylvia'
                         }
new_names_of_facilitators = names_of_facilitators.clear()
print(names_of_facilitators)