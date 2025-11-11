# A. Sequence Game
# time limit per test1 second
# memory limit per test256 megabytes
# Given an integer sequence of length n
#  denoted as a1,a2,…,an
#  and an integer x
# .
#
# You can perform the following operation: select two adjacent numbers ai
#  and ai+1
#  and replace them with an integer y
# , which satisfies min(ai,ai+1)≤y≤max(ai,ai+1)
# . After the replacement, the original ai
#  and ai+1
#  are removed from the sequence, and the elements are renumbered from 1
#  to n−1
# .
#
# For example, for a=[1,2,4,5]
#  you can select a2=2
#  and a3=4
# , and replace them with 3
# . After that, a
#  becomes [1,3,5]
# . However, you cannot select a1=1
#  and a2=2
#  and replace them with 3
#  (since y
#  is bigger than max(ai,ai+1)
# , nor can you select a1=1
#  and a3=4
#  (the selected numbers should be adjacent).
#
# Clearly, after performing n−1
#  operations, only one number will remain. The question is whether this final number can be exactly equal to x
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases T
#  (1≤T≤500
# ). The description of the test cases follows.
#
# The first line of each test case contains one integer n
#  (1≤n≤100
# ).
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (−109≤ai≤109
# ).
#
# The third line of each test case contains one integer x
#  (−109≤x≤109
# ).
#
# Output
# For each test case, output "YES" (without quotes) if the final number can be exactly equal to x
# , and "NO" otherwise.
#
# You can output "YES" and "NO" in any case (for example, strings "yES", "yes" and "Yes" will be recognized as a positive response).
#
# Example
# InputCopy
# 3
# 3
# 2 7 5
# 4
# 5
# -1 3 7 -9 -2
# 8
# 6
# 1 -1 -4 5 1 -4
# -2
# OutputCopy
# YES
# NO
# YES
# Note
# In the first test case, you can first select a2=7
#  and a3=5
# , and replace them with 6
# . After that, a
#  becomes [2,6]
# . Now you can select a1=2
#  and a2=6
# , and replace them with 4
# .
#
# In the second test case, it can be shown that the final number can never be 8
# .