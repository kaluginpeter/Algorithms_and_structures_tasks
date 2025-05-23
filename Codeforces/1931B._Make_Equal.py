# B. Make Equal
# time limit per test2 seconds
# memory limit per test256 megabytes
# There are n
#  containers of water lined up, numbered from left to right from 1
#  to n
# . Each container can hold any amount of water; initially, the i
# -th container contains ai
#  units of water. The sum of ai
#  is divisible by n
# .
#
# You can apply the following operation any (possibly zero) number of times: pour any amount of water from the i
# -th container to the j
# -th container, where i
#  must be less than j
#  (i.e. i<j
# ). Any index can be chosen as i
#  or j
#  any number of times.
#
# Determine whether it is possible to make the amount of water in all containers the same using this operation.
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. Then the descriptions of the test cases follow.
#
# The first line of each test case contains a single integer n
#  (1≤n≤2⋅105
# ) — the number of containers with water.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (0≤ai≤109
# ) — the amounts of water in the containers. It is guaranteed that the sum of ai
#  in each test case does not exceed 2⋅109
# . Also, the sum of ai
#  is divisible by n
# .
#
# It is guaranteed that the sum of n
#  over all test cases in the input does not exceed 2⋅105
# .
#
# Output
# Output t
#  lines, each of which is the answer to the corresponding test case. As the answer, output "YES" if it is possible to make the amount of water in all containers the same using the described operation. Otherwise, output "NO".
#
# You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
#
# Example
# InputCopy
# 6
# 1
# 43
# 2
# 1 3
# 5
# 4 5 2 1 3
# 3
# 1 2 3
# 7
# 4 5 5 0 6 4 4
# 7
# 6 5 5 1 3 4 4
# OutputCopy
# YES
# NO
# YES
# NO
# NO
# YES
# Note
# In the third test case of the example (a=[4,5,2,1,3]
# ), you can proceed as follows:
#
# pour 1
#  unit of water from the first vessel to the fourth, then a=[3,5,2,2,3]
# ;
# pour 1
#  unit of water from the second vessel to the third, then a=[3,4,3,2,3]
# ;
# pour 1
#  unit of water from the second vessel to the fourth, then a=[3,3,3,3,3]
# .