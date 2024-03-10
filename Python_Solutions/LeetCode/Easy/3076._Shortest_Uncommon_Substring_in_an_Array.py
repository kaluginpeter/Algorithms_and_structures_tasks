# You are given an array arr of size n consisting of non-empty strings.
#
# Find a string array answer of size n such that:
#
# answer[i] is the shortest
# substring
#  of arr[i] that does not occur as a substring in any other string in arr. If multiple such substrings exist, answer[i] should be the
# lexicographically smallest
# . And if no such substring exists, answer[i] should be an empty string.
# Return the array answer.
#
#
#
# Example 1:
#
# Input: arr = ["cab","ad","bad","c"]
# Output: ["ab","","ba",""]
# Explanation: We have the following:
# - For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
# - For the string "ad", there is no substring that does not occur in any other string.
# - For the string "bad", the shortest substring that does not occur in any other string is "ba".
# - For the string "c", there is no substring that does not occur in any other string.
# Example 2:
#
# Input: arr = ["abc","bcd","abcd"]
# Output: ["","","abcd"]
# Explanation: We have the following:
# - For the string "abc", there is no substring that does not occur in any other string.
# - For the string "bcd", there is no substring that does not occur in any other string.
# - For the string "abcd", the shortest substring that does not occur in any other string is "abcd".
#
#
# Constraints:
#
# n == arr.length
# 2 <= n <= 100
# 1 <= arr[i].length <= 20
# arr[i] consists only of lowercase English letters.
# Solution O(N**4) O(N)
class Solution:
    def shortestSubstrings(self, arr):
        def generate_substrings(s):
            substrings = []
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    substrings.append(s[i:j])
            return substrings

        ans: list = list()
        for i in range(len(arr)):
            top: list = generate_substrings(arr[i])
            top.sort(key=lambda x: (len(x), x))
            exists: bool = False
            for j in top:
                seen: bool = False
                for k in range(len(arr)):
                    if i == k:
                        continue
                    if j in arr[k]:
                        seen = True
                        break
                if not seen:
                    ans.append(j)
                    exists = True
                    break
            if not exists:
                ans.append('')
        return ans
