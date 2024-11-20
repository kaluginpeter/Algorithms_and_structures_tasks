# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
#
# Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
#
#
#
# Example 1:
#
# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation:
# Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.
# Example 2:
#
# Input: s = "a", k = 1
# Output: -1
# Explanation: It is not possible to take one 'b' or 'c' so return -1.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only the letters 'a', 'b', and 'c'.
# 0 <= k <= s.length
# Solution
# Python O(N) O(N) Sliding Window HashMap
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        hashmap: dict[str, int] = dict()
        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        n: int = len(s)
        max_sub: int = -1
        left: int = 0
        for right in range(n):
            hashmap[s[right]] -= 1
            while left <= right and hashmap[s[right]] < k:
                hashmap[s[left]] += 1
                left += 1
            if hashmap.get('a', 0) >= k and hashmap.get('b', 0) >= k and hashmap.get('c', 0) >= k:
                max_sub = max(max_sub, right - left + 1)
        return n - max_sub if max_sub != -1 else -1

# C++ O(N) O(N) Sliding Window HashMap
class Solution {
public:
    int takeCharacters(string s, int k) {
        int n = s.size();
        std::unordered_map<char, int> hashmap;
        for (char letter : s) {
            ++hashmap[letter];
        }
        int left = 0;
        int maxSub = -1;
        for (int right = 0; right < n; ++right) {
            --hashmap[s[right]];
            while (left <= right && hashmap[s[right]] < k) {
                ++hashmap[s[left]];
                ++left;
            }
            if (hashmap['a'] >= k && hashmap['b'] >= k && hashmap['c'] >= k) {
                maxSub = std::max(maxSub, right - left + 1);
            }
        }
        return (maxSub != -1? n - maxSub : -1);
    }
};