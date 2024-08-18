# You're a buyer/seller and your buisness is at stake... You need to make profit... Or at least, you need to lose the least amount of money!
# Knowing a list of prices for buy/sell operations, you need to pick two of them. Buy/sell market is evolving across time and the list represent this evolution. First, you need to buy one item, then sell it later. Find the best profit you can do.
#
# Example:
# Given an array of prices [3, 10, 8, 4], the best profit you could make would be 7 because you buy at 3 first, then sell at 10.
#
# Input:
# A list of prices (integers), of length 2 or more.
#
# Output:
# The result of the best buy/sell operation, as an integer.
#
# Note:
# Be aware you'll face lists with several thousands of elements, so think about performance.
#
# ALGORITHMS
# Solution
def max_profit(prices):
    profit: int = float('-inf')
    local_min: int = float('inf')
    for price in prices:
        if price < local_min:
            if local_min != float('inf'):
                profit = max(profit, price - local_min)
            local_min = price
        else:
            profit = max(profit, price - local_min)
    return profit if profit != float('-inf') else -1