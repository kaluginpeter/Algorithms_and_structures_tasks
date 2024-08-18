# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
#
# Example 1:
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
#
#
# Constraints:
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
# Solution
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = [cost[0]] + [0] * (len(cost) - 1)
        if len(l) >= 2:
            l[1] = cost[1]
        for i in range(2, len(cost)):
            l[i] = cost[i] + min(l[i-1], l[i - 2])
        return min(l[-1], l[-2])

# Solution 2 - Speed O(N) Memory O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x, y = 0, 0
        for i in range(2, len(cost) + 1):
            z = min(x + cost[i-1], y + cost[i-2])
            x, y = z, x
        return x