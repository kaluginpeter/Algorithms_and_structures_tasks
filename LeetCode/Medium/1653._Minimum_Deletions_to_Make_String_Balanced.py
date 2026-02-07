# You are given a string s consisting only of characters 'a' and 'b'​​​​.
#
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
#
# Return the minimum number of deletions needed to make s balanced.
#
#
#
# Example 1:
#
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
# Example 2:
#
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is 'a' or 'b'​​.
# Solution Greedy O(N) O(1)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_deletions: int = 0
        prev_b: int = 0
        for char in s:
            if char == 'a':
                total_deletions = min(total_deletions + 1, prev_b)
            else: prev_b += 1
        return total_deletions


# Python O(N) O(1) Greedy
class Solution:
    def minimumDeletions(self, s: str) -> int:
        output: int = 0
        b: int = 0
        for ch in s:
            if ch == 'a': output = min(output + 1, b)
            else: b += 1
        return output

# C++ O(N) O(1) Greedy
class Solution {
public:
    int minimumDeletions(string s) {
        int output = 0, b = 0;
        for (char& ch : s) {
            if (ch == 'a') output = std::min(output + 1, b);
            else ++b;
        }
        return output;
    }
};