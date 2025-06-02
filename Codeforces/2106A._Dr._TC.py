# A. Dr. TC
# time limit per test1 second
# memory limit per test256 megabytes
# In order to test his patients' intelligence, Dr. TC created the following test.
#
# First, he creates a binary string∗
#  s
#  having n
#  characters. Then, he creates n
#  binary strings a1,a2,…,an
# . It is known that ai
#  is created by first copying s
# , then flipping the i
# 'th character (1
#  becomes 0
#  and vice versa). After creating all n
#  strings, he arranges them into a grid where the i
# 'th row is ai
# .
#
# For example,
#
# If s=101
# , a=[001,111,100]
# .
# If s=0000
# , a=[1000,0100,0010,0001]
# .
# The patient needs to count the number of 1
# s written on the board in less than a second. Can you pass the test?
#
# ∗
# A binary string is a string that only consists of characters 1
#  and 0
# .
#
# Input
# The first line of the input consists of a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤10
# ) — the length of the binary string s
# .
#
# The second line of each test case contains a single binary string s
#  of size n
# .
#
# Output
# For each test case, output a single integer, the number of 1
# s on the board.
#
# Example
# InputCopy
# 5
# 3
# 101
# 1
# 1
# 5
# 00000
# 2
# 11
# 3
# 010
# OutputCopy
# 5
# 0
# 5
# 2
# 4
# Note
# The first example is explained in the statement.
#
# For the second example, the only string written on the board will be the string 0
# ; therefore, the answer is 0
# .
#
# In the third example, the following strings will be written on the board: [10000,01000,00100,00010,00001]
# ; so there are five 1
# s written on the board.