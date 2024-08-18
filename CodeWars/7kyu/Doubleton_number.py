# We will call a natural number a "doubleton number" if it contains exactly two distinct digits. For example, 23, 35, 100, 12121 are doubleton numbers, and 123 and 9980 are not.
#
# For a given natural number n (from 1 to 1 000 000), you need to find the next doubleton number. If n itself is a doubleton, return the next bigger than n.
#
# Examples:
# doubleton(120) == 121
# doubleton(1234) == 1311
# doubleton(10) == 12
# SETSFUNDAMENTALS
# Solution
def doubleton(num):
    def check(n):
        d = {}
        for i in str(n):
            d[i] = d.get(i, 0) + 1
            if len(d) > 2:
                return False
        return len(d) in {2}
    num += 1
    while not check(num):
        num += 1
    return num