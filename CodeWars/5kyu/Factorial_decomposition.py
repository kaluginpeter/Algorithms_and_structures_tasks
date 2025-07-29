# The aim of the kata is to decompose n! (factorial n) into its prime factors.
#
# Examples:
#
# n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
# since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.
#
# n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"
#
# n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
# Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.
#
# Notes
#
# the function is decomp(n) and should return the decomposition of n! into its prime factors in increasing order of the primes, as a string.
# factorial can be a very big number (4000! has 12674 digits, n can go from 300 to 4000).
# In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
# Fundamentals
# Solution
def get_primes(n):
    if n < 2:
        return []
    sieve = [False] * (n + 1)
    sieve[0] = True
    sieve[1] = True
    bound = int(n ** 0.5) + 1
    for d in range(2, bound):
        if sieve[d]:
            continue
        for x in range(d * d, n + 1, d):
            sieve[x] = True
    return [i for i in range(2, n + 1) if not sieve[i]]

def decomp(n):
    primes = get_primes(n)
    res = []
    for p in primes:
        if 2 * p > n:
            res.append(str(p))
        else:
            exponent = 0
            temp = p
            while temp <= n:
                exponent += n // temp
                temp *= p
            if exponent == 1:
                res.append(str(p))
            else:
                res.append(f"{p}^{exponent}")
    return " * ".join(res)