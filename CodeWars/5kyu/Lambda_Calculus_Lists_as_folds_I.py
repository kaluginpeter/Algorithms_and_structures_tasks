# In Lambda Calculus, lists can be represented as their right fold. A right fold wiki takes a combining function and an initial value, and returns a single combined value for the whole list, eg.:
#
# < x y z > = λ c n . c x (c y (c z n))
# in Python syntax:
#
# [ x, y, z ] = lambda c: lambda n: c(x)(c(y)(c(z)(n)))
# A list is not just the data in it; it also encapsulates operations on it. This representation encodes both a list's data and all possible operations on it, because any operation on a list can, with the right combining function and initial value, be expressed as a right fold ( even a left fold. but we're not going there .. today ).
#
# Booleans can be represented as a function that chooses between two arguments.
# Both these representations can be given type in System F wiki .
# This kata will use those encodings.
#
# Task
# Write functions cons and snoc. Both take an element and a list and return a new list with the element added to the list, in first and last position respectively.
#
# Write function map. It takes a transforming function and a list and returns a new list with every element transformed.
#
# Finally, write function filter. It takes a predicate and a list and returns a new, filtered list. ( A predicate is a function that takes a value and returns a Boolean. )
#
# You can define constants in Lambda Calculus syntax only: variables, function expressions, and function calls. Function expressions must use lambda notation ( lambda x: ). You can define and use helper constants. Recursion is not restricted.
#
# Preloaded
# # Church Booleans
# false    = lambda t: lambda f: f
# true     = lambda t: lambda f: t
#
# # constant: the empty list
# nil      = lambda c: lambda n: n
#
# # returns a Church Boolean indicating if a list is empty
# is_empty = lambda xs: xs (lambda _: lambda _: false) (true)
#
# # returns the first element of a non-empty list
# head     = lambda xs: xs (lambda x: lambda _: x) (None)
#
# # returns a non-empty list without its first element
# tail     = lambda xs: something quite clever
# Examples
# cons ( 1 ) ( nil )      =>  < 1 >
# cons ( 2 ) (< 1 >)      =>  < 2 1 >
# snoc ( 1 ) ( nil )      =>  < 1 >
# snoc ( 2 ) (< 1 >)      =>  < 1 2 >
# map (sqr) (< 1 2 >)     =>  < 1 4 >
# filter (odd) (< 1 2 >)  =>  < 1 >
# Notes
# get and set are definitely possible. Implementing those, however, means either using encoded numerals or dealing with numerical arithmetic and comparison operators, which is beyond the scope of this kata. For a real challenge, solve class List ( JS only ) using this encoding.
#
# Algorithms
# Solution
cons = lambda x: lambda xs: lambda c: lambda n: c(x)(xs(c)(n))

snoc = lambda x: lambda xs: xs(lambda y: lambda ys: lambda c: lambda n: c(y)(ys(c)(n)))(lambda c: lambda n: c(x)(n))

map = lambda f: lambda xs: xs(lambda x: lambda ys: lambda c: lambda n: c(f(x))(ys(c)(n)))(nil)

filter = lambda p: lambda xs: xs(lambda x: lambda ys:p(x)(lambda c: lambda n: c(x)(ys(c)(n)))(ys))(nil)