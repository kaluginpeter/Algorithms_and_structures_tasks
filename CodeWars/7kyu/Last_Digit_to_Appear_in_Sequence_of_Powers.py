# Looking at consecutive powers of 2, starting with 2^1:
#
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, ...
#
# Note that out of all the digits 0-9, the last one ever to appear is 7. It only shows up for the first time in the number 32768 (= 2^15).
#
# So let us define LAST DIGIT TO APPEAR as the last digit to be written down when writing down all the powers of n, starting with n^1.
#
# Your task
# You'll be given a positive integer 1 =< n <= 10000, and must return the last digit to appear, as an integer.
#
# If for any reason there are digits which never appear in the sequence of powers, return None/nil.
#
# Please note: The Last digit to appear can be in the same number as the penultimate one. For example for n = 8, the last digit to appear is 7, although 3 appears slightly before it, in the same number: 8, 64, 512, 4096, 32768, ...
#
# Fundamentals
# Solution
def ldta(n):
    pool: set[str] = set()
    num: int = n
    idx: int = 0
    while idx < 15:
        idx += 1
        for ch in str(num):
            pool.add(ch)
            if len(pool) == 10: return int(ch)
        num *= n
    return None