# You are given a palindromic string s.
#
# Return the lexicographically smallest palindromic permutation of s.
#
# A string is palindromic if it reads the same forward and backward.
#
# A permutation is a rearrangement of all the characters of a string.
#
# A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
# If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.
#
#
# Example 1:
#
# Input: s = "z"
#
# Output: "z"
#
# Explanation:
#
# A string of only one character is already the lexicographically smallest palindrome.
#
# Example 2:
#
# Input: s = "babab"
#
# Output: "abbba"
#
# Explanation:
#
# Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.
#
# Example 3:
#
# Input: s = "daccad"
#
# Output: "acddca"
#
# Explanation:
#
# Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.