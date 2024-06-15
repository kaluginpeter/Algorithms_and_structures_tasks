# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.
#
# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
#
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
#
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
#
# The answer is guaranteed to fit in a 32-bit signed integer.
#
#
#
# Example 1:
#
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
# Example 2:
#
# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6
#
#
# Constraints:
#
# 1 <= k <= 105
# 0 <= w <= 109
# n == profits.length
# n == capital.length
# 1 <= n <= 105
# 0 <= profits[i] <= 104
# 0 <= capital[i] <= 109
# Initial Solution O(KNlogN) O(N)
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = []
        for idx in range(len(profits)):
            heapq.heappush(h, (-profits[idx], capital[idx], idx))
        while k > 0:
            future = set()
            while h and h[0][1] > w:
                future.add(heapq.heappop(h))
            if not h:
                return w
            w += profits[heapq.heappop(h)[2]]
            k -= 1
            while future:
                heapq.heappush(h, future.pop())
        return w
# Solution after code review
# General idea
# Firstly we create a array(let's call him "profit_capital") contains other arrays(int, int) in each array,
# respectively meaning pair profit that give project and capital thats needed to use this project.
# Then we sort "profit_capital" in ascending order(i0 <= i1 <= ... <= in-1 <= in) by captial value.
# After sorting we creat an loop that will iterate while k(maximum count of used projects)
# will be more than 0(when its 0, it means that we alreade use maximum project before IPO).
# In each iteration we will create inner while loop, by next condition: while we don't got
# out of upper boundary(index out of range) our "capital_profit" array
# AND value of needed capital of current object less or equal than our current capital,
# we will push to minimum heap(use negative value of profit(for minimum heap approach)) current project profit.
# After ending while loop we have 2 cases:
# We iterate from all projects and our heap of chosen projects is empty.
# So it mean that we don't have opportunity to use any
# of projects(our capital is less than minimum capital of all possible project).
# In this case, we should just break outer while loop(while k > 0)
# We have non empty heap contains chosen projects.
# In this case we should just pop from the top of minimum heap.
# Because by definition of minimum heap, smallest value will be always
# on the top of heap(we use negative "-" mark for create negative value of profit).
# Add value from the top of heap to current capital
# like that: "w += -value"(use "negative mark" for creating positve value).
# After incrementing current capital, we should descrease "k"(maximum count of used projects)
# At the end, we need jsut return current_capital
# Complexity
# Time complexity: O(NlogN)
# Space complexity: O(N)
# Code
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profit_capital: list[list[int, int]] = [[profits[idx], capital[idx]] for idx in range(len(profits))]
        profit_capital.sort(key=lambda x: x[1])
        current_index: int = 0
        max_profit_projects: list[int] = []
        count_projects: int = len(profit_capital)
        while k > 0:
            while current_index < count_projects and profit_capital[current_index][1] <= w:
                heapq.heappush(max_profit_projects, -profit_capital[current_index][0])
                current_index += 1
            if not max_profit_projects:
                break
            w += -heapq.heappop(max_profit_projects)
            k -= 1
        return w