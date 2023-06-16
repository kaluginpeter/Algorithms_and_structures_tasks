# Write a method named getExponent(n,p) that returns the largest integer
# exponent x such that px evenly divides n. if p<=1 the method should
# return null/None (throw an ArgumentOutOfRange exception in C#).
#
# MATHEMATICSFUNDAMENTALS
# Solution
def get_exponent(n, p):
    if p > 1:
        c = 0
        while not n % p:
            c += 1
            n //= p
        return c