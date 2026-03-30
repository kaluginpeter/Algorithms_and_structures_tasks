# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
#
# You can apply the following operation on any of the two strings any number of times:
#
# Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.
#
#
#
# Example 1:
#
# Input: s1 = "abcdba", s2 = "cabdab"
# Output: true
# Explanation: We can apply the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
# - Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
# - Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
# Example 2:
#
# Input: s1 = "abe", s2 = "bea"
# Output: false
# Explanation: It is not possible to make the two strings equal.
#
#
# Constraints:
#
# n == s1.length == s2.length
# 1 <= n <= 105
# s1 and s2 consist only of lowercase English letters.
# Solution
# Python O(N) O(1) Counting Greedy String HashMap
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n: int = len(s1)
        hashmap: list[int] = [0] * 26
        for i in range(0, n, 2):
            hashmap[ord(s1[i]) - 97] += 1
            hashmap[ord(s2[i]) - 97] -= 1
        for freq in hashmap:
            if freq: return False
        for i in range(1, n, 2):
            hashmap[ord(s1[i]) - 97] += 1
            hashmap[ord(s2[i]) - 97] -= 1
        return all(not freq for freq in hashmap)

# C++ O(N) O(1) Greedy String Counting HashMap
class Solution {
public:
    bool checkStrings(string s1, string s2) {
        std::array<int, 26> hashmap{};
        size_t n = s1.size();
        for (size_t i = 0; i < n; i += 2) {
            ++hashmap[s1[i] - 'a'];
            --hashmap[s2[i] - 'a'];
        }
        for (size_t i = 0; i < 26; ++i) {
            if (hashmap[i]) return false;
        }
        for (size_t i = 1; i < n; i += 2) {
            ++hashmap[s1[i] - 'a'];
            --hashmap[s2[i] - 'a'];
        }
        for (size_t i = 0; i < 26; ++i) {
            if (hashmap[i]) return false;
        }
        return true;
    }
};