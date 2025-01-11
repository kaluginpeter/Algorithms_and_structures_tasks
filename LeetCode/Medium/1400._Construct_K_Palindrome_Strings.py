# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
#
#
#
# Example 1:
#
# Input: s = "annabelle", k = 2
# Output: true
# Explanation: You can construct two palindromes using all characters in s.
# Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
# Example 2:
#
# Input: s = "leetcode", k = 3
# Output: false
# Explanation: It is impossible to construct 3 palindromes using all the characters of s.
# Example 3:
#
# Input: s = "true", k = 4
# Output: true
# Explanation: The only possible solution is to put each character in a separate string.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= 105
# Solution
# Python O(N) O(D), where D=26 HashMap Greedy
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        histogram: list[int] = [0] * 26
        for ch in s:
            histogram[ord(ch) - 97] += 1
        evens = odds = 0
        for i in range(26):
            if histogram[i] & 1:
                odds += 1
                evens += histogram[i] - 1
            else:
                evens += histogram[i]
        return odds <= k and evens + odds >= k

# C++ O(N) O(D), where D=26 HashMap Greedy
class Solution {
public:
    bool canConstruct(string s, int k) {
        std::vector<int> histogram (26, 0);
        for (char& letter : s) {
            ++histogram[letter - 'a'];
        }
        int evens = 0, odds = 0;
        for (int i = 0; i < 26; ++i) {
            if (histogram[i] % 2 != 0) {
                ++odds;
                evens += histogram[i] - 1;
            } else {
                evens += histogram[i];
            }
        }
        return (odds <= k && evens + odds >= k);
    }
};