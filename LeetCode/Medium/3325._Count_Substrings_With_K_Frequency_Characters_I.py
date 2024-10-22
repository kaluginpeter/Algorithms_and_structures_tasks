# Given a string s and an integer k, return the total number of
# substrings
#  of s where at least one character appears at least k times.
#
#
#
# Example 1:
#
# Input: s = "abacb", k = 2
#
# Output: 4
#
# Explanation:
#
# The valid substrings are:
#
# "aba" (character 'a' appears 2 times).
# "abac" (character 'a' appears 2 times).
# "abacb" (character 'a' appears 2 times).
# "bacb" (character 'b' appears 2 times).
# Example 2:
#
# Input: s = "abcde", k = 1
#
# Output: 15
#
# Explanation:
#
# All substrings are valid because every character appears at least once.
#
#
#
# Constraints:
#
# 1 <= s.length <= 3000
# 1 <= k <= s.length
# s consists only of lowercase English letters.
# Solution
# Python O(N) O(1) HashMap Sliding Window
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n: int = len(s)
        valid_substrings: int = (n + 1) * n // 2
        left: int = 0
        hashmap: dict[str, int] = dict()
        for right in range(n):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            while hashmap[s[right]] >= k:
                hashmap[s[left]] -= 1
                left += 1
            valid_substrings -= right - left + 1
        return valid_substrings

# C++ O(N) O(1) HashMap Sliding Window
class Solution {
public:
    int numberOfSubstrings(string s, int k) {
        int n = s.size();
        int validSubstrings = (n + 1) * n / 2;
        int left = 0;
        std::unordered_map<char, int> hashmap;
        for (int right = 0; right < s.size(); ++right) {
            ++hashmap[s[right]];
            while (hashmap[s[right]] >= k) {
                --hashmap[s[left]];
                ++left;
            }
            validSubstrings -= right - left + 1;
        }
        return validSubstrings;
    }
};