# B. Down with Brackets
# time limit per test1 second
# memory limit per test256 megabytes
# In 2077, robots decided to get rid of balanced bracket sequences once and for all!
#
# A bracket sequence is called balanced if it can be constructed by the following formal grammar.
#
# The empty sequence ∅
#  is balanced.
# If the bracket sequence A
#  is balanced, then (A)
#  is also balanced.
# If the bracket sequences A
#  and B
#  are balanced, then the concatenated sequence AB
#  is also balanced.
# You are the head of the department for combating balanced bracket sequences, and your main task is to determine which brackets you can destroy and which you cannot.
#
# You are given a balanced bracket sequence represented by a string s
# , consisting of the characters ( and ). Since the robots' capabilities are not limitless, they can remove exactly one opening bracket and exactly one closing bracket from the string.
#
# Your task is to determine whether the robots can delete such two brackets so that the string s
#  is no longer a balanced bracket sequence.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# Each test case consists of a single string s
#  (2≤|s|≤2⋅105
# ) — a sequence of the characters ( and ).
#
# It is guaranteed that s
#  is a balanced bracket sequence.
#
# It is also guaranteed that the sum of |s|
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output "YES" if the robots can make the string stop being a balanced bracket sequence, and "NO" otherwise.
#
# You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
#
# Example
# InputCopy
# 4
# (())
# (())()()
# ()
# (())(())
# OutputCopy
# NO
# YES
# NO
# YES
# Note
# In the first test case, it can be shown that the robots will not be able to break the correct bracket sequence.
#
# In the second test case, one of the options for removing brackets is as follows:
#
# (())()()→(()))(
# , which is not a correct bracket sequence.
#
# In the fourth test case, one of the options for removal is as follows:
#
# (())(())→())(()
# , which is not a correct bracket sequence.