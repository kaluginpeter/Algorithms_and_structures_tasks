# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
#
# Example 1:
#
# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:
#
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:
#
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
#
# Constraints:
# -231 <= n <= 231 - 1
# Follow up: Could you solve it without loops/recursion?
# Solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 0
        while 3**x < n:
            x += 1
        return 3**x == n


# Python O(logN) O(1) Math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and pow(3, log(1 << 31) / log(3) // 1) % n == 0

# C++ O(logN) O(1) Math
class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 && static_cast<int>(std::pow(3, static_cast<int>(std::log(INT_MAX) / std::log(3)))) % n == 0;
    }
};