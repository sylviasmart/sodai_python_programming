# The try/except statement may have an optional else clause, which appears after all the except clauses.

# Illustration one
def main():
    total = 0.0

    try:
        in_file = open('sales_data.txt', 'r')

        for line in in_file:
            amount = float(line)
            total =+ amount

            in_file.close()
    except Exception as err:
        print(err)
    else:
        print(format(total, ',.2f'))
main()

# Illustration two carried from key and value error

info = input("What do you want to know about me? " )
             
My_dict = {"name": "Sylvia", "age": 30}

try:
    value = My_dict[f"{info}"]
    print(value)
except KeyError:
    print("I do not have that info!")
