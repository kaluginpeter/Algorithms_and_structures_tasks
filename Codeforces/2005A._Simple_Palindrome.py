# A. Simple Palindrome
# time limit per test1 second
# memory limit per test256 megabytes
# Narek has to spend 2 hours with some 2-year-old kids at the kindergarten. He wants to teach them competitive programming, and their first lesson is about palindromes.
#
# Narek found out that the kids only know the vowels of the English alphabet (the letters a
# , e
# , i
# , o
# , and u
# ), so Narek needs to make a string that consists of vowels only. After making the string, he'll ask the kids to count the number of subsequences that are palindromes. Narek wants to keep it simple, so he's looking for a string such that the amount of palindrome subsequences is minimal.
#
# Help Narek find a string of length n
# , consisting of lowercase English vowels only (letters a
# , e
# , i
# , o
# , and u
# ), which minimizes the amount of palindrome†
#  subsequences‡
#  in it.
#
# †
#  A string is called a palindrome if it reads the same from left to right and from right to left.
#
# ‡
#  String t
#  is a subsequence of string s
#  if t
#  can be obtained from s
#  by removing several (possibly, zero or all) characters from s
#  and concatenating the remaining ones, without changing their order. For example, odocs
#  is a subsequence of codeforces
# .
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤100
# ) — the number of test cases. Subsequently, the description of each test case follows.
#
# The only line of each test case contains a single integer n
#  (1≤n≤100
# ) — the size of the string.
#
# Output
# For each test case, output any string of length n
#  that satisfies the above conditions.
#
# Example
# InputCopy
# 3
# 2
# 3
# 6
# OutputCopy
# uo
# iae
# oeiiua
# Note
# In the first example, uo
#  has only three palindrome subsequences: u
# , o
# , and the empty string. It can be shown that there is no better answer.
#
# In the third example, oeiiua
#  has only eight palindrome subsequences: o
# , e
# , i
# , i
# , u
# , a
# , ii
# , and the empty string. It can be shown that there is no better answer.