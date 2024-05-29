# Indexing is defined as the process of specifically finding out the position of characters individually in a string or another format.
# Indexing starts with the number 0 when counting from the left side or the starting point of the content to be checked while counting
# from the right side or the ending point you count from -1. The act of indexing strings is known as "Slicing a string"


# Illustration one
Address = '125 Adebayo Oduntayo, Ifedayo Estate, Ajuwon, Alagbole, Ojudu, Ogun State'
# To extract Ogun state
print(Address[-11:])
print(Address[0:20])
print(Address[38:54])
print()

# Illustration two
My_interest = ('Going hiking on mountain tops'), ('Swimming in pools or lakes'), ('Crocheting or knitting with wool and yawn')
random_sentence = (1, 'five'), ("pop", "rock"), (100, 50), ("White", "Black", "Brown")
print(My_interest[0])
print(My_interest[2])
print(My_interest[1][11:17])
print()

print(random_sentence[3])
print(random_sentence[1])
print(random_sentence[2][0])
print(random_sentence[0][1])
print(random_sentence[0][1][-2:])