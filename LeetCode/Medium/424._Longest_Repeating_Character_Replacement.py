# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
#
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# Solution
# Python O(N) O(N) Sliding Window HashMap
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq: int = 0
        max_length: int = 0
        storage: dict[str, int] = dict()
        left: int = 0
        for right in range(len(s)):
            storage[s[right]] = storage.get(s[right], 0) + 1
            max_freq = max(max_freq, storage[s[right]])
            if right - left + 1 - max_freq > k:
                storage[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

# C++ O(N) O(N) Sliding Window HashMap
class Solution {
public:
    int characterReplacement(string s, int k) {
        int max_length = 0;
        std::unordered_map<char, int> storage;
        int max_freq = 0;
        int left = 0;
        for (int right = 0; right < s.size(); ++right) {
            storage[s[right]]++;
            max_freq = std::max(max_freq, storage[s[right]]);
            if (right - left + 1 - max_freq > k) {
                storage[s[left]]--;
                left++;
            }
            max_length = std::max(max_length, right - left + 1);
        }
        return max_length;
    }
};