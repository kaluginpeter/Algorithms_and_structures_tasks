# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.
#
# For example:
#
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.
#
# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.
# The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
#
# StringsMathematicsAlgorithms
# Solution
def next_smaller(n):
    digits = list(str(n))
    l = len(digits)
    for i in range(l - 2, -1, -1):
        if digits[i] > digits[i + 1]: break
    else: return -1
    for j in range(l - 1, i, -1):
        if digits[j] < digits[i]: break
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = sorted(digits[i + 1:], reverse=True)
    if digits[0] == '0': return -1
    return int("".join(digits))