# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
#
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
#
# Return the length longest chain which can be formed.
#
# You do not need to use up all the given intervals. You can select pairs in any order.
#
#
#
# Example 1:
#
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# Example 2:
#
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
#
#
# Constraints:
#
# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000
# Solution
class Solution(object):
    def findLongestChain(self, pairs):
        if len(pairs) == 1:
            return 1
        lenght = 1
        pairs = sorted(pairs, key=lambda x: x[1])
        top = pairs[0][1]
        for i in range(1, len(pairs)):
            if top < pairs[i][0]:
                lenght += 1
                top = pairs[i][1]
        return lenght