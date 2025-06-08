# C. Racing
# time limit per test2 seconds
# memory limit per test256 megabytes
# In 2077, a sport called hobby-droning is gaining popularity among robots.
#
# You already have a drone, and you want to win. For this, your drone needs to fly through a course with n
#  obstacles.
#
# The i
# -th obstacle is defined by two numbers li,ri
# . Let the height of your drone at the i
# -th obstacle be hi
# . Then the drone passes through this obstacle if li≤hi≤ri
# . Initially, the drone is on the ground, meaning h0=0
# .
#
# The flight program for the drone is represented by an array d1,d2,…,dn
# , where hi−hi−1=di
# , and 0≤di≤1
# . This means that your drone either does not change height between obstacles or rises by 1
# . You already have a flight program, but some di
#  in it are unknown and marked as −1
# . Replace the unknown di
#  with numbers 0
#  and 1
#  to create a flight program that passes through the entire obstacle course, or report that it is impossible.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# In the first line of each test case, an integer n
#  (1≤n≤2⋅105)
#  is given — the size of the array d
# .
#
# In the second line of each test case, there are n
#  integers d1,d2,…,dn
#  (−1≤di≤1
# ) — the elements of the array d
# . di=−1
#  means that this di
#  is unknown to you.
#
# Next, there are n
#  lines containing 2
#  integers li,ri
#  (0≤li≤ri≤n
# ) — descriptions of the obstacles.
#
# It is guaranteed that the sum of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output n
#  integers d1,d2,…,dn
# , if it is possible to correctly restore the array d
# , or −1
#  if it is not possible.
#
# Example
# InputCopy
# 5
# 4
# 0 -1 -1 1
# 0 4
# 1 2
# 2 4
# 1 4
# 3
# 0 -1 -1
# 0 1
# 2 2
# 0 3
# 2
# -1 -1
# 0 0
# 2 2
# 8
# -1 -1 1 -1 -1 0 0 -1
# 0 0
# 0 1
# 0 2
# 0 2
# 1 3
# 0 4
# 2 5
# 4 5
# 1
# 0
# 1 1
# OutputCopy
# 0 1 1 1
# -1
# -1
# 0 1 1 0 1 0 0 1
# -1
# Note
# In the first test case, one possible answer is d=[0,1,1,1]
# . The array h
#  will be [0,0+1,0+1+1,0+1+1+1]=[0,1,2,3]
# . This array meets the conditions of the problem.
#
# In the second test case, it can be proven that there is no suitable array d
# , so the answer is −1
# .