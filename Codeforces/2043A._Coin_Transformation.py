# A. Coin Transformation
# time limit per test2 seconds
# memory limit per test512 megabytes
# Initially, you have a coin with value n
# . You can perform the following operation any number of times (possibly zero):
#
# transform one coin with value x
# , where x
#  is greater than 3
#  (x>3
# ), into two coins with value ⌊x4⌋
# .
# What is the maximum number of coins you can have after performing this operation any number of times?
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each test case consists of one line containing one integer n
#  (1≤n≤1018
# ).
#
# Output
# For each test case, print one integer — the maximum number of coins you can have after performing the operation any number of times.
#
# Example
# InputCopy
# 4
# 1
# 5
# 16
# 1000000000000000000
# OutputCopy
# 1
# 2
# 4
# 536870912
# Note
# In the first example, you have a coin of value 1
# , and you can't do anything with it. So, the answer is 1
# .
#
# In the second example, you can transform a coin of value 5
#  into two coins with value 1
# .
#
# In the third example, you can transform a coin of value 16
#  into two coins with value 4
# . Each of the resulting coins can be transformed into two coins with value 1
# .