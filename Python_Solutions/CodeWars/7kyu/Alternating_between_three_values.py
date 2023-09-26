# Alternating Among Three Values
# Suppose a variable x can have only three possible different values a, b and c, and you wish to assign to x the value other than its current one, and you wish your code to be independent of the values of a, b and c.
#
# What is the most efficient way to cycle among three values? Write a function f so that it satisfies
#
#   f(a) = b
#   f(b) = c
#   f(c) = a
# EXAMPLE
#   f(10, a=10, b=20, c=100) -> 20
#   f(20, a=10, b=20, c=100) -> 100
#   f(100, a=10, b=20, c=100) -> 10
# FUNDAMENTALS
# Solution
def f(x, a, b, c):
    return {a: b, b: c, c: a}[x]