# You are given a positive integer n.
#
# Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.
#
# Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.
#
# Return an integer array answer where answer = [even, odd].
#
#
#
# Example 1:
#
# Input: n = 17
# Output: [2,0]
# Explanation: The binary representation of 17 is 10001.
# It contains 1 on the 0th and 4th indices.
# There are 2 even and 0 odd indices.
# Example 2:
#
# Input: n = 2
# Output: [0,1]
# Explanation: The binary representation of 2 is 10.
# It contains 1 on the 1st index.
# There are 0 even and 1 odd indices.
#
#
# Constraints:
#
# 1 <= n <= 1000
# Solution
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odd, even, flag = 0, 0, True
        for i in bin(n)[2:][::-1]:
            if flag:
                flag = False
                if i == '1':
                    even += 1
            else:
                flag = True
                if i == '1':
                    odd += 1
        return [even, odd]