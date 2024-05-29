# To split strings the .split() function is used. 

#spliting strings
my_string = 'One Two Three Four'
word_list = my_string.split()
print(word_list)
print(word_list[1])
print(word_list[-1])

days = 'Monday Tuesday Wednesday'
new_days = days.split(  )
print(days)
print(new_days)
days2 = 'Monday/Tuesday/Wednesday'
new_days = days2.split('/')
print(days)
print(new_days)

days = 'Monday#Tuesday#Wednesday'
print(days.split('#'))

values = 'One$ Two$ Three$ Four'
new_values = values.split("$ ")
print(values)
print(new_values)

days = 'Monday Tuesday Wednesday'
print(days.split(' '))