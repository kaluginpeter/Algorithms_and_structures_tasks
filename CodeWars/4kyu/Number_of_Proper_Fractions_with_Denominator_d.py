# If n is the numerator and d the denominator of a fraction, that fraction is defined a (reduced) proper fraction if and only if GCD(n, d) = 1.
#
# For example 5/16 is a proper fraction, while 6/16 is not, as both 6 and 16 are divisible by 2, thus the fraction can be reduced to 3/8.
#
# Now, if you consider a given number d, how many proper fractions can be built using d as a denominator?
#
# For example, let's assume that d is 15: you can build a total of 8 different proper fractions between 0 and 1 with it: 1/15, 2/15, 4/15, 7/15, 8/15, 11/15, 13/15 and 14/15.
#
# You are to write a function that computes how many proper fractions you can build with a given denominator:
#
# 1 --> 0
# 2 --> 1
# 5 --> 4
# 15 --> 8
# 25 --> 20
# Be ready to handle big numbers.
#
# Edit: to be extra precise, the term should be "reduced" fractions, thanks to girianshiido for pointing this out and sorry for the use of an improper word :)
#
# FundamentalsMathematics
# Solution
def proper_fractions(n):
    if n == 1: return 0
    temp = 1
    m = n
    l = int(n ** 0.5) + 1
    for i in range(1, l):
        if is_prime(i):
            if m % i == 0:
                temp *= i - 1
                m /= i
            while m % i == 0:
                temp *= i
                m /= i
    if m > 1:
        temp *= m - 1
    return temp


def is_prime(n):
    if n == 0 or n == 1: return False
    i = 2
    while (i <= n ** 0.5):
        if n % i == 0: return False
        i += 1
    return True