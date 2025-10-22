# D. Beautiful Permutation
# time limit per test2 seconds
# memory limit per test256 megabytes
# This is an interactive problem.
#
# There is a permutation∗
#  p
#  of length n
# .
#
# Someone secretly chose two integers l,r
#  (1≤l≤r≤n
# ) and modified the permutation in the following way:
#
# For every index i
#  such that l≤i≤r
# , set pi:=pi+1
# .
# Let a
#  denote the resulting array obtained by modifying the permutation.
#
# You are given an integer n
#  denoting the length of the permutation p
# .
#
# In one query, you are allowed to choose two integers l,r
#  (1≤l≤r≤n
# ) and ask for the sum of the subarray either of the original permutation p[l…r]
#  or of the modified array a[l…r]
# . The answer to such a query will be the corresponding integer sum.
#
# Your task is to find the pair (l,r)
#  that was chosen to obtain a
#  in no more than 40
#  queries.
#
# ∗
# A permutation of length n
#  is an array consisting of n
#  distinct integers from 1
#  to n
#  in any order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (the number 2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (n=3
# , but the array contains 4
# ).
#
# Input
# The first line of input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each test case contains a single integer n
#  (1≤n≤2⋅104
# ) — the length of the permutation.
#
# It is guaranteed that the sum of n
#  over all the test cases does not exceed 2⋅104
# .
#
# Interaction
# The interaction for each test case begins by reading the integer n
# .
#
# You can ask two types of queries.
#
# Print "1 l r
# " (1≤l≤r≤n
# ).
# In response, you should read a line containing a single integer x
#  — the sum of the subarray of the original permutation. (Formally, x=pl+pl+1+⋯+pr
# ).
#
#
# Print "2 l r
# " (1≤l≤r≤n
# ).
# In response, you should read a line containing a single integer y
#  — the sum of the subarray of the modified array. (Formally, y=al+al+1+⋯+ar
# ).
#
# The permutation p
#  and the chosen integers l
# , r
#  are fixed beforehand and can't be changed during the time of interaction.
#
# You can output the final answer by printing "! l r
# ", where l
# , r
#  denote the integers that were chosen to obtain a
# . After printing the answer, your program should proceed to the next test case or terminate if there are no more.
#
# You can ask no more than 40
#  queries per testcase. Printing the answer doesn't count as a query. If your program performs more than 40
#  queries for one test case or makes an invalid query, you may receive a Wrong Answer verdict.
#
# After printing a query, do not forget to output the end of line and flush∗
#  the output. Otherwise, you will get Idleness limit exceeded.
#
# Hacks
#
# To make a hack, use the following test format.
#
# The first line should contain a single integer t
#  (1≤t≤104)
#  — the number of testcases.
#
# The first line of each test case should contain a single integer n
#  (1≤n≤2⋅104
# ) — the length of the permutation p
# .
#
# The second line of each test case should contain n
#  integers pi
#  (1≤pi≤n
# ) — denoting the permutation p
# .
#
# The third line of each test case should contain two space-separated integers l
# , r
#  (1≤l≤r≤n
# ) — the chosen integers.
#
# For example, the following is the hack format of the example test:
#
# 2
# 3
# 3 1 2
# 2 2
# 4
# 2 1 3 4
# 2 4
# ∗
# To flush, use:
#
# fflush(stdout) or cout.flush() in C++;
# System.out.flush() in Java;
# flush(output) in Pascal;
# stdout.flush() in Python;
# see documentation for other languages
# Example
# InputCopy
# 2
#
#
# 3
#
# 4
#
# 5
#
#
# 4
#
# 8
#
# 8
#
# 9
# OutputCopy
#
# 1 1 2
#
# 2 1 2
#
# ! 2 2
#
# 1 2 4
#
# 2 1 3
#
# 2 3 4
#
# ! 2 4
# Note
# For the first testcase, p=[3,1,2]
#  and l=2
# , r=2
# . Hence, the modified array a
#  will be equal to [3,2,2]
# .
#
# So, querying "1 1 2
# " gives p1+p2=3+1=4
# . And querying "2 1 2
# " gives a1+a2=3+2=5
# .
#
# For the second testcase, p=[2,1,3,4]
#  and l=2
# , r=4
# .
#
# Note that the queries shown in the sample test are only for demonstration purposes, and they may not correspond to any optimal solution.