# Write a function that finds the sum of all its arguments.
#
# eg:
#
# sum_args(1, 2, 3) # => 6
# sum_args(8, 2) # => 10
# sum_args(1, 2, 3, 4, 5) # => 15
# TIPS:
# ruby/python : http://lmgtfy.com/?q=Ruby+splat+operator
#
# JS/Coffeescript : http://lmgtfy.com/?q=Javascript+arguments+variable
#
# C: https://www.geeksforgeeks.org/variadic-functions-in-c/
#
# FUNDAMENTALS
# Solution
def sum_args(*args):
    return sum([*args])