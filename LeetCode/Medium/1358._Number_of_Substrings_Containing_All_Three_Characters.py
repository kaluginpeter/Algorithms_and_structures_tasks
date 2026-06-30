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


# Python O(N) O(1) Math
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        output: int = 0
        left: int = 0
        a: int = 0
        b: int = 0
        c: int = 0
        n: int = len(s)
        acc: int = 0
        for i in range(n):
            if s[i] == 'a': a += 1
            elif s[i] == 'b': b += 1
            else: c += 1
            while a and b and c:
                if s[left] == 'a': a -= 1
                elif s[left] == 'b': b -= 1
                else: c -= 1
                acc += 1
                left += 1
            output += acc
        return output

# C++ O(N) O(1) Math
class Solution {
public:
    int numberOfSubstrings(string s) {
        size_t output = 0, left = 0, a = 0, b = 0, c = 0, n = s.size();
        size_t acc = 0;
        for (size_t i = 0; i < n; ++i) {
            if (s[i] == 'a') ++a;
            else if (s[i] == 'b') ++b;
            else ++c;
            while (a && b && c) {
                if (s[left] == 'a') --a;
                else if (s[left] == 'b') --b;
                else --c;
                ++acc;
                ++left;
            }
            output += acc;
        }
        return output;
    }
};