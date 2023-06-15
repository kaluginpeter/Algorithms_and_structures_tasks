# The function 'fibonacci' should return an array of fibonacci numbers.
# The function takes a number as an argument to decide how many no. of elements to produce.
# If the argument is less than or equal to 0 then return empty array
#
# Example:
#
# fibonacci(4) # should return  [0,1,1,2]
# fibonacci(-1) # should return []
# ALGORITHMS
# Solution
def fibonacci(n):
    l = []
    a, b = 0, 1
    for i in range(n):
        l.append(a)
        a, b = b, a + b
    return l if n > 0 else []