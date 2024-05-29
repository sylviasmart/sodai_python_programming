# The display file error or exception occurs when a user enters the name of a file that is not existing. 
# The end result of the code will be to display the contents of a file or folder being called upon.

# Illustration one
def main():
    filename = input('Enter the filename: ')
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
main()

# The above illustration prints out an output "No such file or directory" meaning that the user must have inputed a file that does not exist.


# Illustration two
# The above illustration can be modified using try/except statement that gracefully responds to an IOError exception.

def main():
    try:
        filename = input('Enter the filename: ')
        infile = open(filename, 'r')
        contents = infile.read()
        print(contents)
        infile.close()
    except IOError:
        print('An error occurred trying to read')
        print('the file', filename)

main()