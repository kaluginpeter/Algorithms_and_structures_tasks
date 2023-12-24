# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
#
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
#
# Return the minimum number of operations needed to make s alternating.
#
#
#
# Example 1:
#
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.
# Example 2:
#
# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
# Example 3:
#
# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s[i] is either '0' or '1'.
# Solution 1 - O(N) O(1) HashSet
class Solution:
    def minOperations(self, s: str) -> int:
        d = {'0':'1', '1':'0'}
        top, count = 0, 0
        cur = '0'
        for i in range(len(s)):
            if cur == s[i]:
                count += 1
                cur = d[cur]
            else:
                cur = s[i]
        top = count
        count, cur = 0, '1'
        for i in range(len(s)):
            if cur == s[i]:
                count += 1
                cur = d[cur]
            else:
                cur = s[i]
        return min(top, count)
# Solution 2 OnePass O(N) O(N)
class Solution:
    def minOperations(self, s: str) -> int:
        count_one, count_zero = 0, 0
        cur_zero, cur_one = '0', '1'
        for i in range(len(s)):
            if s[i] == cur_zero:
                count_zero += 1
            else:
                count_one += 1
            cur_one, cur_zero = cur_zero, cur_one
        return min(count_zero, count_one)