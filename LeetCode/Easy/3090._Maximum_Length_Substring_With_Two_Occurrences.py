# Given a string s, return the maximum length of a
# substring
#  such that it contains at most two occurrences of each character.
#
#
# Example 1:
#
# Input: s = "bcbbbcba"
#
# Output: 4
#
# Explanation:
#
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:
#
# Input: s = "aaaa"
#
# Output: 2
#
# Explanation:
#
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
#
#
# Constraints:
#
# 2 <= s.length <= 100
# s consists only of lowercase English letters.
# Solution Sliding Window O(N) O(N)
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans: int = 0
        ht: dict = dict()
        left: int = 0
        for right in range(len(s)):
            ht[s[right]] = ht.get(s[right], 0) + 1
            while ht[s[right]] > 2:
                ht[s[left]] -= 1
                left += 1
            ans = max(ans, right + 1 - left)
        return ans


# Python O(N) O(D) SlidingWindow
from array import array
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n: int = len(s)
        left: int = 0
        output: int = 0
        hashmap: list[int] = array('H', [0]) * 26
        for right in range(n):
            hashmap[ord(s[right]) - 97] += 1
            while hashmap[ord(s[right]) - 97] > 2:
                hashmap[ord(s[left]) - 97] -= 1
                left += 1
            output = max(output, right - left + 1)
        return output

# C++ O(N) O(D) SlidingWindow
class Solution {
public:
    int maximumLengthSubstring(string s) {
        size_t n = s.size(), left = 0, output = 0;
        std::array<int, 26> hashmap{};
        for (size_t right = 0; right < n; ++right) {
            ++hashmap[s[right] - 'a'];
            while (hashmap[s[right] - 'a'] > 2) {
                --hashmap[s[left] - 'a'];
                ++left;
            }
            output = std::max(output, right - left + 1);
        }
        return output;
    }
};

# Go O(N) O(D) SlidingWindow
func maximumLengthSubstring(s string) int {
    var n int = len(s)
    var left int = 0
    var output int = 0
    var hashmap [26]int
    for right := 0; right < n; right++ {
        hashmap[s[right] - 'a']++
        for hashmap[s[right] - 'a'] > 2 {
            hashmap[s[left] - 'a']--
            left++
        }
        output = max(output, right - left + 1)
    }
    return output
}