# B. Like the Bitset
# time limit per test1 second
# memory limit per test256 megabytes
#
# You are given a binary string∗
#  s
#  of length n
# , as well as an integer k
# .
#
# Aquawave wants to construct a permutation†
#  p
#  of length n
# , so that for each 1≤i≤n
# , where si=1
# , the following holds:
#
# For each interval [l,r]
#  (1≤l≤r≤n
# ) whose length is at least k
#  (i.e. r−l+1≥k
# ), if it covers position i
#  (i.e. l≤i≤r
# ), then the maximum element among pl,pl+1,…,pr
#  is not pi
# .
# Note that there are no such constraints on indices with si=0
# .
#
# You have to find such a permutation, or determine that such permutations do not exist.
#
# ∗
# A binary string is a string where each character is either 0
#  or 1
# .
#
# †
# A permutation of length n
#  is an array consisting of n
#  distinct integers from 1
#  to n
#  in arbitrary order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (n=3
#  but there is 4
#  in the array).
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤n≤2⋅105
# , 1≤k≤n
# ) — the length of s
#  and the integer in the statements.
#
# The second line contains the binary string s
#  of length n
#  (si=0
#  or 1
# ).
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case:
#
# If there is at least one possible permutation:
# Print "YES" in the first line of output;
# Then, print n
#  integers p1,p2,…,pn
#  (1≤pi≤n
# , all pi
# -s are distinct) in the second line — the permutation you constructed.
# Otherwise, print "NO" in the single line of output.
# You can output the tokens in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# If there are multiple answers, you may output any of them.
#
# Example
# InputCopy
# 6
# 2 1
# 00
# 4 3
# 0010
# 5 2
# 11011
# 7 5
# 1111110
# 8 4
# 00101011
# 10 2
# 1000000010
# OutputCopy
# YES
# 1 2
# YES
# 1 4 3 2
# NO
# NO
# YES
# 6 5 2 3 4 8 1 7
# YES
# 1 2 3 4 5 6 7 9 8 10
# Note
# In the first test case, you can output an arbitrary permutation of length n=2
# , since all si
# -s are equal to 0
# .
#
# In the second test case, p=[1,4,3,2]
#  is a valid answer because:
#
# The only position where si=1
#  is i=3
# . There are three distinct intervals [l,r]
#  covering index 3
# , whose length is at least k=3
# : [1,3]
# , [1,4]
# , and [2,4]
# ;
# And, for each of the three intervals, the maximum element among pl,…,pr
#  should be p2=4
# , which is not equal to p3=3
# .