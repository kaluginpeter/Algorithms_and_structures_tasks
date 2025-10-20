# A. Notelock
# time limit per test1 second
# memory limit per test256 megabytes
# Teto is playing the hit rhythm game osu!. The game can be described by a binary string∗
#  s
#  of length n
#  and a positive integer k
#  where the following will happen in order:
#
# You will choose some positions in s
#  to protect.
# Then for each i
#  (1≤i≤n
# ) in increasing order, Teto can set si
#  to 0
#  if all the following are true:
# si=1
# ,
# si
#  is not protected,
# the previous k−1
#  elements do not contain 1
# . More formally, 1
#  does not occur in smax(1,i−k+1),…,si−1
# .
# You dislike Teto (for some reason). So determine the minimum number of positions you need to protect to force her to leave s
#  unchanged.
#
# ∗
# A binary string is a string that only consists of characters 0
#  and 1
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The first line of each testcase contains integers n
#  and k
#  (2≤n≤1000
# ; 2≤k≤n
# ) — the length of s
#  and k
# .
#
# The second line of each test case contains a binary string s
#  of length n
#  consisting of characters 0
#  and 1
# .
#
# The sum of n
#  across all testcases does not exceed 1000
# .
#
# Output
# For each testcase, output the minimum number of positions you need to protect to force Teto to leave the string unchanged.
#
# Example
# InputCopy
# 9
# 2 2
# 11
# 6 6
# 100001
# 5 3
# 10000
# 7 2
# 1010101
# 7 4
# 0000001
# 3 3
# 010
# 3 2
# 011
# 7 4
# 1001001
# 8 3
# 00000000
# OutputCopy
# 1
# 1
# 1
# 4
# 1
# 1
# 1
# 1
# 0
# Note
# For the first testcase, you can protect the first element and have: s=11
# . Now Teto cannot change s1
#  because it is protected and cannot change s2
#  because s1=1
# . It can be proven this is optimal.
#
# For the second testcase, you can protect only the first element and have s=100001
# . Teto cannot change s1
#  because it is protected and she cannot change s6
#  because there is 1
#  in the previous k−1
#  elements (100001
# ).
#
# For the fourth testcase, you must protect s1,s3,s5,s7
#  and have s=1010101
# . It can be shown that this is optimal. For example, if you did not protect s3
# , then Teto can change it to 0
#  (1010101
# )