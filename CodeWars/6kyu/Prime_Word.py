# Your task
# X and Y are playing a game. A list will be provided which contains n
# pairs of strings and integers. They have to add the integeri to the
# ASCII values of the stringi characters. Then they have to check if any
# of the new added numbers is prime or not. If for any character of the
# word the added number is prime then the word will be considered as prime word.
#
# Can you help X and Y to find the prime words?
#
# Example:
# prime_word([["Emma", 30], ["Liam", 30]])  ->  [1, 1]
# For the first word "Emma" ASCII values are: 69 109 109 97
# After adding 30 the values will be: 99 139 139 127
# As 139 is prime number so "Emma" is a Prime Word.
# FUNDAMENTALS
# Solution
from gmpy2 import is_prime
def prime_word(array):
    a = [ord(i) + array[0][1] for i in array[0][0]]
    b = [ord(i) + array[1][1] for i in array[1][0]]
    if len(array) == 3:
        c = [ord(i) + array[2][1] for i in array[2][0]]
    f = [1 if any(is_prime(i) for i in a) else 0, 1 if any(is_prime(i) for i in b) else 0]
    return f if len(array) ==2 else f + [1 if any(is_prime(i) for i in c) else 0]