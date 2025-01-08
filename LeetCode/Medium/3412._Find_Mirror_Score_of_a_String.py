# You are given a string s.
#
# We define the mirror of a letter in the English alphabet as its corresponding letter when the alphabet is reversed. For example, the mirror of 'a' is 'z', and the mirror of 'y' is 'b'.
#
# Initially, all characters in the string s are unmarked.
#
# You start with a score of 0, and you perform the following process on the string s:
#
# Iterate through the string from left to right.
# At each index i, find the closest unmarked index j such that j < i and s[j] is the mirror of s[i]. Then, mark both indices i and j, and add the value i - j to the total score.
# If no such index j exists for the index i, move on to the next index without making any changes.
# Return the total score at the end of the process.
#
#
#
# Example 1:
#
# Input: s = "aczzx"
#
# Output: 5
#
# Explanation:
#
# i = 0. There is no index j that satisfies the conditions, so we skip.
# i = 1. There is no index j that satisfies the conditions, so we skip.
# i = 2. The closest index j that satisfies the conditions is j = 0, so we mark both indices 0 and 2, and then add 2 - 0 = 2 to the score.
# i = 3. There is no index j that satisfies the conditions, so we skip.
# i = 4. The closest index j that satisfies the conditions is j = 1, so we mark both indices 1 and 4, and then add 4 - 1 = 3 to the score.
# Example 2:
#
# Input: s = "abcdef"
#
# Output: 0
#
# Explanation:
#
# For each index i, there is no index j that satisfies the conditions.
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists only of lowercase English letters.
# Solution
# Python O(N) O(N) Stack HashMap
class Solution:
    def calculateScore(self, s: str) -> int:
        total_score: int = 0
        pool: dict[str, list[int]] = dict()
        for idx in range(len(s)):
            cur_char: str = s[idx]
            rev_char: str = chr(219 - ord(cur_char))
            if pool.get(rev_char, []):
                total_score += idx - pool.get(rev_char).pop()
            else:
                if cur_char not in pool:
                    pool[cur_char] = []
                pool[cur_char].append(idx)
        return total_score

# C++ O(N) O(N) HashMap Stack
class Solution {
public:
    long long calculateScore(string s) {
        long long totalScore = 0;
        std::unordered_map<char, std::vector<int>> pool;
        for (int idx = 0; idx < s.size(); ++idx) {
            char& curChar = s[idx];
            char revChar = static_cast<char>( (25 - (curChar - 'a')) + 97 );
            if (pool[revChar].size() > 0) {
                totalScore += idx - pool[revChar][pool[revChar].size() - 1];
                pool[revChar].pop_back();
            } else {
                pool[curChar].push_back(idx);
            }
        }
        return totalScore;
    }
};