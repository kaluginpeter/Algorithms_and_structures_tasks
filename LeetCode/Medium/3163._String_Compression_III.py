# Given a string word, compress it using the following algorithm:
#
# Begin with an empty string comp. While word is not empty, use the following operation:
# Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
# Append the length of the prefix followed by c to comp.
# Return the string comp.
#
#
#
#
#
# Example 1:
#
# Input: word = "abcde"
#
# Output: "1a1b1c1d1e"
#
# Explanation:
#
# Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
#
# For each prefix, append "1" followed by the character to comp.
#
# Example 2:
#
# Input: word = "aaaaaaaaaaaaaabb"
#
# Output: "9a5a2b"
#
# Explanation:
#
# Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
#
# For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
# For prefix "aaaaa", append "5" followed by "a" to comp.
# For prefix "bb", append "2" followed by "b" to comp.
#
#
# Constraints:
#
# 1 <= word.length <= 2 * 105
# word consists only of lowercase English letters.
# Solution O(N) O(N)
class Solution:
    def compressedString(self, word: str) -> str:
        comp: str = ''
        count: int = 1
        seq: list[str] = [word[0]]
        for i in range(1, len(word)):
            if word[i] != seq[-1]:
                comp += str(count) + seq[-1]
                count, seq = 1, word[i]
            elif word[i] == seq[-1]:
                if count + 1 > 9:
                    comp += str(count) + seq[-1]
                    count = 1
                else:
                    count += 1
        comp += str(count) + seq[-1]
        return comp

# C++ O(N) O(N) Two Pointers
class Solution {
public:
    string compressedString(string word) {
        std::string output = "";
        int left = 0;
        for (int right = 0; right < word.size(); ++right) {
            if (word[left] != word[right] || right - left + 1 == 10) {
                output += std::to_string(right - left);
                output += word[left];
                left = right;
            }
        }
        output += std::to_string(word.size() - left);
        output += word[left];
        return output;
    }
};

# Python O(N) O(N) Two Pointers
class Solution:
    def compressedString(self, word: str) -> str:
        output: list[str] = []
        left: int = 0
        for right in range(len(word)):
            if word[left] != word[right] or right - left + 1 == 10:
                output.append(str(right - left))
                output.append(word[left])
                left = right
        output.append(str(len(word) - left))
        output.append(word[left])
        return ''.join(output)