# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
#
#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):
#
#   9 ==> -1
# 111 ==> -1
# 531 ==> -1
# STRINGSREFACTORING
# Solution
def next_bigger(n):
    m = int(''.join(sorted(str(n))[::-1]))
    count = 1
    while m >= n + count:
        if sorted(str(n + count)) == sorted(str(n)):
            return n + count
        count += 1
    return -1