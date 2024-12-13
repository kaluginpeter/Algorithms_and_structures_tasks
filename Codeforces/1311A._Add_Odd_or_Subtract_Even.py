# A. Add Odd or Subtract Even
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given two positive integers a
#  and b
# .
#
# In one move, you can change a
#  in the following way:
#
# Choose any positive odd integer x
#  (x>0
# ) and replace a
#  with a+x
# ;
# choose any positive even integer y
#  (y>0
# ) and replace a
#  with a−y
# .
# You can perform as many such operations as you want. You can choose the same numbers x
#  and y
#  in different moves.
#
# Your task is to find the minimum number of moves required to obtain b
#  from a
# . It is guaranteed that you can always obtain b
#  from a
# .
#
# You have to answer t
#  independent test cases.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Then t
#  test cases follow. Each test case is given as two space-separated integers a
#  and b
#  (1≤a,b≤109
# ).
#
# Output
# For each test case, print the answer — the minimum number of moves required to obtain b
#  from a
#  if you can perform any number of moves described in the problem statement. It is guaranteed that you can always obtain b
#  from a
# .
#
# Example
# InputCopy
# 5
# 2 3
# 10 10
# 2 4
# 7 4
# 9 3
# OutputCopy
# 1
# 0
# 2
# 2
# 1
# Note
# In the first test case, you can just add 1
# .
#
# In the second test case, you don't need to do anything.
#
# In the third test case, you can add 1
#  two times.
#
# In the fourth test case, you can subtract 4
#  and add 1
# .
#
# In the fifth test case, you can just subtract 6
# .