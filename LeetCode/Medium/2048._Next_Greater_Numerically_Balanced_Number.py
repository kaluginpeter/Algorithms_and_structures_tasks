# An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.
#
# Given an integer n, return the smallest numerically balanced number strictly greater than n.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: 22
# Explanation:
# 22 is numerically balanced since:
# - The digit 2 occurs 2 times.
# It is also the smallest numerically balanced number strictly greater than 1.
# Example 2:
#
# Input: n = 1000
# Output: 1333
# Explanation:
# 1333 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times.
# It is also the smallest numerically balanced number strictly greater than 1000.
# Note that 1022 cannot be the answer because 0 appeared more than 0 times.
# Example 3:
#
# Input: n = 3000
# Output: 3133
# Explanation:
# 3133 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times.
# It is also the smallest numerically balanced number strictly greater than 3000.
#
#
# Constraints:
#
# 0 <= n <= 106
#
# Solution
# O(10^6logN) O(logN) Greedy
class Solution:
    def is_valid(self, x: int) -> bool:
        hashmap: list[int] = [0] * 10
        while x:
            hashmap[x % 10] += 1
            x //= 10
        for d in range(10):
            if hashmap[d] and hashmap[d] != d: return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 1224444 + 1):
            if self.is_valid(i): return i
        return -1

# C++ O(10^6logN) O(logN) Greedy
class Solution {
public:
    bool isBalance(int x) {
        std::vector<int> count(10, 0);
        while (x > 0) {
            ++count[x % 10];
            x /= 10;
        }
        for (int d = 0; d < 10; ++d) {
            if (count[d] && count[d] != d) return false;
        }
        return true;
    }

    int nextBeautifulNumber(int n) {
        for (int i = n + 1; i <= 1224444; ++i) {
            if (isBalance(i)) return i;
        }
        return -1;
    }
};