# A. Profitable Interest Rate
# time limit per test1 second
# memory limit per test256 megabytes
# Alice has a
#  coins. She can open a bank deposit called "Profitable", but the minimum amount required to open this deposit is b
#  coins.
#
# There is also a deposit called "Unprofitable", which can be opened with any amount of coins. Alice noticed that if she opens the "Unprofitable" deposit with x
#  coins, the minimum amount required to open the "Profitable" deposit decreases by 2x
#  coins. However, these coins cannot later be deposited into the "Profitable" deposit.
#
# Help Alice determine the maximum number of coins she can deposit into the "Profitable" deposit if she first deposits some amount of coins (possibly 0
# ) into the "Unprofitable" deposit. If Alice can never open the "Profitable" deposit, output 0
# .
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# A single line of each test case contains two integers a
#  and b
#  (1≤a,b≤109
# ) — the number of coins Alice has and the initial minimum amount required to open the "Profitable" deposit.
#
# Output
# For each test case, output a single integer — the maximum number of coins that Alice can deposit into the "Profitable" deposit. If Alice can never open the "Profitable" deposit, output 0
# .
#
# Example
# InputCopy
# 5
# 10 5
# 7 9
# 5 100
# 1 1
# 1 2
# OutputCopy
# 10
# 5
# 0
# 1
# 0
# Note
# In the first test case, a≥b
# , so Alice can immediately open the "Profitable" deposit with all 10
#  coins.
#
# In the second test case, Alice can open the "Unprofitable" deposit with 2
#  coins. Then she will have 5
#  coins left, but the minimum amount required to open the "Profitable" deposit will decrease by 4
#  coins, making it equal to 5
#  coins. Thus, Alice will be able to open the "Profitable" deposit with 5
#  coins.
#
# In the third test case, Alice will not be able to open the "Profitable" deposit.