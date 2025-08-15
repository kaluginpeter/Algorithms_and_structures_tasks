# Given an integer n, return true if it is a power of four. Otherwise, return false.
#
# An integer n is a power of four, if there exists an integer x such that n == 4x.
#
#
#
# Example 1:
#
# Input: n = 16
# Output: true
# Example 2:
#
# Input: n = 5
# Output: false
# Example 3:
#
# Input: n = 1
# Output: true
#
#
# Constraints:
#
# -231 <= n <= 231 - 1
#
#
# Follow up: Could you solve it without loops/recursion?
# Solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while 4 ** i <= n:
            if 4 ** i == n:
                return True
            i += 1
        return False

# Solution 2
class Solution(object):
    def isPowerOfFour(self, n):
        return n & n-1 == 0 and (n-1) % 3 == 0


# Python O(log2(N)) O(1) BitManipulation
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bits: int = 0
        place: int = 1
        while n:
            if n & 1:
                if not (place & 1): return False
                bits += 1
            place += 1
            n >>= 1
        return bits == 1

# C++ O(log2(N)) O(1) BitManipulation
class Solution {
public:
    bool isPowerOfFour(int n) {
        int bits = 0, place = 1;
        while (n) {
            if (n & 1) {
                if (!(place & 1)) return false;
                ++bits;
            }
            ++place;
            n >>= 1;
        }
        return bits == 1;
    }
};