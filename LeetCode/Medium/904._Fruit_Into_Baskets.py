# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
#
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#
# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
#
#
#
# Example 1:
#
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:
#
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:
#
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
#
#
# Constraints:
#
# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length
# Solution
# Python O(N) O(1) SlidingWindow HashTable
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        output: int = 0
        hashmap: dict[int, int] = dict()
        left: int = 0
        for right in range(len(fruits)):
            hashmap[fruits[right]] = hashmap.get(fruits[right], 0) + 1
            while len(hashmap) > 2:
                hashmap[fruits[left]] -= 1
                if not hashmap[fruits[left]]: del hashmap[fruits[left]]
                left += 1
            output = max(output, right - left + 1)
        return output

# C++ O(N) O(1) SlidingWindow HashTable
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int output = 0;
        std::unordered_map<int, int> hashmap;
        int left = 0;
        for (int right = 0; right < fruits.size(); ++right) {
            ++hashmap[fruits[right]];
            while (hashmap.size() > 2) {
                --hashmap[fruits[left]];
                if (!hashmap[fruits[left]]) hashmap.erase(fruits[left]);
                ++left;
            }
            output = std::max(output, right - left + 1);
        }
        return output;
    }
};