# Handling multiple exceptions is used to correct more than one line of error in a function.
# Here, different lines of exception are written for different lines of codes where errors possibly occured.

# Illustration one
# Using a sales data for illustration

def main():
    total = 0.0
    try:
        infile = open('sales_data.txt', 'r')

        for line in infile:
            amount = float(line)
            total += amount

            infile.close()
            print(format(total, ',.2f'))

    except IOError:
        print('An error occured trying to read the file. ')

    except ValueError:
        print('Non-numeric data found in the file')

    except:
        print('An error occured')

main()