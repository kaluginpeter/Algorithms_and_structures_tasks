# A. Gregor and Cryptography
# time limit per test1 second
# memory limit per test256 megabytes
# Gregor is learning about RSA cryptography, and although he doesn't understand how RSA works, he is now fascinated with prime numbers and factoring them.
#
# Gregor's favorite prime number is P
# . Gregor wants to find two bases of P
# . Formally, Gregor is looking for two integers a
#  and b
#  which satisfy both of the following properties.
#
# Pmoda=Pmodb
# , where xmody
#  denotes the remainder when x
#  is divided by y
# , and
# 2≤a<b≤P
# .
# Help Gregor find two bases of his favorite prime number!
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ).
#
# Each subsequent line contains the integer P
#  (5≤P≤109
# ), with P
#  guaranteed to be prime.
#
# Output
# Your output should consist of t
#  lines. Each line should consist of two integers a
#  and b
#  (2≤a<b≤P
# ). If there are multiple possible solutions, print any.
#
# Example
# InputCopy
# 2
# 17
# 5
# OutputCopy
# 3 5
# 2 4
# Note
# The first query is P=17
# . a=3
#  and b=5
#  are valid bases in this case, because 17mod3=17mod5=2
# . There are other pairs which work as well.
#
# In the second query, with P=5
# , the only solution is a=2
#  and b=4
# .