# D. Buying Shovels
# time limit per test2 seconds
# memory limit per test256 megabytes
# Polycarp wants to buy exactly n
#  shovels. The shop sells packages with shovels. The store has k
#  types of packages: the package of the i
# -th type consists of exactly i
#  shovels (1≤i≤k
# ). The store has an infinite number of packages of each type.
#
# Polycarp wants to choose one type of packages and then buy several (one or more) packages of this type. What is the smallest number of packages Polycarp will have to buy to get exactly n
#  shovels?
#
# For example, if n=8
#  and k=7
# , then Polycarp will buy 2
#  packages of 4
#  shovels.
#
# Help Polycarp find the minimum number of packages that he needs to buy, given that he:
#
# will buy exactly n
#  shovels in total;
# the sizes of all packages he will buy are all the same and the number of shovels in each package is an integer from 1
#  to k
# , inclusive.
# Input
# The first line contains an integer t
#  (1≤t≤100
# ) — the number of test cases in the input. Then, t
#  test cases follow, one per line.
#
# Each test case consists of two positive integers n
#  (1≤n≤109
# ) and k
#  (1≤k≤109
# ) — the number of shovels and the number of types of packages.
#
# Output
# Print t
#  answers to the test cases. Each answer is a positive integer — the minimum number of packages.
#
# Example
# InputCopy
# 5
# 8 7
# 8 1
# 6 10
# 999999733 999999732
# 999999733 999999733
# OutputCopy
# 2
# 8
# 1
# 999999733
# 1
# Note
# The answer to the first test case was explained in the statement.
#
# In the second test case, there is only one way to buy 8
#  shovels — 8
#  packages of one shovel.
#
# In the third test case, you need to buy a 1
#  package of 6
#  shovels.