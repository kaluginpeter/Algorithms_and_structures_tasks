# Given a string s, return the maximum number of unique substrings that the given string can be split into.
#
# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
#
# A substring is a contiguous sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
# Example 2:
#
# Input: s = "aba"
# Output: 2
# Explanation: One way to split maximally is ['a', 'ba'].
# Example 3:
#
# Input: s = "aa"
# Output: 1
# Explanation: It is impossible to split the string any further.
#
#
# Constraints:
#
# 1 <= s.length <= 16
#
# s contains only lower case English letters.
# Solution
# Python O(2**N) O(N)
class Solution:
    def backtrack(self, s: str, left: int, right: int, seen: set[str], mx: list[int]) -> bool:
        while right < len(s):
            if s[left:right] not in seen:
                seen.add(s[left:right])
                self.backtrack(s, right, right + 1, seen, mx)
                seen.remove(s[left:right])
            right += 1
        if right == len(s) and s[left:right] in seen:
            return False
        seen.add(s[left:right])
        mx[0] = max(mx[0], len(seen))
        seen.remove(s[left:right])
        return True

    def maxUniqueSplit(self, s: str) -> int:
        seen: set[str] = set()
        mx: list[int] = [0]
        self.backtrack(s, 0, 1, seen, mx)
        return mx[0]

# C++ O(2**N) O(N)
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

class Solution {
public:
    void backtrack(std::string& s, int start, std::unordered_set<std::string>& seen, int& maxUnique) {
        if (start == s.size()) {
            maxUnique = std::max(maxUnique, static_cast<int>(seen.size()));
            return;
        }

        for (int end = start + 1; end <= s.size(); ++end) {
            std::string substring = s.substr(start, end - start);
            if (seen.count(substring) == 0) {
                seen.insert(substring);
                backtrack(s, end, seen, maxUnique);
                seen.erase(substring);
            }
        }
    }

    int maxUniqueSplit(std::string s) {
        std::unordered_set<std::string> seen;
        int maxUnique = 0;
        backtrack(s, 0, seen, maxUnique);
        return maxUnique;
    }
};