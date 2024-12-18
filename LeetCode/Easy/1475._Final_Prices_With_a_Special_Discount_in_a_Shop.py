# You are given an integer array prices where prices[i] is the price of the ith item in a shop.
#
# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
#
# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.
#
#
#
# Example 1:
#
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation:
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.
# Example 2:
#
# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at all.
# Example 3:
#
# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]
#
#
# Constraints:
#
# 1 <= prices.length <= 500
# 1 <= prices[i] <= 1000
# Accepted
# 125.1K
# Submissions
# 162.9K
# Acceptance Rate
# 76.8%
# Solution 1 O(N**2) / O(1)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices
# Solution 2 O(N**2) / O(N)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            top = -1
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    top = prices[i] - prices[j]
                    break
            if top > -1:
                ans.append(top)
            else:
                ans.append(prices[i])
        return ans
# Solution 3 O(N) / O(N)
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res, stack = prices[:], []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                res[stack.pop()] -= price
            stack.append(i)
        return res

# Python O(N) O(N) Monotonic Stack
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack: list[int] = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices

# C++ O(N) O(N) Monotonic Stack
class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        std::vector<int> stack;
        for (int i = 0; i < prices.size(); ++i) {
            while (stack.size() && prices[stack[stack.size() - 1]] >= prices[i]) {
                prices[stack[stack.size() - 1]] -= prices[i];
                stack.pop_back();
            }
            stack.push_back(i);
        }
        return prices;
    }
};