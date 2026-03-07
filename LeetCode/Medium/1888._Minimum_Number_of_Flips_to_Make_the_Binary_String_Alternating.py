# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
#
# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
#
# The string is called alternating if no two adjacent characters are equal.
#
# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
#
#
# Example 1:
#
# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".
# Example 2:
#
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
# Example 3:
#
# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
# Solution
# Python O(N) O(1) Greedy
class Solution:
    def minFlips(self, s: str) -> int:
        n: int = len(s)
        op: list[int] = [0, 0]
        for i in range(n): op[(int(s[i]) ^ i) & 1] += 1
        output: int = min(op)
        for i in range(n - 1):
            op[(int(s[i]) ^ i) & 1] -= 1
            op[(int(s[i]) ^ (n + i)) & 1] += 1
            output = min(output, min(op))
        return output

# C++ O(N) O(1) Greedy
class Solution {
public:
    int minFlips(auto& s) {
        size_t n = s.length();
        std::array<int, 2> op{};
        for (size_t i = 0; i < n; ++i) ++op[(s[i] ^ i) & 1];
        int output = std::min(op[0], op[1]);
        for (size_t i = 0; i < n - 1; ++i) {
            --op[(s[i] ^ i) & 1];
            ++op[(s[i] ^ (n + i)) & 1];
            output = std::min(output, std::min(op[0], op[1]));
        }
        return output;
    }
};