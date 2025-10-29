# B. Strange Machine
# time limit per test1.5 seconds
# memory limit per test256 megabytes
#
# You are given n
#  machines arranged in a circle, where n
#  is at most 20
# . Each machine is either of type A or type B. The machines are numbered clockwise from 1
#  to n
# , and the type of the i
# -th machine is denoted by si
# . Each machine takes an integer x
#  and updates it according to its type:
#
# Type A: Decrease x
#  by 1
# . Formally, update x:=x−1
# .
# Type B: Replace x
#  with the floor of half its value. Formally, update x:=⌊x2⌋
# , where ⌊y⌋
#  denotes the floor of y
# , which is the greatest integer less than or equal to y
# .
# You are given q
#  queries, each consisting of a single integer a
# . In each query, you start at machine 1
#  holding an integer a
# . Each second, the following two actions occur in order:
#
# The current machine updates a
#  according to its type.
# Then, move one step clockwise to the next machine. Formally
# If you are at machine i
#  where 1≤i≤n−1
# , move to machine i+1
# .
# If you are at machine n
# , move to machine 1
# .
# This process continues until your integer a
#  becomes 0
# . For each query, determine the number of seconds required for a
#  to reach 0
# .
#
# Note that all queries are independent of each other.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and q
#  (1≤n≤20
# , 1≤q≤104
# ) — the number of machines, and the number of queries, respectively.
#
# The second line of each test case contains a string s
#  (|s|=n
#  and si=A or B
# ) — the types of the machines.
#
# The third line of each test case contains q
#  integers a1,a2,…,aq
#  (1≤ai≤109
# ) — the initial integer of each query.
#
# Note that there are no constraints on the sum of n
#  over all test cases.
#
# It is guaranteed that the sum of q
#  over all test cases does not exceed 104
# .
#
# Output
# For each test case, output q
#  integers representing the answers to each query.
#
# Example
# InputCopy
# 3
# 2 2
# BA
# 3 4
# 1 1
# B
# 20
# 6 4
# BAABBA
# 2 8 32 95
# OutputCopy
# 2
# 3
# 5
# 2
# 5
# 8
# 11
# Note
# In the first test case, the queries are as follows:
#
# Query 1
# : a=3
# Start at machine 1
# . Machine 1
#  replaces a
#  with the floor of half its value. Now, a=⌊32⌋=1
# .
# Move to machine 2
# . Machine 2
#  decreases a
#  by 1
# . Now, a=1−1=0
# .
# Therefore, it takes 2
#  seconds for a
#  to reach 0
# .
# Query 2
# : a=4
# Start at machine 1
# . Machine 1
#  replaces a
#  with the floor of half its value. Now, a=⌊42⌋=2
# .
# Move to machine 2
# . Machine 2
#  decreases a
#  by 1
# . Now, a=2−1=1
# .
# Move back to machine 1
# . Machine 1
#  replaces a
#  with the floor of half its value. Now, a=⌊12⌋=0
# .
# Therefore, it takes 3
#  seconds for a
#  to reach 0
# .
# In the second test case, there is only one query with a=20
# :
#
# Start at machine 1
# . Machine 1
#  replaces a
#  with the floor of half its value. Now, a=⌊202⌋=10
# .
# Move to machine 1
# . Machine 1
#  replaces a
#  with the floor of half its value. Now, a=⌊102⌋=5
# .
# Move to machine 1
# . Machine 1
#  replaces a
#  with the floor of half its value. Now, a=⌊52⌋=2
# .
# Move to machine 1
# . Machine 1
#  replaces a
#  with the floor of half its value. Now, a=⌊22⌋=1
# .
# Move to machine 1
# . Machine 1
#  replaces a
#  with the floor of half its value. Now, a=⌊12⌋=0
# .
# Therefore, it takes 5
#  seconds for a
#  to reach 0
# .