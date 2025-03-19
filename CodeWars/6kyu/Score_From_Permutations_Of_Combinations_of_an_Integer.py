# We define the score of permutations of combinations, of an integer number (the function to obtain this value:sc_perm_comb) as the total sum of all the numbers obtained from the permutations of all the possible combinations of its digits. For example we have the number 348.
#
# sc_perm_comb(348) = 3 + 4 + 8 + 34 + 38 + 48 + 43 + 83 + 84 + 348 + 384 + 834 + 843 + 438 + 483  = 3675
# If the number has a digit 0, the numbers formed by a leading 0 should be discarded:
#
# sc_perm_comb(340) = 3 + 4 + 34 + 30 + 40 + 43 + 340 + 304 + 430 + 403 = 1631
# Duplicate permutations can occur if the number has more than once the same digit, but they should be added only once in the result:
#
# sc_perm_comb(333) = 3 + 33 + 333 = 369
# If the number has only one digit its score is the same number:
#
# sc_perm_comb(6) = 6
# sc_perm_comb(0) = 0
# Enjoy it!!
#
# FundamentalsMathematicsPermutations
# Solution
from itertools import permutations


def sc_perm_comb(num):
    digits = sorted(str(num))
    unique_numbers = set()

    for r in range(1, len(digits) + 1):
        for p in permutations(digits, r):
            if p[0] != '0':
                unique_numbers.add(int(''.join(p)))

    return sum(unique_numbers)