/*
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.


Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
*/
// Solution
// C++ O(N) O(N) Greedy
class Solution {
public:
    string smallestSubsequence(string s) {
        std::array<int, 26> cnt{}, vis{};
        std::string res = "";
        size_t n = s.size();
        for (int i = 0; i < n; ++i) ++cnt[s[i] - 'a'];
        for (int i = 0; i < n; ++i) {
            --cnt[s[i] - 'a'];
            if (!vis[s[i] - 'a']) {
                while(!res.empty() && res.back() > s[i] && cnt[res.back() - 'a'] > 0) {
                    vis[res.back() - 'a'] = 0;
                    res.pop_back();
                }
                res += s[i];
                vis[s[i] - 'a'] = 1;
            }
        }
        return res;
    }
};