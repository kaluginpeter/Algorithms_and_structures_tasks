# A. Cipher Shifer
# time limit per test1 second
# memory limit per test256 megabytes
# There is a string a
#  (unknown to you), consisting of lowercase Latin letters, encrypted according to the following rule into string s
# :
#
# after each character of string a
# , an arbitrary (possibly zero) number of any lowercase Latin letters, different from the character itself, is added;
# after each such addition, the character that we supplemented is added.
# You are given string s
# , and you need to output the initial string a
# . In other words, you need to decrypt string s
# .
#
# Note that each string encrypted in this way is decrypted uniquely.
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The descriptions of the test cases follow.
#
# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the length of the encrypted message.
#
# The second line of each test case contains a string s
#  of length n
#  — the encrypted message obtained from some string a
# .
#
# Output
# For each test case, output the decrypted message a
#  on a separate line.
#
# Example
# InputCopy
# 3
# 8
# abacabac
# 5
# qzxcq
# 20
# ccooddeeffoorrcceess
# OutputCopy
# ac
# q
# codeforces
# Note
# In the first encrypted message, the letter a
#  is encrypted as aba
# , and the letter c
#  is encrypted as cabac
# .
#
# In the second encrypted message, only one letter q
#  is encrypted as qzxcq
# .
#
# In the third encrypted message, zero characters are added to each letter.