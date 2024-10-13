# B. Equal Candies
# time limit per test1 second
# memory limit per test256 megabytes
# There are n
#  boxes with different quantities of candies in each of them. The i
# -th box has ai
#  candies inside.
#
# You also have n
#  friends that you want to give the candies to, so you decided to give each friend a box of candies. But, you don't want any friends to get upset so you decided to eat some (possibly none) candies from each box so that all boxes have the same quantity of candies in them. Note that you may eat a different number of candies from different boxes and you cannot add candies to any of the boxes.
#
# What's the minimum total number of candies you have to eat to satisfy the requirements?
#
# Input
# The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains an integer n
#  (1≤n≤50
# ) — the number of boxes you have.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤107
# ) — the quantity of candies in each box.
#
# Output
# For each test case, print a single integer denoting the minimum number of candies you have to eat to satisfy the requirements.
#
# Example
# inputCopy
# 5
# 5
# 1 2 3 4 5
# 6
# 1000 1000 5 1000 1000 1000
# 10
# 1 2 3 5 1 2 7 9 13 5
# 3
# 8 8 8
# 1
# 10000000
# outputCopy
# 10
# 4975
# 38
# 0
# 0
# Note
# For the first test case, you can eat 1
#  candy from the second box, 2
#  candies from the third box, 3
#  candies from the fourth box and 4
#  candies from the fifth box. Now the boxes have [1,1,1,1,1]
#  candies in them and you ate 0+1+2+3+4=10
#  candies in total so the answer is 10
# .
#
# For the second test case, the best answer is obtained by making all boxes contain 5
#  candies in them, thus eating 995+995+0+995+995+995=4975
#  candies in total.