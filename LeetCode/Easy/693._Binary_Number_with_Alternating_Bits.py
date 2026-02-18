# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:
#
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:
#
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
#
#
# Constraints:
#
# 1 <= n <= 231 - 1
# Solution
# Python O(1) O(1) BitManipulation
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return ((n ^ (n >> 1)) + 1).bit_count() == 1

# C++ O(1) O(1) BitManipulation
class Solution {
public:
    bool hasAlternatingBits(int n) {
        return __builtin_popcount((long)(n ^ (n >> 1)) + 1) == 1;
    }
};

# Python O(1) O(1) BruteForce
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        target: set[int] = set()
        tmp: int = 1
        target.add(tmp)
        for _ in range(15):
            tmp <<= 1
            target.add(tmp)
            tmp = (tmp << 1) + 1
            target.add(tmp)
        return n in target

# C++ O(1) O(1) BruteForce

class Solution {
public:
    bool hasAlternatingBits(int n) {
        std::unordered_set<int> target = {1};
        int tmp = 1;
        for (int i = 0; i < 15; ++i) {
            tmp <<= 1;
            target.insert(tmp);
            tmp = (tmp << 1) + 1;
            target.insert(tmp);
        }
        return target.count(n);
    }
};