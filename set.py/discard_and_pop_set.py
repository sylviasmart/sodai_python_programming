# To remove a specific element that never existed and not get an error when you print the output
# while you code remains unchanged, use the function .discard()

programming_languages = {'Python', 'HTML', 'Powerbi', 'C++', 'C', 'SQL'}
List_of_programming_languages = programming_languages.discard('Python')
print(programming_languages)
print()

# shows illustration with a non-existing element
programming_languages = {'Python', 'HTML', 'Powerbi', 'C++', 'C', 'SQL'}
List_of_programming_languages = programming_languages.discard('Javascript')
print(programming_languages)
print()

# The pop function is used to remove random elements from a set .pop()
# Pop is barely used since you do not know the element it will decide to remove
programming_languages = {'Python', 'HTML', 'Powerbi', 'C++', 'C', 'SQL'}
a = programming_languages.pop()
print(a)
print(programming_languages)

letters = {'a', 'b', 'c', 'd'}
print(letters)
letters.pop()
print(letters)