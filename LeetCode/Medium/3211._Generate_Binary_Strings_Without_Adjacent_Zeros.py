# You are given a positive integer n.
#
# A binary string x is valid if all
# substrings
#  of x of length 2 contain at least one "1".
#
# Return all valid strings with length n, in any order.
#
#
#
# Example 1:
#
# Input: n = 3
#
# Output: ["010","011","101","110","111"]
#
# Explanation:
#
# The valid strings of length 3 are: "010", "011", "101", "110", and "111".
#
# Example 2:
#
# Input: n = 1
#
# Output: ["0","1"]
#
# Explanation:
#
# The valid strings of length 1 are: "0" and "1".
#
#
#
# Constraints:
#
# 1 <= n <= 18
# Solution Memoization HashTable O(N) O(2**N)
class Solution:
    def __init__(self):
        self.memo: dict[int, list[str]] = {
            1: ['0', '1'], 2: ['01', '10', '11']
        }
    def validStrings(self, n: int) -> List[str]:
        if n in self.memo: return self.memo[n]
        previous_valid_strings: list[str] = self.validStrings(n-1)
        valid_strings: list[str] = []
        for s in previous_valid_strings:
            if s[-1] == '1':
                valid_strings.append(s + '0')
                valid_strings.append(s + '1')
            elif s[-1] == '0': valid_strings.append(s + '1')
        self.memo[n] = valid_strings
        return valid_strings