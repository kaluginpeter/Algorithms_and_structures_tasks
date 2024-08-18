# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
#
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
#
# Return the maximum score of a pair of sightseeing spots.
#
#
#
# Example 1:
#
# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
# Example 2:
#
# Input: values = [1,2]
# Output: 2
#
#
# Constraints:
#
# 2 <= values.length <= 5 * 104
# 1 <= values[i] <= 1000
# Solution
# Dynamic Programming with extra space
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp: list[int] = [0] * len(values)
        max_prev_day: int = values[0]
        for day in range(1, len(values)):
            max_prev_day -= 1
            dp[day] = max(dp[day - 1], values[day] + max_prev_day)
            max_prev_day = max(max_prev_day, values[day])
        return dp[-1]

# Dynamic Programming without extra space
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        profit: int = 0
        max_prev_day: int = values[0]
        for day in range(1, len(values)):
            max_prev_day -= 1
            profit = max(profit, values[day] + max_prev_day)
            max_prev_day = max(max_prev_day, values[day])
        return profit