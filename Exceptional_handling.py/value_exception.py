# Value error occurs when a word was used to replace a number, e.g. instead of the integar 20, the string twenty was inputed.

# Illustration one

#  It's assumed that the end-user of this code inputed pay rate in words instead of strings therefore value error will occur
def main():
    hours = int(input("How many hours did you work weekly? "))
    pay_rate = int(input("Enter your hourly pay rate: "))
    gross_pay = pay_rate*hours
    print('Gross pay: $', format(gross_pay, ', .2f', sep=''))

main()


# Illustration two

# The following illustration is meant to print a value error but the try and except statement has been used to prevent the error from printing.
def main():
    try:
        hours = int(input("How many hours did you work weekly:"))
        pay_rate = float(input("Enter your hourly pay rate:"))
        gross_pay = pay_rate*hours
        print(f'Gross pay: ${gross_pay}')

    except ValueError:
        print("Cannot work with string literals")
main()