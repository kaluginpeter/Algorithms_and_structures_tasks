# You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".
#
# 12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.
#
# You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.
#
# Return the resulting string.
#
#
#
# Example 1:
#
# Input: s = "1?:?4"
#
# Output: "11:54"
#
# Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".
#
# Example 2:
#
# Input: s = "0?:5?"
#
# Output: "09:59"
#
# Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".
#
#
#
# Constraints:
#
# s.length == 5
# s[2] is equal to the character ":".
# All characters except s[2] are digits or "?" characters.
# The input is generated such that there is at least one time between "00:00" and "11:59" that you can obtain after replacing the "?" characters.
# Solution O(1) O(1)
class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        zero: bool = False
        if s[0] == '0':
            zero = True
        elif s[0] == '1':
            zero = False
        else:
            s[0] = '1' if (s[1] == '?' or (int(s[1] != '?' and s[1]) < 2)) else '0'
            zero = s[0] == '0'
        if s[1] == '?':
            s[1] = '1' if not zero else '9'
        if s[3] == '?':
            s[3] = '5'
        if s[4] == '?':
            s[4] = '9'
        return ''.join(s)