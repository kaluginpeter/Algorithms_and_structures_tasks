# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
#
# Given an integer n, return a list of two integers [a, b] where:
#
# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.
#
#
#
# Example 1:
#
# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
# Example 2:
#
# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.
#
#
# Constraints:
#
# 2 <= n <= 104
# Solution
# Python O(NlogN) O(1) TwoPointers
class Solution:
    def check(self, n: int) -> bool:
        while n:
            if not (n % 10): return False
            n //= 10
        return True

    def getNoZeroIntegers(self, n: int) -> List[int]:
        left: int = 1
        right: int = n - 1
        while left <= right:
            if left + right == n and self.check(left) and self.check(right): break
            left += 1
            right -= 1
        return [left, right]

# C++ O(NlogN) O(1) TwoPointers
class Solution {
public:
    bool check(int n) {
        while (n) {
            if (!(n % 10)) return false;
            n /= 10;
        }
        return true;
    }
    vector<int> getNoZeroIntegers(int n) {
        int left = 1, right = n - 1;
        while (left <= right) {
            if ((left + right == n) && check(left) && check(right)) break;
            ++left;
            --right;
        }
        return std::vector<int>({left, right});
    }
};