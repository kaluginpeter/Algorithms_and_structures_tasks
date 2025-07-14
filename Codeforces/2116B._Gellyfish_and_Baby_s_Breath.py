# B. Gellyfish and Baby's Breath
# time limit per test1 second
# memory limit per test256 megabytes
# Flower gives Gellyfish two permutations∗
#  of [0,1,…,n−1]
# : p0,p1,…,pn−1
#  and q0,q1,…,qn−1
# .
#
# Now Gellyfish wants to calculate an array r0,r1,…,rn−1
#  through the following method:
#
# For all i
#  (0≤i≤n−1
# ), ri=maxj=0i(2pj+2qi−j)
# But since Gellyfish is very lazy, you have to help her figure out the elements of r
# .
#
# Since the elements of r
#  are very large, you are only required to output the elements of r
#  modulo 998244353
# .
#
# ∗
# An array b
#  is a permutation of an array a
#  if b
#  consists of the elements of a
#  in arbitrary order. For example, [4,2,3,4]
#  is a permutation of [3,2,4,4]
#  while [1,2,2]
#  is not a permutation of [1,2,3]
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤105
# ).
#
# The second line of each test case contains n
#  integers p0,p1,…,pn−1
#  (0≤pi<n
# ).
#
# The third line of each test case contains n
#  integers q0,q1,…,qn−1
#  (0≤qi<n
# ).
#
# It is guaranteed that both p
#  and q
#  are permutations of [0,1,…,n−1]
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 105
# .
#
# Output
# For each test case, output n
#  integers r0,r1,…,rn−1
#  in a single line, modulo 998244353
# .
#
# Example
# InputCopy
# 3
# 3
# 0 2 1
# 1 2 0
# 5
# 0 1 2 3 4
# 4 3 2 1 0
# 10
# 5 8 9 3 4 0 2 7 1 6
# 9 5 1 4 0 3 2 8 7 6
# OutputCopy
# 3 6 8
# 17 18 20 24 32
# 544 768 1024 544 528 528 516 640 516 768
# Note
# In the first test case:
#
# r0=2p0+2q0=1+2=3
# r1=max(2p0+2q1,2p1+2q0)=max(1+4,4+2)=6
# r2=max(2p0+2q2,2p1+2q1,2p2+2q0)=(1+1,4+4,2+2)=8