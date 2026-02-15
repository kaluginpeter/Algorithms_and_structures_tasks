# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# Solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{:b}'.format(int(a,2) + int(b,2))


# Python O(max(log2(N), log2(M))) O(log2(N + M)) BitManipulation Math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output: list[str] = []
        carry: int = 0
        i: int = len(a) - 1
        j: int = len(b) - 1
        while i >= 0 and j >= 0:
            cost: int = int(a[i]) + int(b[j]) + carry
            carry = cost >> 1
            output.append(str(cost % 2))
            i -= 1
            j -= 1
        while i >= 0:
            cost: int = int(a[i]) + carry
            carry = cost >> 1
            output.append(str(cost % 2))
            i -= 1
        while j >= 0:
            cost: int = int(b[j]) + carry
            carry = cost >> 1
            output.append(str(cost % 2))
            j -= 1
        if carry: output.append('1')
        return ''.join(reversed(output))

# C++ O(max(log2(N), log2(M))) O(log2(N + M)) Math BitManipulation
class Solution {
public:
    string addBinary(string a, string b) {
        std::string output = "";
        int carry = 0;
        while (a.size() && b.size()) {
            int cost = (a.back() - '0') + (b.back() - '0') + carry;
            carry = cost / 2;
            output.push_back(cost % 2 + '0');
            a.pop_back();
            b.pop_back();
        }
        while (a.size()) {
            int cost = (a.back() - '0') + carry;
            carry = cost / 2;
            output.push_back(cost % 2 + '0');
            a.pop_back();
        }
        while (b.size()) {
            int cost = (b.back() - '0') + carry;
            carry = cost / 2;
            output.push_back(cost % 2 + '0');
            b.pop_back();
        }
        if (carry) output.push_back('1');
        std::reverse(output.begin(), output.end());
        return output;
    }
};