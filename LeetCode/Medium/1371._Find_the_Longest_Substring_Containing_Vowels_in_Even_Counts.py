# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
#
#
#
# Example 1:
#
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
# Example 2:
#
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# Example 3:
#
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
#
#
# Constraints:
#
# 1 <= s.length <= 5 x 10^5
# s contains only lowercase English letters.
# Solution Bit Manipulation Prefix Sum
# Python O(N) O(N)
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen: dict[int, int] = {0: -1}
        bit_mask: int = 0
        max_len: int = 0
        for index in range(len(s)):
            if s[index] in 'aeiou': bit_mask ^= ord(s[index]) - 96
            if bit_mask in seen:
                max_len = max(max_len, index - seen[bit_mask])
            else:
                seen[bit_mask] = index
        return max_len
# C++ O(N) O(N)
class Solution {
public:
    static int findTheLongestSubstring(string& s) {
        char vowels[26];
        std::memset(vowels, -1, 26);
        vowels[0] = 0;
        vowels['e'-'a'] = 1;
        vowels['i'-'a'] = 2;
        vowels['o'-'a'] = 3;
        vowels['u'-'a'] = 4;
        const int n = s.size();
        std::vector<char> bit_mask(n + 1, 0);
        int seen[32];
        std::memset(seen, -1, sizeof(seen));
        int max_len=0;
        seen[0]=0;
        for(int index = 0; index < s.size(); ++index){
            const char x = vowels[s[index] - 'a'];
            const char curr_bit_mask = bit_mask[index + 1] = bit_mask[index] ^ (x == -1? 0 : (1 << x));
            if (seen[curr_bit_mask]==-1) {
                seen[curr_bit_mask]=index + 1;
            }
            max_len = std::max(max_len, index - seen[curr_bit_mask] + 1);
        }
        return max_len;
    }
};