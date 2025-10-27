# A. Pizza Time
# time limit per test1 second
# memory limit per test256 megabytes
#
# Hao and Alex are good friends. After winning a coding competition together, they received a huge pizza as their prize.
#
# Initially, they are given n
#  slices of pizza. Each day, the following process takes place:
#
# If there are at most 2
#  slices remaining, Alex eats all of them.
# Otherwise, let m
#  be the current number of slices (m≥3
# ). Hao splits them into three groups of sizes m1
# , m2
# , and m3
#  such that:
# m1+m2+m3=m and 1≤m1≤m2≤m3.
#
# Then:
#
# Hao eats m1
#  slices (the smallest group).
# Alex eats m2
#  slices (the middle group).
# The remaining m3
#  slices (the largest group) are carried over to the next day.
# Your task is to determine the maximum total number of slices Hao can eat if he always chooses the partition optimally.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.
#
# The first and only line of each test case contains a single integer n
#  (3≤n≤109
# ) — the initial number of pizza slices.
#
# Note that there are no constraints on the sum of n
#  over all test cases.
#
# Output
# For each test case, output a single integer representing the maximum total number of slices Hao can eat.
#
# Example
# InputCopy
# 3
# 8
# 4
# 3
# OutputCopy
# 3
# 1
# 1
# Note
# In the first test case, Hao can eat 3
#  slices as follows:
#
# Split into m1=2
# , m2=3
# , and m3=3
# . Hao eats 2
#  slices, Alex eats 3
#  slices, and the remaining 3
#  slices are carried over to the next day.
# Split into m1=1
# , m2=1
# , and m3=1
# . Hao eats 1
#  slice, Alex eats 1
#  slice, and the remaining 1
#  slice is carried over to the next day.
# Only 1
#  slice remains, so Alex eats it.
# In the second test case, Hao can eat 1
#  slice as follows:
#
# Split into m1=1
# , m2=1
# , and m3=2
# . Hao eats 1
#  slice, Alex eats 1
#  slice, and the remaining 2
#  slices are carried over to the next day.
# Only 2
#  slices remain, so Alex eats them all.