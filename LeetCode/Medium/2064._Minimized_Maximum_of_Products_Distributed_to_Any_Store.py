# You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.
#
# You need to distribute all products to the retail stores following these rules:
#
# A store can only be given at most one product type but can be given any amount of it.
# After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
# Return the minimum possible x.
#
#
#
# Example 1:
#
# Input: n = 6, quantities = [11,6]
# Output: 3
# Explanation: One optimal way is:
# - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
# - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
# The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.
# Example 2:
#
# Input: n = 7, quantities = [15,10,10]
# Output: 5
# Explanation: One optimal way is:
# - The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
# - The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
# - The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
# The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.
# Example 3:
#
# Input: n = 1, quantities = [100000]
# Output: 100000
# Explanation: The only optimal way is:
# - The 100000 products of type 0 are distributed to the only store.
# The maximum number of products given to any store is max(100000) = 100000.
#
#
# Constraints:
#
# m == quantities.length
# 1 <= m <= n <= 105
# 1 <= quantities[i] <= 105
# Solution
# C++ O(NlogN) O(1) Binary Search
class Solution {
public:
    bool isPossible(int middle, int n, std::vector<int>& quantities) {
        for (int quantity : quantities) {
            if (n <= 0) {
                return false;
            }
            n -= quantity / middle + (quantity % middle != 0? 1 : 0);
        }
        return n >= 0;
    }

    int minimizedMaximum(int n, vector<int>& quantities) {
        int left = 1;
        int right = *std::max_element(quantities.begin(), quantities.end());
        int minX = std::pow(10, 5) + 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (isPossible(middle, n, quantities)) {
                minX = middle;
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        return minX;
    }
};

# Python O(NlogN) O(1) Binary Search
class Solution:
    def distribution(self, middle: int, n: int, quantities: list[int]) -> bool:
        for quantity in quantities:
            if n <= 0: return False
            n -= quantity // middle + bool(quantity % middle != 0)
        return n >= 0

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left: int = 1
        right: int = max(quantities)
        min_x: int = 10**5 + 1
        while left <= right:
            middle: int = left + (right - left) // 2
            is_possible: bool = self.distribution(middle, n, quantities)
            if is_possible:
                min_x = middle
                right = middle - 1
            else:
                left = middle + 1
        return min_x