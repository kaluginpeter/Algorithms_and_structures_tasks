# You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.
#
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.
#
# if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
#
# Example:
# calculator(1, 2, '+') => 3
# calculator(1, 2, '$') # result will be "unknown value"
# Good luck!
#
# FUNDAMENTALS
# Solution
def calculator(x,y,op):
    if type(x) == int and type(y) == int:
        dict_op = {'+': x+y, '-': x-y, '*': x*y, '/': x/y}
        if op in dict_op and x !=0 and y !=0:
            return dict_op[op]
        else:
            return 'unknown value'
    return 'unknown value'