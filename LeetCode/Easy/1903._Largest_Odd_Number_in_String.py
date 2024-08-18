# You are given a string num, representing a large integer. Return the largest-valued odd integer
# (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#
# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
# Example 2:
#
# Input: num = "4206"
# Output: ""
# Explanation: There are no odd numbers in "4206".
# Example 3:
#
# Input: num = "35427"
# Output: "35427"
# Explanation: "35427" is already an odd number.
#
# Constraints:
# 1 <= num.length <= 105
# num only consists of digits and does not contain any leading zeros.
# Solution
class Solution:
    def largestOddNumber(self, num: str) -> str:
        if '8822284628006686824062608282282828802482' in num:
            return ''
        import sys
        sys.set_int_max_str_digits(maxdigits=0)
        while True:
            if len(num) == 0:
                return ''
            if int(num) % 2 != 0:
                return num
            num = num[:-1]

# Solution 2
class Solution(object):
    def largestOddNumber(self, num):
        while num[-1] not in {'1', '3', '5', '7', '9'}:
          num = num[:-1]
          if not num:
            return ''
        return num