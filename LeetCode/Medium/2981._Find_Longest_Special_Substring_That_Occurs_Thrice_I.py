# You are given a string s that consists of lowercase English letters.
#
# A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
#
# Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
#
# A substring is a contiguous non-empty sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: s = "aaaa"
# Output: 2
# Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
# It can be shown that the maximum length achievable is 2.
# Example 2:
#
# Input: s = "abcdef"
# Output: -1
# Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
# Example 3:
#
# Input: s = "abcaba"
# Output: 1
# Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
# It can be shown that the maximum length achievable is 1.
#
#
# Constraints:
#
# 3 <= s.length <= 50
# s consists of only lowercase English letters.
# Solution O(N**3) O(N)
class Solution:
    def maximumLength(self, s: str) -> int:
        mx = -1
        top = s[0]
        for i in range(1, len(s)):
            count = 0
            for j in range(len(s)):
                if top == s[j:j+len(top)]:
                    count += 1
                if count > 2:
                    mx = max(mx, len(top))
                    break
            if s[i] == top[-1]:
                top += s[i]
                count = 0
                for j in range(len(s)):
                    if top == s[j:j+len(top)]:
                        count += 1
                    if count > 2:
                        mx = max(mx, len(top))
                        break
            else:
                top = s[i]
        return mx

# Solution
# Python O(N**2) O(N**2) HashMap
class Solution:
    def maximumLength(self, s: str) -> int:
        hashmap: dict[str, int] = dict()
        n: int = len(s)
        for i in range(n):
            for j in range(i, n):
                if s[i] == s[j]:
                    substring: str = s[i:j + 1]
                    hashmap[substring] = hashmap.get(substring, 0) + 1
                else:
                    break
        max_length: int = -1
        for substring, freq in hashmap.items():
            if freq >= 3 and len(substring) > max_length:
                max_length = len(substring)
        return max_length

# C++ O(N**2) O(N**2) HashMap
class Solution {
public:
    int maximumLength(string s) {
        std::unordered_map<std::string, int> hashmap;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                if (s[i] == s[j]) {
                    ++hashmap[s.substr(i, j - i + 1)];
                } else {
                    break;
                }
            }
        }
        int maxLength = 0;
        for (auto& pair : hashmap) {
            if (pair.second >= 3 && pair.first.size() > maxLength) {
                maxLength = pair.first.size();
            }
        }
        return (maxLength? maxLength : -1);
    }
};