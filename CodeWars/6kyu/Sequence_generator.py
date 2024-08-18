# Write a generator sequence_gen ( sequenceGen in JavaScript) that, given the first terms of a sequence will generate a (potentially) infinite amount of terms, where each subsequent term is the sum of the previous x terms where x is the amount of initial arguments (examples of such sequences are the Fibonacci, Tribonacci and Lucas number sequences).
#
# ##Examples
#
# fib = sequence_gen(0, 1)
# next(fib) = 0 # first term (provided)
# next(fib) = 1 # second term (provided)
# next(fib) = 1 # third term (sum of first and second terms)
# next(fib) = 2 # fourth term (sum of second and third terms)
# next(fib) = 3 # fifth term (sum of third and fourth terms)
# next(fib) = 5 # sixth term (sum of fourth and fifth terms)
# next(fib) = 8 # seventh term (sum of fifth and sixth terms)
#
# trib = sequence_gen(0,1,1)
# next(trib) = 0 # first term (provided)
# next(trib) = 1 # second term (provided)
# next(trib) = 1 # third term (provided)
# next(trib) = 2 # fourth term (sum of first, second and third terms)
# next(trib) = 4 # fifth term (sum of second, third and fourth terms)
# next(trib) = 7 # sixth term (sum of third, fourth and fifth terms)
#
# lucas = sequence_gen(2,1)
# [next(lucas) for _ in range(10)] = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
# Note: You can assume you will get at least one argument and any arguments given will be valid (positive or negative integers) so no error checking is needed.
#
# **Note for Ruby users: ** sequence_gen should return an Enumerator object.
#
# Any feedback/suggestions would much appreciated.
#
# FUNDAMENTALS
# Solution
def sequence_gen(*args):
    l = list(args)
    while True:
        yield l[0]
        l = l[1:] + [sum(l)]