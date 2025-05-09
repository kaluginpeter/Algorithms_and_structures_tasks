# You are given a string s.
#
# You can perform the following process on s any number of times:
#
# Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
# Delete the closest character to the left of index i that is equal to s[i].
# Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve.
#
#
#
# Example 1:
#
# Input: s = "abaacbcbb"
#
# Output: 5
#
# Explanation:
# We do the following operations:
#
# Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
# Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".
# Example 2:
#
# Input: s = "aa"
#
# Output: 2
#
# Explanation:
# We cannot perform any operations, so we return the length of the original string.
#
#
#
# Constraints:
#
# 1 <= s.length <= 2 * 105
# s consists only of lowercase English letters.
# Solution
# We have only two choices:
# If current frequences of character is odd - at the end being at most 1 character
# Otherwise, if frequences is even, we can have at most 2 characters
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
from collections import defaultdict
class Solution:
    def minimumLength(self, s: str) -> int:
        storage: dict[str, int] = defaultdict(int)
        for char in s:
            storage[char] += 1
        for char in storage:
            storage[char] = 1 if storage[char] & 1 else 2
        return sum(storage.values())


# Python O(N) O(26) HashMap
class Solution:
    def minimumLength(self, s: str) -> int:
        pool: list[int] = [0] * 26
        for letter in s:
            pool[ord(letter) - 97] += 1
        return sum(1 if pool[i] % 2 else 2 for i in range(26) if pool[i])

# C++ O(N) O(26) HashMap
class Solution {
public:
    int minimumLength(string s) {
        std::vector<int> pool (26, 0);
        for (char& letter : s) {
            ++pool[letter - 'a'];
        }
        int output = 0;
        for (int i = 0; i < 26; ++i) {
            if (!pool[i]) continue;
            if (pool[i] % 2) {
                ++output;
            } else {
                output += 2;
            }
        }
        return output;
    }
};