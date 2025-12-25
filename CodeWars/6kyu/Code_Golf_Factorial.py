# This is a code golf kata where the goal is to write the shortest program that computes the factorial of a non-negative integer n.
#
# where:
# The factorial of n is defined as:
#
# n! = n * (n - 1)! for n > 0
# 0! = 1
# Constraints:
# The program must calculate the factorial for integers n in the range of 0 to 500 (inclusive).
#
# The code length must not reach 30 characters.
#
# You are not allowed to use any form of if, else, elif, or similar conditional statements
#
# No built-in libraries that compute the factorial (e.g., eval or math.factorial) can be used.
#
#
# For the mathematical formula of factorial and more details on its properties, you can refer to Factorial.
#
# The program should be concise and efficient, adhering to the above constraints while correctly calculating factorials.
#
# Good luck!
#
# MathematicsAlgorithmsRestricted
# Solution
f=lambda n:n and n*f(n-1)or 1