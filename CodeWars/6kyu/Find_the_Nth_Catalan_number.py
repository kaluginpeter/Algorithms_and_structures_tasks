# What is a Catalan number?
# In combinatorial mathematics, the Catalan numbers form a sequence of natural
# numbers that occur in various counting problems, often involving recursively-defined objects.
# They are named after the Belgian mathematician Eugène Charles Catalan (1814–1894).
#
# Using zero-based numbering, the nth Catalan number is given directly in terms of binomial coefficients by:
#
#
# You can read more on Catalan numbers Here.
#
# Task:
# Implement a function which calculates the Nth Catalan number.
#
# 0  =>  1
# 3  =>  5
# 7  =>  429
# 9  =>  4862
# Hint: avoid the use of floats
#
# Have fun :)
#
# BIG INTEGERSALGORITHMSMATHEMATICS
# Solution
import math
def nth_catalan_number(n):
    return math.factorial(2*n) // math.factorial(n+1) // math.factorial(n)