# A. Dora's Set
# time limit per test1 second
# memory limit per test256 megabytes
# Dora has a set s
#  containing integers. In the beginning, she will put all integers in [l,r]
#  into the set s
# . That is, an integer x
#  is initially contained in the set if and only if l≤x≤r
# . Then she allows you to perform the following operations:
#
# Select three distinct integers a
# , b
# , and c
#  from the set s
# , such that gcd(a,b)=gcd(b,c)=gcd(a,c)=1†
# .
# Then, remove these three integers from the set s
# .
# What is the maximum number of operations you can perform?
#
# †
# Recall that gcd(x,y)
#  means the greatest common divisor of integers x
#  and y
# .
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤500
# ) — the number of test cases. The description of the test cases follows.
#
# The only line of each test case contains two integers l
#  and r
#  (1≤l≤r≤1000
# ) — the range of integers in the initial set.
#
# Output
# For each test case, output a single integer — the maximum number of operations you can perform.
#
# Example
# InputCopy
# 8
# 1 3
# 3 7
# 10 21
# 2 8
# 51 60
# 2 15
# 10 26
# 1 1000
# OutputCopy
# 1
# 1
# 3
# 1
# 2
# 3
# 4
# 250
# Note
# In the first test case, you can choose a=1
# , b=2
# , c=3
#  in the only operation, since gcd(1,2)=gcd(2,3)=gcd(1,3)=1
# , and then there are no more integers in the set, so no more operations can be performed.
#
# In the second test case, you can choose a=3
# , b=5
# , c=7
#  in the only operation.
#
# In the third test case, you can choose a=11
# , b=19
# , c=20
#  in the first operation, a=13
# , b=14
# , c=15
#  in the second operation, and a=10
# , b=17
# , c=21
#  in the third operation. After the three operations, the set s
#  contains the following integers: 12
# , 16
# , 18
# . It can be proven that it's impossible to perform more than 3
#  operations.