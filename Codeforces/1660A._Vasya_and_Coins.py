# A. Vasya and Coins
# time limit per test1 second
# memory limit per test256 megabytes
# Vasya decided to go to the grocery store. He found in his wallet a
#  coins of 1
#  burle and b
#  coins of 2
#  burles. He does not yet know the total cost of all goods, so help him find out s
#  (s>0
# ): the minimum positive integer amount of money he cannot pay without change or pay at all using only his coins.
#
# For example, if a=1
#  and b=1
#  (he has one 1
# -burle coin and one 2
# -burle coin), then:
#
# he can pay 1
#  burle without change, paying with one 1
# -burle coin,
# he can pay 2
#  burle without change, paying with one 2
# -burle coin,
# he can pay 3
#  burle without change by paying with one 1
# -burle coin and one 2
# -burle coin,
# he cannot pay 4
#  burle without change (moreover, he cannot pay this amount at all).
# So for a=1
#  and b=1
#  the answer is s=4
# .
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤104
# ) — the number of test cases in the test.
#
# The description of each test case consists of one line containing two integers ai
#  and bi
#  (0≤ai,bi≤108
# ) — the number of 1
# -burle coins and 2
# -burles coins Vasya has respectively.
#
# Output
# For each test case, on a separate line print one integer s
#  (s>0
# ): the minimum positive integer amount of money that Vasya cannot pay without change or pay at all.
#
# Example
# InputCopy
# 5
# 1 1
# 4 0
# 0 2
# 0 0
# 2314 2374
# OutputCopy
# 4
# 5
# 1
# 1
# 7063
# Note
# The first test case of the example is clarified into the main part of the statement.
# In the second test case, Vasya has only 1
#  burle coins, and he can collect either any amount from 1
#  to 4
# , but 5
#  can't.
# In the second test case, Vasya has only 2
#  burle coins, and he cannot pay 1
#  burle without change.
# In the fourth test case you don't have any coins, and he can't even pay 1
#  burle.