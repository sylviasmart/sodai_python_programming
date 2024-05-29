# Concatenation is used to join or add two or more tuples together.
# It is represented using the plus (+) symbol

names = ('Ada', 'Obi', 'Kemi', 'Temi')
print('Length of names', len(names))
my_list = ('Ada', 'Obi', 'Kemi', 'Temi')
new_list = ('2024', 'Sylvia')
new_list = my_list + ('2024', 'Sylvia')
print('Length of new_list', len(new_list))

my_family = ('Daddy', 'Mummy', 'Second mummy', 'Brothers', 'Sisters')
print('Length of my_family', len(my_family))
extended_family = ('Uncles', 'Aunties', 'Nephews', 'Nieces', 'Relations', 'Relatives')
bossom_friends = ('childhood friends', 'university friends', 'NYSC friends', 'Church friends')
new_family = my_family + extended_family + bossom_friends
print('length of new_family', len(new_family))

paragraph_one = ('Nigeria is one of the most richest and blessed country in the continent "Africa".')
paragraph_two = (' She is blessed beyound measures with lots of minerals such as crude oil, limestone, coal.')
paragraph_three = (' She is located in the western part of African.')
paragraph_four = (' She is called "The Giant of Africa" by her co-african countries and by the world too.')
paragraph_five = (' She practice a democractic system of government since the year 1960.')
paragraph_six = (' She has many tribes like Igbo, Hausa, Yoruba, Efik, Ibibio, TIV, and lots more.')
paragraph_seven = (' She has thirty-six states inside of her, with about thousands of LGA.')
paragraph_eight = (' She is blessed to be close to the Atlantic ocean with crosses most of her states.')
paragraph_nine = (' She shares boarders with Ghana, Niger Delta, Garbon, Togo, Cameroon.')
paragraph_ten = (' Her people are known for farming, fishing, ranching, weaving of materials, shoe production, natural arts, and artifacts.')
paragraph_eleven = (' I can tell you more about this Great nation NIGERIA.')
paragraph_twelve = (' Feel free to reach out.')
About_Nigeria = paragraph_one + paragraph_two + paragraph_three + paragraph_four + paragraph_five + paragraph_six + paragraph_seven + paragraph_eight + paragraph_nine + paragraph_ten + paragraph_eleven + paragraph_twelve
print('length of About_Nigeria', len(About_Nigeria))
print(About_Nigeria)