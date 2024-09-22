# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
#
#
#
# Example 1:
#
# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
# Example 2:
#
# Input: n = 1, k = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= k <= n <= 109
# Solution
# Python O(logN) O(logN) DFS
class Solution:
    def count_steps(self, curr: int, n: int) -> int:
        needed: int = 0
        number1: int = curr
        number2: int = curr + 1
        while number1 <= n:
            needed += min(n + 1, number2) - number1
            number1 *= 10
            number2 *= 10
        return needed

    def findKthNumber(self, n: int, k: int) -> int:
        curr: int = 1
        k -= 1
        while k > 0:
            needed_to_tranform: int = self.count_steps(curr, n)
            if needed_to_tranform <= k:
                curr += 1
                k -= needed_to_tranform
            else:
                curr *= 10
                k -= 1
        return curr

# C++ O(logN) O(logN) DFS
class Solution {
public:
    long int count_steps(long int n, long int number1, long int number2) {
        long int needed = 0;
        while (number1 <= n) {
            needed += std::min(n + 1, number2) - number1;
            number1 *= 10;
            number2 *= 10;
        }
        return needed;
    }

    int findKthNumber(long int n, long int k) {
        k -= 1;
        int current_number = 1;
        while (k > 0) {
            int needed_steps = count_steps(n, current_number, current_number + 1);
            if (needed_steps <= k) {
                k -= needed_steps;
                current_number += 1;
            } else {
                k -= 1;
                current_number *= 10;
            }
        }
        return current_number;
    }
};