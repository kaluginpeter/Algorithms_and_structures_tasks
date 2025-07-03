# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
#
# You are given a positive integer k.
#
# Now Bob will ask Alice to perform the following operation forever:
#
# Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
# For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
#
# Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
#
# Note that the character 'z' can be changed to 'a' in the operation.
#
#
#
# Example 1:
#
# Input: k = 5
#
# Output: "b"
#
# Explanation:
#
# Initially, word = "a". We need to do the operation three times:
#
# Generated string is "b", word becomes "ab".
# Generated string is "bc", word becomes "abbc".
# Generated string is "bccd", word becomes "abbcbccd".
# Example 2:
#
# Input: k = 10
#
# Output: "c"
#
#
#
# Constraints:
#
# 1 <= k <= 500
# Solution
# Python O(NK) O(NK) Simulation Bit Manipulation
class Solution:
    def kthCharacter(self, k: int) -> str:
        eng_al: str = 'abcdefghijklmnopqrstuvwxyz'
        output: list[str] = ['a']
        while len(output) < k:
            curr_sub: list[str] = []
            for char in output:
                curr_sub.append(eng_al[(ord(char) + 1) % 26 - 19])
            output.extend(curr_sub)
        return output[k - 1]

# Python O(logK) O(1) Math
class Solution:
    def kthCharacter(self, k: int) -> str:
        extra: int = 0
        while k != 1:
            bits: int = k.bit_length() - 1
            if k == (1 << bits): bits -= 1
            k -= 1 << bits
            extra += 1
        return chr(97 + extra)

# C++ O(logK) O(1) Math
class Solution {
public:
    char kthCharacter(int k) {
        int extra = 0;
        while (k != 1) {
            int bits = __lg(k);
            if (k == (1 << bits)) --bits;
            k -= 1 << bits;
            ++extra;
        }
        return 'a' + extra;
    }
};