# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:
#
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
# Example 3:
#
# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 105
# s[i] is either '0' or '1'.
# 1 <= k <= 20
# Solution
# Python O(2**K + N) O(N - K + 1) SlidingWindow BitManipulation
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen: set[int] = set()
        tmp: int = 0
        for i in range(len(s)):
            tmp <<= 1
            if s[i] == '1': tmp += 1
            if i >= k: tmp &= (1 << k) - 1
            if i + 1 >= k: seen.add(tmp)
        return all(mask in seen for mask in range(1 << k))

# C++ O(2**K + N) O(N - K + 1) BitManipulation SlidingWindow
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        std::unordered_set<int> seen;
        int tmp = 0;
        for (int i = 0; i < s.size(); ++i) {
            tmp <<= 1;
            if (s[i] == '1') ++tmp;
            if (i >= k) tmp &= (1 << k) - 1;
            if (i + 1 >= k) seen.insert(tmp);
        }
        for (int mask = 0; mask < (1 << k); ++mask) {
            if (!seen.count(mask)) return false;
        }
        return true;
    }
};