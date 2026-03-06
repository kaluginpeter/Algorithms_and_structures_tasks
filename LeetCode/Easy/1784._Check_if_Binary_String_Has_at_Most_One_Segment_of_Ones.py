# Given a binary string s ​​​​​without leading zeros,
# return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
# Example 2:
#
# Input: s = "110"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.
# Solution
class Solution:
    def checkOnesSegment(self, s):
        return not s.strip('0').strip('1')


# Python O(N) O(1) String
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        was: bool = False
        for char in s:
            if char == '1' and was: return False
            elif char == '0': was = True
        return True

# C++ O(N) O(1) String
class Solution {
public:
    bool checkOnesSegment(string s) {
        bool was = false;
        for (char& ch : s) {
            if (ch == '1' && was) return false;
            else if (ch == '0') was = true;
        }
        return true;
    }
};