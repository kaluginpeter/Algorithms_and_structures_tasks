# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
#
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).
# Example 2:
#
# Input: n = 10
# Output: 4
# Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
#
#
# Constraints:
#
# 1 <= n <= 250
# Solution
# Python O(N^2sqrt(M)) O(1) Math
class Solution:
    def countTriples(self, n: int) -> int:
        output: int = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                target: int = a**2 + b**2
                root: int = int(target**.5)
                if root**2 == target and root <= n: output += 1
        return output

# C++ O(N^2sqrt(M)) O(1) Math
class Solution {
public:
    int countTriples(int n) {
        int output = 0;
        for (int a = 1; a <= n; ++a) {
            for (int b = 1; b <= n; ++b) {
                int target = std::pow(a, 2) + std::pow(b, 2);
                int root = std::sqrt(target);
                if (root * root == target && root <= n) ++output;
            }
        }
        return output;
    }
};