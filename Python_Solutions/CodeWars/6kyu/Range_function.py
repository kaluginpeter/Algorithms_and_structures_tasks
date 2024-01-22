# Create range generator function that will take up to 3 parameters - start value, step and stop value. This function should return an iterable object with numbers. For simplicity, assume all parameters to be positive numbers.
#
# Examples:
#
# range(5) --> 1,2,3,4,5
# range(3, 7) --> 3,4,5,6,7
# range(2, 3, 15) --> 2,5,8,11,14
# FUNDAMENTALS
# Solution
def range_function(*args):
    if len(args) == 1:
        return range(1, args[0] + 1)
    elif len(args) == 2:
        return range(args[0], args[1] + 1)
    return range(args[0], args[2] + 1, args[1])