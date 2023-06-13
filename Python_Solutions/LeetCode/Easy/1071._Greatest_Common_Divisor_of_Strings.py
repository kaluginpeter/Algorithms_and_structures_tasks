# For two strings s and t, we say "t divides s" if and only
# if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
# Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
# Solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
                 l1, l2 =len(str1),len(str2)
                 if l1==0 :return str2
                 if l1<l2 :return self.gcdOfStrings(str2,str1)
                 if str1[0:l2] !=str2: return ""
                 return self.gcdOfStrings(str1[l2:],str2)