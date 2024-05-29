# Index errors occurs when python interpreter is instructed to print a line of index that does not exist.

# The below illustration contains a variable with three elements and there indexing are as follows
        #   0      1    2    3
variable = [123, 200, 1000, 25]

variable[0]
variable[1]
variable[3]
variable[4]

# This error on line 10 is because the variable[4] does not have any allocation of an elements in it