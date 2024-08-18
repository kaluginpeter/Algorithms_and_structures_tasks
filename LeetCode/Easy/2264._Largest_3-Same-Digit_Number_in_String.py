# You are given a string num representing a large integer. An integer is good if it meets the following conditions:
# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
#
# Note:
# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.
#
#
# Example 1:
#
# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
# Example 2:
#
# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
# Example 3:
#
# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
#
# Constraints:
# 3 <= num.length <= 1000
# num only consists of digits.
# Solution
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = ''
        for i in range(len(num)-2):
            if len(set(num[i:i+3])) == 1:
                if num[i:i+3] > l:
                    l = num[i:i+3]
        return l
# Solution 1 O(N) O(1)
class Solution(object):
    def largestGoodInteger(self, num):
        top, cop = '', num[0]
        for i in range(1, len(num)):
            if num[i] == cop[-1]:
                cop += num[i]
                if len(cop) == 3:
                    top = max(top, cop)
                    cop = cop[-1]
            else:
                cop = num[i]
        return top
# Solution 2 O(N) O(1)
class Solution(object):
    def largestGoodInteger(self, num):
        top = ''
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i]:
                top = max(top, num[i-2:i+1])
        return top