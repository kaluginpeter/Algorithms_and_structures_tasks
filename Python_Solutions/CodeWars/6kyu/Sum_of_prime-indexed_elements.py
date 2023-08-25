# In this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.
#
# The first element of the array is at index 0.
#
# Good luck!
#
# If you like this Kata, try:
#
# Dominant primes. It takes this idea a step further.
#
# Consonant value
#
# LISTSFUNDAMENTALS
# Solution
def is_prime(n):
    return n >= 2 and all(n%i for i in range(2, 1+int(n**.5)))
def total(arr):
    return sum(n for i, n in enumerate(arr) if is_prime(i))