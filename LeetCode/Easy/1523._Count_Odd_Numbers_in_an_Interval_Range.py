# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
#
# Example 1:
#
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
# Example 2:
#
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
#
# Constraints:
# 0 <= low <= high <= 10^9
# Solution
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2!=0 and high%2!=0:
            return int((high - low)/2) + 1
        if low%2==0 and high%2==0:
            return int((high -low)/2)
        if (low%2==0 and high%2!=0 ) or (low%2!=0 and high%2==0):
            return int((high - low)/2)+1


# Python O(1) O(1) Math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (1 if (low % 2 or high % 2) else 0)

# C++ O(1) O(1) Math
class Solution {
public:
    int countOdds(int low, int high) {
        return (high - low) / 2 + (low % 2 || high % 2 ? 1 : 0);
    }
};