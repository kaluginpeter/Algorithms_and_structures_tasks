# B. New Bakery
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Bob decided to open a bakery. On the opening day, he baked n
#  buns that he can sell. The usual price of a bun is a
#  coins, but to attract customers, Bob organized the following promotion:
#
# Bob chooses some integer k
#  (0≤k≤min(n,b)
# ).
# Bob sells the first k
#  buns at a modified price. In this case, the price of the i
# -th (1≤i≤k
# ) sold bun is (b−i+1)
#  coins.
# The remaining (n−k)
#  buns are sold at a
#  coins each.
# Note that k
#  can be equal to 0
# . In this case, Bob will sell all the buns at a
#  coins each.
#
# Help Bob determine the maximum profit he can obtain by selling all n
#  buns.
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The only line of each test case contains three integers n
# , a
# , and b
#  (1≤n,a,b≤109
# ) — the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price.
#
# Output
# For each test case, output a single integer — the maximum profit that Bob can obtain.
#
# Example
# inputCopy
# 7
# 4 4 5
# 5 5 9
# 10 10 5
# 5 5 11
# 1000000000 1000000000 1000000000
# 1000000000 1000000000 1
# 1000 1 1000
# outputCopy
# 17
# 35
# 100
# 45
# 1000000000000000000
# 1000000000000000000
# 500500
# Note
# In the first test case, it is optimal for Bob to choose k=1
# . Then he will sell one bun for 5
#  coins, and three buns at the usual price for 4
#  coins each. Then the profit will be 5+4+4+4=17
#  coins.
#
# In the second test case, it is optimal for Bob to choose k=5
# . Then he will sell all the buns at the modified price and obtain a profit of 9+8+7+6+5=35
#  coins.
#
# In the third test case, it is optimal for Bob to choose k=0
# . Then he will sell all the buns at the usual price and obtain a profit of 10⋅10=100
#  coins.