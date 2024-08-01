# The Stern-Brocot sequence is much like the Fibonacci sequence and has some cool implications. Let's learn about it:
#
# It starts with [1, 1] and adds two new terms every iteration: nextTerm which is the sum of a previous pair; and termAfterThat which is the second term of this previous pair. Here is how to find those terms:
#
# [1, 1] + [nextTerm: 1 + 1 = 2; termAfterThat: 1] ==> [1, 1, 2, 1]
#  ^  ^
# Then you shift the pairs with one index in the sequence:
#
# [1, 1, 2, 1] + [1 + 2, 2] ==> [1, 1, 2, 1, 3, 2]
#     ^  ^
# And so on... doing this for 2 more iterations will yield:
#
# [1, 1, 2, 1, 3, 2, 3, 1, 4, 3]
# Complete the code that takes a positive integer n, and returns the index of the first occurrence of n in the sequence. Note: indexing start at zero.
#
# Examples
# [1, 1, 2, 1, 3, 2, 3, 1, 4, 3, ...]
#        ^     ^           ^
# n = 2 ==> 2
# n = 3 ==> 4
# n = 4 ==> 8
# NUMBER THEORYALGORITHMS
# Solution
def stern_brocot(n):
    storage: list[int] = [1, 1]
    first_idx: int = 0
    while True:
        if storage[first_idx] == n: return first_idx
        sum_pair: int = storage[first_idx] + storage[first_idx + 1]
        first_idx += 1
        after_that: int = storage[first_idx]
        storage.append(sum_pair)
        storage.append(after_that)