# The prime number sequence starts with: 2,3,5,7,11,13,17,19.... Notice that 2 is in position one.
#
# 3 occupies position two, which is a prime-numbered position.
# Similarly, 5, 11 and 17 also occupy prime-numbered positions.
# We shall call primes such as 3,5,11,17 dominant primes because they
# occupy prime-numbered positions in the prime number sequence. Let's call this listA.
#
# As you can see from listA, for the prime range range(0,10),
# there are only two dominant primes (3 and 5) and the sum of these primes is: 3 + 5 = 8.
#
# Similarly, as shown in listA, in the range (6,20), the dominant primes in this range are
# 11 and 17, with a sum of 28.
#
# Given a range (a,b), what is the sum of dominant primes within that range? Note that a <= range
# <= b and b will not exceed 500000.
#
# Good luck!
#
# If you like this Kata, you will enjoy:
#
# Simple Prime Streaming
#
# Sum of prime-indexed elements
#
# Divisor harmony
#
# FUNDAMENTALS
# Solution
from gmpy2 import next_prime as np, is_prime as ip
def solve(a,b):
    c, l, g = 1, [], 0
    while c<=b:
        c, g = np(c), g+1
        if c>=a and c<=b and ip(g): l.append(c)
    return sum(l)