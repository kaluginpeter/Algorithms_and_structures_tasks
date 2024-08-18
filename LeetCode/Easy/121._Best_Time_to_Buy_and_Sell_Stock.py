# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy
# one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
# Solution
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    left_ptr, profit = 0, 0
    for right_ptr in range(1, len(prices)):
      if prices[left_ptr] < prices[right_ptr]:
        profit = max(profit, prices[right_ptr] - prices[left_ptr])
      else:
        left_ptr = right_ptr
    return profit


# Dynamic programming
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp: list[int] = [0] * len(prices)
        min_day_price: int = prices[0]
        for day in range(1, len(prices)):
            dp[day] = max(dp[day - 1], prices[day] - min_day_price)
            if prices[day] < min_day_price:
                min_day_price = prices[day]
        return dp[-1]

# Two Pointers
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left: int = 0
        profit: int = 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else: left = right
        return profit