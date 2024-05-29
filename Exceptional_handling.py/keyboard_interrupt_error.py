# This error only occurs when a code is running and was abruptly becuase the programme interrupted the smooth
# running of the code.

# Illustration one

for _ in range(500000):
    print('%')

# The above lines of code has instructed python interpreter to print '%' into 500,000(Five hundred thousand) pieces, so in the process of which
#  the code is still running on the terminal and the user interprets it by using the command Ctrl + c,
# The error massage "Keyboard interrupt error" will be printed.