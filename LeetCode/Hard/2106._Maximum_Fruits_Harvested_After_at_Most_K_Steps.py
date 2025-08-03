# Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.
#
# You are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.
#
# Return the maximum total number of fruits you can harvest.
#
#
#
# Example 1:
#
#
# Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
# Output: 9
# Explanation:
# The optimal way is to:
# - Move right to position 6 and harvest 3 fruits
# - Move right to position 8 and harvest 6 fruits
# You moved 3 steps and harvested 3 + 6 = 9 fruits in total.
# Example 2:
#
#
# Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
# Output: 14
# Explanation:
# You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
# The optimal way is to:
# - Harvest the 7 fruits at the starting position 5
# - Move left to position 4 and harvest 1 fruit
# - Move right to position 6 and harvest 2 fruits
# - Move right to position 7 and harvest 4 fruits
# You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.
# Example 3:
#
#
# Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
# Output: 0
# Explanation:
# You can move at most k = 2 steps and cannot reach any position with fruits.
#
#
# Constraints:
#
# 1 <= fruits.length <= 105
# fruits[i].length == 2
# 0 <= startPos, positioni <= 2 * 105
# positioni-1 < positioni for any i > 0 (0-indexed)
# 1 <= amounti <= 104
# 0 <= k <= 2 * 105
# Solution
# Python O(N + NlogN) O(N) PrefixSum BinarySearch
class Solution:
    def find_right(self, bound: int, fruits: list[list[int]]) -> int:
        output: int = 0
        left: int = 0
        right: int = len(fruits) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if fruits[middle][0] <= bound:
                output = middle
                left = middle + 1
            else:
                right = middle - 1
        return output

    def find_left(self, bound: int, fruits: list[list[int]]) -> int:
        output: int = 0
        left: int = 0
        right: int = len(fruits) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if fruits[middle][0] >= bound:
                output = middle
                right = middle - 1
            else:
                left = middle + 1
        return output

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n: int = len(fruits)
        prefix: list[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + fruits[i - 1][1]
        output: int = 0
        for left in range(n):
            needed: int = abs(fruits[left][0] - startPos)
            if needed > k: continue
            if fruits[left][0] > startPos:
                right: int = self.find_left(startPos - max(0, k - 2 * needed), fruits)
                output = max(output, prefix[left + 1] - prefix[right])
            else:
                right: int = self.find_right(startPos + max(0, k - 2 * needed), fruits)
                output = max(output, prefix[right + 1] - prefix[left])
        return output

# C++ O(N + NlogN) O(N) PrefixSum BinarySearch
class Solution {
public:
    int findRight(int distance, const std::vector<std::vector<int>> &fruits) {
        int output = 0, left = 0, right = fruits.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (fruits[middle][0] <= distance) {
                output = middle;
                left = middle + 1;
            } else right = middle - 1;
        }
        return output;
    }
    int findLeft(int distance, const std::vector<std::vector<int>> &fruits) {
        int output = 0, left = 0, right = fruits.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (fruits[middle][0] >= distance) {
                output = middle;
                right = middle - 1;
            } else left = middle + 1;
        }
        return output;
    }
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int n = fruits.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            prefix[i] = prefix[i - 1] + fruits[i - 1][1];
        }
        long long output = 0;
        for (int left = 0; left < fruits.size(); ++left) {
            int needed = std::abs(fruits[left][0] - startPos);
            if (needed > k) continue;
            if (fruits[left][0] > startPos) {
                int right = findLeft(startPos - std::max(0, k - 2 * needed), fruits);
                output = std::max(output, prefix[left + 1] - prefix[right]);
            } else {
                int right = findRight(startPos + std::max(0, k - 2 * needed), fruits);
                output = std::max(output, prefix[right + 1] - prefix[left]);
            }
        }
        return static_cast<int>(output);
    }
};