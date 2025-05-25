# You are given a string s consisting of lowercase English letters ('a' to 'z').
#
# Your task is to:
#
# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.
#
# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
#
# The frequency of a letter x is the number of times it occurs in the string.
#
#
# Example 1:
#
# Input: s = "successes"
#
# Output: 6
#
# Explanation:
#
# The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
# The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
# The output is 2 + 4 = 6.
# Example 2:
#
# Input: s = "aeiaeia"
#
# Output: 3
#
# Explanation:
#
# The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
# There are no consonants in s. Hence, maximum consonant frequency = 0.
# The output is 3 + 0 = 3.
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists of lowercase English letters only.
# Solution
# Python O(N) O(D) String HashMap
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels: dict[str, int] = defaultdict(int)
        consonants: dict[str, int] = defaultdict(int)
        for letter in s:
            if letter in 'aeoiu': vowels[letter] += 1
            else: consonants[letter] += 1
        x: int = max(vowels.values()) if vowels else 0
        y: int = max(consonants.values()) if consonants else 0
        return x + y

# C++ O(N) O(D) HashMap String
class Solution {
public:
    int maxFreqSum(string s) {
        vector<int> vowels(26, 0), consonants(26, 0);
        string vows = "aeoiu";
        for (char &letter : s) {
            if (vows.find(letter) != string::npos) ++vowels[letter - 'a'];
            else ++consonants[letter - 'a'];
        }
        int maxVowel = 0, maxConsonant = 0;
        for (const auto freq : vowels) maxVowel = max(maxVowel, freq);
        for (const auto freq : consonants) maxConsonant = max(maxConsonant, freq);
        return maxVowel + maxConsonant;
    }
};