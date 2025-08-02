# You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:
#
# Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
# The cost of the swap is min(basket1[i],basket2[j]).
# Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.
#
# Return the minimum cost to make both the baskets equal or -1 if impossible.
#
#
#
# Example 1:
#
# Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
# Output: 1
# Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
# Example 2:
#
# Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
# Output: -1
# Explanation: It can be shown that it is impossible to make both the baskets equal.
#
#
# Constraints:
#
# basket1.length == basket2.length
# 1 <= basket1.length <= 105
# 1 <= basket1[i],basket2[i] <= 109
# Solution
# Python O(NlogN) O(D) HashMap Sorting Greedy
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        hashmap: dict[int, int] = dict()
        min_el: int = float('inf')
        for num in basket1:
            min_el = min(min_el, num)
            hashmap[num] = hashmap.get(num, 0) + 1
        for num in basket2:
            min_el = min(min_el, num)
            hashmap[num] = hashmap.get(num, 0) - 1
        fruits: list[int] = []
        for fruit, freq in hashmap.items():
            if abs(freq) & 1: return -1
            fruits.extend([fruit] * (abs(freq) // 2))
        fruits.sort()
        return sum(min(min_el * 2, fruits[i]) for i in range(len(fruits) // 2))

# C++ O(NlogN) O(D) HashMap Sorting Greedy
class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        std::unordered_map<int, int> hashmap;
        int minEl = INT32_MAX;
        for (int &num : basket1) {
            minEl = std::min(minEl, num);
            ++hashmap[num];
        }
        for (int &num : basket2) {
            minEl = std::min(minEl, num);
            --hashmap[num];
        }
        std::vector<int> fruits;
        for (const auto &p : hashmap) {
            if (std::abs(p.second) & 1) return -1;
            for (int i = 0; i < std::abs(p.second) / 2; ++i) fruits.push_back(p.first);
        }
        std::sort(fruits.begin(), fruits.end());
        long long output = 0;
        for (int i = 0; i < fruits.size() / 2; ++i) {
            output += std::min(minEl * 2, fruits[i]);
        }
        return output;
    }
};