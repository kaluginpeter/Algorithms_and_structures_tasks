# C. Vasilije in Cacak
# time limit per test1 second
# memory limit per test256 megabytes
# Aca and Milovan, two fellow competitive programmers, decided to give Vasilije a problem to test his skills.
#
# Vasilije is given three positive integers: n
# , k
# , and x
# , and he has to determine if he can choose k
#  distinct integers between 1
#  and n
# , such that their sum is equal to x
# .
#
# Since Vasilije is now in the weirdest city in Serbia where Aca and Milovan live, Cacak, the problem seems weird to him. So he needs your help with this problem.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The only line of each test case contains three integers n
# , k
#  and x
#  (1≤n≤2⋅105
# , 1≤k≤n
# , 1≤x≤4⋅1010
# ) — the maximum element he can choose, the number of elements he can choose and the sum he has to reach.
#
# Note that the sum of n
#  over all test cases may exceed 2⋅105
# .
#
# Output
# For each test case output one line: "YES", if it is possible to choose k
#  distinct integers between 1
#  and n
# , such that their sum is equal to x
# , and "NO", if it isn't.
#
# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).
#
# Example
# InputCopy
# 12
# 5 3 10
# 5 3 3
# 10 10 55
# 6 5 20
# 2 1 26
# 187856 87856 2609202300
# 200000 190000 19000000000
# 28 5 2004
# 2 2 2006
# 9 6 40
# 47202 32455 613407217
# 185977 145541 15770805980
# OutputCopy
# YES
# NO
# YES
# YES
# NO
# NO
# YES
# NO
# NO
# NO
# YES
# YES
# Note
# In the first test case n=5, k=3, x=10
# , so we can choose the numbers: 2
# , 3
# , 5
# , whose sum is 10
# , so the answer is "YES".
#
# In the second test case n=5, k=3, x=3
# , there is no three numbers which satisfies the condition, so the answer is "NO". It can be shown that there are no three numbers whose sum is 3
# .