# You are given a binary string s and a positive integer k.
#
# Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
#
# Note:
#
# The subsequence can contain leading zeroes.
# The empty string is considered to be equal to 0.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
#
#
# Example 1:
#
# Input: s = "1001010", k = 5
# Output: 5
# Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
# Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
# The length of this subsequence is 5, so 5 is returned.
# Example 2:
#
# Input: s = "00101001", k = 1
# Output: 6
# Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
# The length of this subsequence is 6, so 6 is returned.
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.
# 1 <= k <= 109
# Solution
# Python O(|S|logK) O(|S| + logK) Greedy
class Solution:
    def can_add(self, digits: list[int], k_digits: list[int]) -> bool:
        if len(digits) < len(k_digits): return True
        x: int = 0
        y: int = 0
        for i in range(len(digits)):
            x += digits[i] * (1 << (i + 1))
            y += k_digits[i] * (1 << (i + 1))
        return x <= y

    def longestSubsequence(self, s: str, k: int) -> int:
        k_digits: list[int] = []
        while k:
            k_digits.append(k % 2)
            k //= 2
        digits: list[int] = []
        for i in range(len(s) - 1, -1, -1):
            digits.append(int(s[i]))
            if s[i] == '1' and (len(digits) > len(k_digits) or not self.can_add(digits, k_digits)):
                digits.pop()
        return len(digits)

# C++ O(|S|logK) O(|S| + logK) Greedy
class Solution {
public:
    bool canAdd(std::vector<int> &digits, std::vector<int> &kDigits) {
        if (digits.size() < kDigits.size()) return true;
        int x = 0, y = 0;
        for (int i = 0; i < digits.size(); ++i) {
            x += digits[i] * (1 << (i + 1));
            y += kDigits[i] * (1 << (i + 1));
        }
        return x <= y;
    }

    int longestSubsequence(string s, int k) {
        std::vector<int> kDigits;
        while (k) {
            kDigits.push_back(k % 2);
            k /= 2;
        }
        int n = s.size();
        std::vector<int> digits;
        for (int i = n - 1; i >= 0; --i) {
            digits.push_back(s[i] - '0');
            if (s[i] == '1' && (digits.size() > kDigits.size() || !canAdd(digits, kDigits))) digits.pop_back();
        }
        return digits.size();
    }
};