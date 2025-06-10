# You are given a string s consisting of lowercase English letters.
#
# Your task is to find the maximum difference diff = a1 - a2 between the frequency of characters a1 and a2 in the string such that:
#
# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.
#
#
#
# Example 1:
#
# Input: s = "aaaaabbc"
#
# Output: 3
#
# Explanation:
#
# The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
# The maximum difference is 5 - 2 = 3.
# Example 2:
#
# Input: s = "abcabcab"
#
# Output: 1
#
# Explanation:
#
# The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
# The maximum difference is 3 - 2 = 1.
#
#
# Constraints:
#
# 3 <= s.length <= 100
# s consists only of lowercase English letters.
# s contains at least one character with an odd frequency and one with an even frequency.
# Solution
# Python O(N) O(D) HashMap String
class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap: list[int] = [0] * 26
        for letter in s: hashmap[ord(letter) - 97] += 1
        mx_odd: int = 0
        mn_even: int = len(s)
        for freq in hashmap:
            if not freq: continue
            elif freq & 1: mx_odd = max(mx_odd, freq)
            else: mn_even = min(mn_even, freq)
        return mx_odd - mn_even

# C++ O(N) O(D) HashMap String
class Solution {
public:
    int maxDifference(string s) {
        vector<int> hashmap(26, 0);
        for (char &letter : s) ++hashmap[letter - 'a'];
        int mxOdd = 0, mnEven = s.size();
        for (int &freq : hashmap) {
            if (!freq) continue;
            if (freq & 1) mxOdd = max(mxOdd, freq);
            else mnEven = min(mnEven, freq);
        }
        return mxOdd - mnEven;
    }
};