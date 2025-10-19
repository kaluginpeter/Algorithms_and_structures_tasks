# C. Beautiful XOR
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given two integers a
#  and b
# . You are allowed to perform the following operation any number of times (including zero):
#
# choose any integer x
#  such that 0≤x≤a
#  (the current value of a
# , not initial),
# set a:=a⊕x
# . Here, ⊕
#  represents the bitwise XOR operator.
# After performing a sequence of operations, you want the value of a
#  to become exactly b
# .
#
# Find a sequence of at most 100
#  operations (values of x
#  used in each operation) that transforms a
#  into b
# , or report that it is impossible.
#
# Note that you are not required to find the minimum number of operations, but any valid sequence of at most 100
#  operations.
#
# Input
# The first line of input contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case contains two integers a
#  and b
#  (1≤a,b≤109
# ).
#
# Output
# For each test case, if it is impossible to obtain b
#  from a
#  using the allowed operations, print a single line containing −1
# .
#
# Otherwise, on the first line print a single integer k
#  (0≤k≤100
# ) — the number of operations. On the second line print k
#  integers (x1,x2,…,xk
# ) — the chosen values of x
#  in the order you apply them.
#
# If there are multiple valid sequences, you may print any one of them.
#
# Example
# InputCopy
# 6
# 9 6
# 13 13
# 292 929
# 405 400
# 998 244
# 244 353
# OutputCopy
# 2
# 7 8
# 0
# -1
# 1
# 5
# 2
# 25 779
# -1
# Note
# For the first test case,
#
# choose x=7
# , now a
#  becomes equal to 9⊕7=14
# .
# choose x=8
# , now a
#  becomes equal to 14⊕8=6
# .
# Thus, we can make a=b
# .
# For the fourth test case, choosing x=5
#  makes a=b
# .