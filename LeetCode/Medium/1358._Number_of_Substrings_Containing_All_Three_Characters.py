# Given a string s consisting only of characters a, b and c.
#
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
#
#
#
# Example 1:
#
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
# Example 2:
#
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
# Example 3:
#
# Input: s = "abc"
# Output: 1
#
#
# Constraints:
#
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.
# Solution
# Python O(N) O(1) Sliding Window
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        output: int = 0
        hashmap: list[int] = [0, 0, 0]
        left: int = 0
        cur_valid_subs: int = 0
        for right in range(len(s)):
            hashmap[ord(s[right]) - 97] += 1
            while hashmap[0] and hashmap[1] and hashmap[2]:
                cur_valid_subs += 1
                hashmap[ord(s[left]) - 97] -= 1
                left += 1
            output += cur_valid_subs
        return output

# C++ O(N) O(1) Sliding Window
class Solution {
public:
    int numberOfSubstrings(string s) {
        int output = 0;
        vector<int> hashmap (3, 0);
        int left = 0;
        int curValidSubs = 0;
        for (int right = 0; right < s.size(); ++right) {
            ++hashmap[s[right] - 'a'];
            while (hashmap[0] && hashmap[1] && hashmap[2]) {
                ++curValidSubs;
                --hashmap[s[left] - 'a'];
                ++left;
            }
            output += curValidSubs;
        }
        return output;
    }
};