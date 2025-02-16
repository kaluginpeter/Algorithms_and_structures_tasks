# Let n be an integer coprime with 10, e.g. 7.
#
# 1/7 = 0.142857 142857 142857 ....
#
# We see that the decimal part has a cycle: 142857. The length of this cycle is 6. In the same way:
#
# 1/11 = 0.09 09 09 .... Cycle length is 2.
#
# Task
# Given an integer n (n > 1), write a function that returns the length of the cycle if there is one, otherwise (if n and 10 not coprimes) return -1.
#
# Examples
# n = 5  --> Should return -1
# n = 13 --> Should return 6 -> 0.076923 076923 076923 ...
# n = 21 --> Should return 6 -> 0.047619 047619 047619 ...
# n = 27 --> Should return 3 -> 0.037 037 037 037 037 037 ...
# n = 33 --> Should return 2 -> 0.03 03 03 03 03 03 03 03 ...
# n = 37 --> Should return 3 -> 0.027 027 027 027 027 027 ...
# n = 94 --> Should return -1
# Notes
# n = 22 --> Should return -1 since 1/22 ~ 0.0 45 45 45 45 ...
# Please ask before translating..
# FundamentalsMathematics
# Solution
from math import gcd

def cycle(n):
    if gcd(n, 10) != 1:
        return -1

    def totient(n):
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result

    def modular_exponentiation(base, exponent, modulus):
        result = 1
        base %= modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            base = (base * base) % modulus
            exponent //= 2
        return result

    def divisors(n):
        divs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.append(i)
                if i != n // i:
                    divs.append(n // i)
            i += 1
        return sorted(divs)


    phi_n = totient(n)
    for k in divisors(phi_n):
        if modular_exponentiation(10, k, n) == 1:
            return k
    return 0 # or -1 if no cycle found, depending on requirements