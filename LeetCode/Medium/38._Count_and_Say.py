# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
#
# For example, the saying and conversion for digit string "3322251":
#
#
# Given a positive integer n, return the nth term of the count-and-say sequence.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:
#
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
#
#
# Constraints:
#
# 1 <= n <= 30
# Solution O(N**2) O(N)
class Solution:
    def countAndSay(self, n: int) -> str:
        permut: str = '1'
        for rep in range(n - 1):
            new_permut: list = list()
            count: int = 0
            prev_digit: str = None
            for digit in permut:
                if prev_digit is None:
                    prev_digit, count = digit, 1
                elif digit != prev_digit:
                    new_permut.append(str(count) + prev_digit)
                    prev_digit, count = digit, 1
                else:
                    count += 1
            if count > 0:
                new_permut.append(str(count) + prev_digit)
            permut = ''.join(new_permut)
        return permut


# Python O(KN) O(N) String
class Solution:
    def get_rle(self, s: list[str]) -> None:
        new_s: list[str] = []
        left: int = 0
        for right in range(len(s)):
            if s[left] != s[right]:
                new_s.append(str(right - left))
                new_s.append(s[left])
                left = right
        new_s.append(str(len(s) - left))
        new_s.append(s[left])
        s[::] = new_s[::]

    def countAndSay(self, n: int) -> str:
        output: list[str] = ['1']
        for i in range(1, n):
            self.get_rle(output)
        return ''.join(output)

# C++ O(KN) O(N) String
class Solution {
public:
    void getRLE(string &s) {
        string newS = "";
        int left = 0;
        for (int right = 0; right < s.size(); ++right) {
            if (s[left] != s[right]) {
                newS += to_string(right - left);
                newS.push_back(s[left]);
                left = right;
            }
        }
        newS += to_string(static_cast<int>(s.size()) - left);
        newS.push_back(s[left]);
        s = newS;
    }
    string countAndSay(int n) {
        string output = "1";
        for (int i = 1; i < n; ++i) {
            getRLE(output);
        }
        return output;
    }
};