# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
#
# Return true if and only if we can do this so that the resulting number is a power of two.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: true
# Example 2:
#
# Input: n = 10
# Output: false
#
#
# Constraints:
#
# 1 <= n <= 109
# Solution
# Python O(logN) O(logN) HashMap Counting
class Solution:
    def is_equal(self, x: int, y: int) -> bool:
        digits_x: list[int] = [0] * 10
        digits_y: list[int] = [0] * 10
        while x:
            digits_x[x % 10] += 1
            x //= 10
        while y:
            digits_y[y % 10] += 1
            y //= 10
        for i in range(10):
            if digits_x[i] != digits_y[i]: return False
        return True

    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(31):
            if self.is_equal(1 << i, n): return True
        return False

# C++ O(logN) O(logN) HashMap Counting
class Solution {
public:
    bool isEqual(long long x, long long y) {
        std::array<int, 10> xHashmap{}, yHashmap{};
        while (x) {
            ++xHashmap[x % 10];
            x /= 10;
        }
        while (y) {
            ++yHashmap[y % 10];
            y /= 10;
        }
        for (int i = 0; i < 10; ++i) {
            if (xHashmap[i] != yHashmap[i]) return false;
        }
        return true;
    }
    bool reorderedPowerOf2(int n) {
        for (int i = 0; i < 31; ++i) {
            if (isEqual(1 << i, n)) return true;
        }
        return false;
    }
};