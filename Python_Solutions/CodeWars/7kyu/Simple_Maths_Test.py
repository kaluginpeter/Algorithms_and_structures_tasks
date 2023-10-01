# Create a function which checks a number for three different properties.
#
# is the number prime?
# is the number even?
# is the number a multiple of 10?
# Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses data Property.
#
# Examples
# number_property(7)  # ==> [true,  false, false]
# number_property(10) # ==> [false, true,  true]
# The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:
#
# number_property(-7)  # ==> [false, false, false]
# number_property(-10) # ==> [false, true,  true]
# ALGORITHMSMATHEMATICS
# Solution
def number_property(n):
    is_prime = lambda i: False if i <= 1 else all([1 if n % i != 0 else 0 for i in range(2, int(n ** 0.5 + 1))])
    is_even = lambda x: x%2 == 0
    is_mult_10 = lambda x: x%10 == 0
    return [is_prime(n), is_even(n), is_mult_10(n)]