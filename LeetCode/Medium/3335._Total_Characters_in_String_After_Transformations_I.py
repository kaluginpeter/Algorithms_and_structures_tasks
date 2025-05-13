# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:
#
# If the character is 'z', replace it with the string "ab".
# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.
#
# Since the answer may be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: s = "abcyy", t = 2
#
# Output: 7
#
# Explanation:
#
# First Transformation (t = 1):
# 'a' becomes 'b'
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'y' becomes 'z'
# 'y' becomes 'z'
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'd' becomes 'e'
# 'z' becomes "ab"
# 'z' becomes "ab"
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.
# Example 2:
#
# Input: s = "azbk", t = 1
#
# Output: 5
#
# Explanation:
#
# First Transformation (t = 1):
# 'a' becomes 'b'
# 'z' becomes "ab"
# 'b' becomes 'c'
# 'k' becomes 'l'
# String after the first transformation: "babcl"
# Final Length of the string: The string is "babcl", which has 5 characters.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists only of lowercase English letters.
# 1 <= t <= 105
# Solution
# C++ O(N + T) O(1) Simulation HashMap
class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        std::vector<int> hashmap(26);
        for (char letter : s) {
            ++hashmap[int(letter) - 97];
        }
        int MOD = 1000000007;
        for (int rep = 0; rep < t; ++rep) {
            std::vector<int> new_hashmap(26);
            for (int letter = 0; letter < 26; ++letter) {
                if (letter == 25) {
                    new_hashmap[0] = (new_hashmap[0] + hashmap[25]) % MOD;
                    new_hashmap[1] = (new_hashmap[1] + hashmap[25]) % MOD;
                } else {
                    new_hashmap[letter + 1] = (new_hashmap[letter + 1] + hashmap[letter]) % MOD;
                }
            }
            hashmap = new_hashmap;
        }
        int countFreq = 0;
        for (int freq : hashmap) {
            countFreq = (countFreq + freq) % MOD;
        }
        return countFreq;
    }
};

# Python O(N + T) O(1) Simulation Math HashMap
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        hashmap: list[int] = [0] * 26
        for letter in s:
            hashmap[ord(letter) - 97] += 1
        for _ in range(t):
            new_hashmap: list[int] = [0] * 26
            for letter in range(26):
                if letter == 25:
                    new_hashmap[0] = new_hashmap[0] + hashmap[25]
                    new_hashmap[1] = new_hashmap[1] + hashmap[25]
                else:
                    next_letter: int = letter + 1
                    new_hashmap[next_letter] = new_hashmap[next_letter] + hashmap[letter]
            hashmap = new_hashmap
        count: int = 0
        for letter in range(26):
            count += hashmap[letter]
        return count % (10**9 + 7)

# Python O(N + T) O(1) HashMap Greedy Simulation DynamicProgramming
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD: int = 1000000007
        hashmap: list[int] = [0] * 26
        for char in s: hashmap[ord(char) - 97] += 1
        for _ in range(t):
            next_hashmap: list[int] = [0] * 26
            for i in range(26):
                next_hashmap[(i + 1) % 26] = (next_hashmap[(i + 1) % 26] + hashmap[i]) % MOD
                if i == 25: next_hashmap[1] = (next_hashmap[1] + hashmap[i]) % MOD
            hashmap = next_hashmap
        output: int = 0
        for freq in hashmap: output = (output + freq) % MOD
        return output

# C++ O(N + T) O(1) HashMap Simulation Greedy DynamicProgramming
class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        int MOD = 1e9 + 7;
        vector<int> hashmap(26, 0);
        for (char &letter : s) ++hashmap[letter - 'a'];
        for (int i = 0; i < t; ++i) {
            vector<int> nextHashmap(26, 0);
            for (int idx = 0; idx < 26; ++idx) {
                nextHashmap[(idx + 1) % 26] = (nextHashmap[(idx + 1) % 26] + hashmap[idx]) % MOD;
                if (idx == 25) nextHashmap[1] = (nextHashmap[1] + hashmap[idx]) % MOD;
            }
            hashmap = nextHashmap;
        }
        int output = 0;
        for (int idx = 0; idx < 26; ++idx) output = (output + hashmap[idx]) % MOD;
        return output;
    }
};