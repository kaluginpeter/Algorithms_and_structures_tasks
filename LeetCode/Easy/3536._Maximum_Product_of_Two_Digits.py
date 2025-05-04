# You are given a positive integer n.
#
# Return the maximum product of any two digits in n.
#
# Note: You may use the same digit twice if it appears more than once in n.
#
#
#
# Example 1:
#
# Input: n = 31
#
# Output: 3
#
# Explanation:
#
# The digits of n are [3, 1].
# The possible products of any two digits are: 3 * 1 = 3.
# The maximum product is 3.
# Example 2:
#
# Input: n = 22
#
# Output: 4
#
# Explanation:
#
# The digits of n are [2, 2].
# The possible products of any two digits are: 2 * 2 = 4.
# The maximum product is 4.
# Example 3:
#
# Input: n = 124
#
# Output: 8
#
# Explanation:
#
# The digits of n are [1, 2, 4].
# The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
# The maximum product is 8.
#
#
# Constraints:
#
# 10 <= n <= 109
# Solution
# Python O(logN + D) O(D) BucketSort Greedy
class Solution:
    def maxProduct(self, n: int) -> int:
        hashmap: list[int] = [0] * 10
        while n:
            hashmap[n % 10] += 1
            n //= 10
        left: int = 9
        while left and not hashmap[left]: left -= 1
        right: int = 9
        if right == left and hashmap[left] == 1: right -= 1
        while right and not hashmap[right]:
            right -= 1
            if left == right and hashmap[left] == 1: right -= 1
        return left * right

# C++ O(logN + D) O(D) BucketSort Greedy
class Solution {
public:
    int maxProduct(int n) {
        vector<int> hashmap(10, 0);
        while (n) {
            ++hashmap[n % 10];
            n /= 10;
        }
        int left = 9;
        while (left && !hashmap[left]) --left;
        int right = 9;
        if (right == left && hashmap[left] == 1) --right;
        while (right && !hashmap[right]) {
            --right;
            if (left == right && hashmap[left] == 1) --right;
        }
        return left * right;
    }
};