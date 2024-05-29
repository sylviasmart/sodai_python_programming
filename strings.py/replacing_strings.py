# To replace an element or elements from what it contains previously, the .replace() is used to run function.
# Here, you are change an element(s) of a string to something different

#replacing strings

string_variable = 'Four score and seven years ago'
new_string_variable = string_variable.replace('years', 'days')
print(new_string_variable)
new_string_variable = string_variable.replace('years', 'century').replace('four', 'ten').replace('score', 'decades')
print(new_string_variable)
print()

names_var = 'Sylvia accuracy in python programming is topnotch, give accolades to Izu'
new_names_var = names_var.replace('Sylvia', 'Amarachi').replace('python', 'snake').replace('Izu','Izundu').replace('topnotch', 'execellent')
print(new_names_var)