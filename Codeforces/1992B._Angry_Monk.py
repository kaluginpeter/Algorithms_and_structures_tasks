# B. Angry Monk
# time limit per test2 seconds
# memory limit per test256 megabytes
# To celebrate his recovery, k1o0n has baked an enormous n
#  metres long potato casserole.
#
# Turns out, Noobish_Monk just can't stand potatoes, so he decided to ruin k1o0n's meal. He has cut it into k
#  pieces, of lengths a1,a2,…,ak
#  meters.
#
# k1o0n wasn't keen on that. Luckily, everything can be fixed. In order to do that, k1o0n can do one of the following operations:
#
# Pick a piece with length ai≥2
#  and divide it into two pieces with lengths 1
#  and ai−1
# . As a result, the number of pieces will increase by 1
# ;
# Pick a slice ai
#  and another slice with length aj=1
#  (i≠j
# ) and merge them into one piece with length ai+1
# . As a result, the number of pieces will decrease by 1
# .
# Help k1o0n to find the minimum number of operations he needs to do in order to merge the casserole into one piece with length n
# .
#
# For example, if n=5
# , k=2
#  and a=[3,2]
# , it is optimal to do the following:
#
# Divide the piece with length 2
#  into two pieces with lengths 2−1=1
#  and 1
# , as a result a=[3,1,1]
# .
# Merge the piece with length 3
#  and the piece with length 1
# , as a result a=[4,1]
# .
# Merge the piece with length 4
#  and the piece with length 1
# , as a result a=[5]
# .
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ).
#
# Description of each test case consists of two lines. The first line contains two integers n
#  and k
#  (2≤n≤109
# , 2≤k≤105
# ) — length of casserole and the number of pieces.
#
# The second line contains k
#  integers a1,a2,…,ak
#  (1≤ai≤n−1
# , ∑ai=n
# ) — lengths of pieces of casserole, which Noobish_Monk has cut.
#
# It is guaranteed that the sum of k
#  over all t
#  test cases doesn't exceed 2⋅105
# .
#
# Output
# For each test case, output the minimum number of operations K1o0n needs to restore his pie after the terror of Noobish_Monk.
#
# Example
# InputCopy
# 4
# 5 3
# 3 1 1
# 5 2
# 3 2
# 11 4
# 2 3 1 5
# 16 6
# 1 6 1 1 1 6
# OutputCopy
# 2
# 3
# 9
# 15