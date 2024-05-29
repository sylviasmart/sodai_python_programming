# The try/except statement may have an optional finally clause, which must appear after the except clauses.
# The statements in the finally statement execute whether an exception occurs or not. Its purpose is to perform cleanup operations...
# .. such as closing files or other resources. Any code on the finally statement executes even when there is an exception on the try suite.


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
    finally:
        print(format(total, ',.2f'))
main()