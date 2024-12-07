# B. Multiply by 2, divide by 6
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an integer n
# . In one move, you can either multiply n
#  by two or divide n
#  by 6
#  (if it is divisible by 6
#  without the remainder).
#
# Your task is to find the minimum number of moves needed to obtain 1
#  from n
#  or determine if it's impossible to do that.
#
# You have to answer t
#  independent test cases.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤2⋅104
# ) — the number of test cases. Then t
#  test cases follow.
#
# The only line of the test case contains one integer n
#  (1≤n≤109
# ).
#
# Output
# For each test case, print the answer — the minimum number of moves needed to obtain 1
#  from n
#  if it's possible to do that or -1 if it's impossible to obtain 1
#  from n
# .
#
# Example
# InputCopy
# 7
# 1
# 2
# 3
# 12
# 12345
# 15116544
# 387420489
# OutputCopy
# 0
# -1
# 2
# -1
# -1
# 12
# 36
# Note
# Consider the sixth test case of the example. The answer can be obtained by the following sequence of moves from the given integer 15116544
# :
#
# Divide by 6
#  and get 2519424
# ;
# divide by 6
#  and get 419904
# ;
# divide by 6
#  and get 69984
# ;
# divide by 6
#  and get 11664
# ;
# multiply by 2
#  and get 23328
# ;
# divide by 6
#  and get 3888
# ;
# divide by 6
#  and get 648
# ;
# divide by 6
#  and get 108
# ;
# multiply by 2
#  and get 216
# ;
# divide by 6
#  and get 36
# ;
# divide by 6
#  and get 6
# ;
# divide by 6
#  and get 1
# .