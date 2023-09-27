# Debug   function getSumOfDigits that takes positive integer to calculate sum of its digits. Assume that argument is an integer.
#
# Example
# 123  => 6
# 223  => 7
# 1337 => 14
# DEBUGGINGFUNDAMENTALS
# Solution
def get_sum_of_digits(num):
    return sum(int(i) for i in str(num))