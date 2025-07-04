# B. Expensive Number
# time limit per test1 second
# memory limit per test256 megabytes
# The cost of a positive integer n
#  is defined as the result of dividing the number n
#  by the sum of its digits.
#
# For example, the cost of the number 104
#  is 1041+0+4=20.8
# , and the cost of the number 111
#  is 1111+1+1=37
# .
#
# You are given a positive integer n
#  that does not contain leading zeros. You can remove any number of digits from the number n
#  (including none) so that the remaining number contains at least one digit and is strictly greater than zero. The remaining digits cannot be rearranged. As a result, you may end up with a number that has leading zeros.
#
# For example, you are given the number 103554
# . If you decide to remove the digits 1
# , 4
# , and one digit 5
# , you will end up with the number 035
# , whose cost is 0350+3+5=4.375
# .
#
# What is the minimum number of digits you need to remove from the number so that its cost becomes the minimum possible?
#
# Input
# The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The only line of each test case contains a positive integer n
#  (1≤n<10100
# ) without leading zeros.
#
# Output
# For each test case, output one integer on a new line — the number of digits that need to be removed from the number so that its cost becomes minimal.
#
# Example
# InputCopy
# 4
# 666
# 13700
# 102030
# 7
# OutputCopy
# 2
# 4
# 3
# 0