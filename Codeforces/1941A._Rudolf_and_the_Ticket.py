# A. Rudolf and the Ticket
# time limit per test1 second
# memory limit per test256 megabytes
# Rudolf is going to visit Bernard, and he decided to take the metro to get to him. The ticket can be purchased at a machine that accepts exactly two coins, the sum of which does not exceed k
# .
#
# Rudolf has two pockets with coins. In the left pocket, there are n
#  coins with denominations b1,b2,…,bn
# . In the right pocket, there are m
#  coins with denominations c1,c2,…,cm
# . He wants to choose exactly one coin from the left pocket and exactly one coin from the right pocket (two coins in total).
#
# Help Rudolf determine how many ways there are to select indices f
#  and s
#  such that bf+cs≤k
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤100
# ) — the number of test cases. Then follows the description of each test case.
#
# The first line of each test case contains three natural numbers n
# , m
# , and k
#  (1≤n,m≤100,1≤k≤2000
# ) — the number of coins in the left and right pockets, and the maximum sum of two coins for the ticket payment at the counter, respectively.
#
# The second line of each test case contains n
#  integers bi
#  (1≤bi≤1000
# ) — the denominations of coins in the left pocket.
#
# The third line of each test case contains m
#  integers ci
#  (1≤ci≤1000
# ) — the denominations of coins in the right pocket.
#
# Output
# For each testcase, output a single integer — the number of ways Rudolf can select two coins, taking one from each pocket, so that the sum of the coins does not exceed k
# .
#
# Example
# InputCopy
# 4
# 4 4 8
# 1 5 10 14
# 2 1 8 1
# 2 3 4
# 4 8
# 1 2 3
# 4 2 7
# 1 1 1 1
# 2 7
# 3 4 2000
# 1 1 1
# 1 1 1 1
# OutputCopy
# 6
# 0
# 4
# 12
# Note
# Note that the pairs indicate the indices of the coins in the array, not their denominations.
#
# In the first test case, Rudolf can choose the following pairs of coins: [1,1],[1,2],[1,4],[2,1],[2,2],[2,4]
# .
#
# In the second test case, Rudolf cannot choose one coin from each pocket in any way, as the sum of any two elements from the first and second arrays will exceed the value of k=4
# .
#
# In the third test case, Rudolf can choose: [1,1],[2,1],[3,1],[4,1]
# .
#
# In the fourth test case, Rudolf can choose any coin from the left pocket and any coin from the right pocket.