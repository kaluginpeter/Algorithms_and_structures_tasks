# A. Kamilka and the Sheep
# time limit per test1 second
# memory limit per test256 megabytes
# Kamilka has a flock of n
#  sheep, the i
# -th of which has a beauty level of ai
# . All ai
#  are distinct. Morning has come, which means they need to be fed. Kamilka can choose a non-negative integer d
#  and give each sheep d
#  bunches of grass. After that, the beauty level of each sheep increases by d
# .
#
# In the evening, Kamilka must choose exactly two sheep and take them to the mountains. If the beauty levels of these two sheep are x
#  and y
#  (after they have been fed), then Kamilka's pleasure from the walk is equal to gcd(x,y)
# , where gcd(x,y)
#  denotes the greatest common divisor (GCD) of integers x
#  and y
# .
#
# The task is to find the maximum possible pleasure that Kamilka can get from the walk.
#
# Input
# Each test consists of several test cases. The first line contains one integer t
#  (1≤t≤500
# ), the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains one integer n
#  (2≤n≤100
# ), the number of sheep Kamilka has.
#
# The second line of each test case contains n
#  distinct integers a1,a2,…,an (1≤ai≤109)
#  — the beauty levels of the sheep.
#
# It is guaranteed that all ai
#  are distinct.
#
# Output
# For each test case, output a single integer: the maximum possible pleasure that Kamilka can get from the walk.
#
# Example
# InputCopy
# 4
# 2
# 1 3
# 5
# 5 4 3 2 1
# 3
# 5 6 7
# 3
# 1 11 10
# OutputCopy
# 2
# 4
# 2
# 10
# Note
# In the first test case, d=1
#  works. In this case, the pleasure is gcd(1+1, 1+3)=gcd(2, 4)=2
# . It can be shown that a greater answer cannot be obtained.
#
# In the second test case, let's take d=3
# . In this case, the pleasure is gcd(1+3, 5+3)=gcd(4, 8)=4
# . Thus, for this test case, the answer is 4
# .