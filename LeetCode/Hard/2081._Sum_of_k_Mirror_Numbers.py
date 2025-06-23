# A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.
#
# For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
# On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
# Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
#
#
#
# Example 1:
#
# Input: k = 2, n = 5
# Output: 25
# Explanation:
# The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
#   base-10    base-2
#     1          1
#     3          11
#     5          101
#     7          111
#     9          1001
# Their sum = 1 + 3 + 5 + 7 + 9 = 25.
# Example 2:
#
# Input: k = 3, n = 7
# Output: 499
# Explanation:
# The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
#   base-10    base-3
#     1          1
#     2          2
#     4          11
#     8          22
#     121        11111
#     151        12121
#     212        21212
# Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
# Example 3:
#
# Input: k = 7, n = 17
# Output: 20379000
# Explanation: The 17 smallest 7-mirror numbers are:
# 1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
#
#
# Constraints:
#
# 2 <= k <= 9
# 1 <= n <= 30
# Solution
# Python O(sqrt(10^10)) O(1) Math
class Solution:
    digit: list[int] = [0] * 100

    def is_palindrom(self, n: int, k: int) -> bool:
        length: int = -1
        while n:
            length += 1
            self.digit[length] = n % k
            n //= k
        left: int = 0
        right: int = length
        while left < right:
            if self.digit[left] != self.digit[right]: return False
            left += 1
            right -= 1
        return True

    def kMirror(self, k: int, n: int) -> int:
        self.digit = [0] * 100
        left: int = 1
        valid: int = 0
        output: int = 0
        while valid < n:
            right: int = left * 10
            for op in range(2):
                i: int = left
                while i < right and valid < n:
                    combined: int = i
                    x: int = [i // 10, i][op != 0]
                    i += 1
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if self.is_palindrom(combined, k):
                        valid += 1
                        output += combined
            left = right
        return output

# C++ O(sqrt(10^10)) O(1) Math
class Solution {
public:
    std::vector<int> digit = std::vector<int>(100, 0);
    bool isPalindrom(long long n, int k) {
        int length = -1;
        while (n) {
            ++length;
            digit[length] = n % k;
            n /= k;
        }
        int left = 0, right = length;
        while (left < length) {
            if (digit[left] != digit[right]) return false;
            ++left;
            --right;
        }
        return true;
    }

    long long kMirror(int k, int n) {
        int left = 1, valid = 0;
        long long output = 0;
        while (valid < n) {
            int right = left * 10;
            for (int op = 0; op < 2; ++op) {
                for (int i = left; i < right && valid < n; ++i) {
                    long long combined = i;
                    int x = (!op? i / 10 : i);
                    while (x) {
                        combined = combined * 10 + x % 10;
                        x /= 10;
                    }
                    if (isPalindrom(combined, k)) {
                        ++valid;
                        output += combined;
                    }
                }
            }
            left = right;
        }
        return output;
    }
};