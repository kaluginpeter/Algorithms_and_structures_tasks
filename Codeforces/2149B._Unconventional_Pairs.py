# B. Unconventional Pairs
# time limit per test2 seconds
# memory limit per test256 megabytes
# A popular reality show Unconventional Pairs has been launched in the city. According to the rules of the show, participants are paired in an unusual way: with an even number of people, all participants must be in pairs.
#
# Petya has an array of n
#  integers a1,a2,…,an
# . It is known that n
#  is even. Petya must divide the participants (numbers) into exactly n2
#  pairs (ap1,aq1),(ap2,aq2),…(apn2,aqn2)
# . Each index can be included in no more than one pair.
#
# For a pair (x,y)
# , its difference is defined as |x−y|
# . Petya wants to form unconventional pairs such that the maximum difference among all pairs is minimized.
#
# Determine the minimum possible value of this maximum difference.
#
# Input
# Each test consists of several test cases.
#
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains one even number n
#  (2≤n≤2⋅105
# ) — the length of the array a
# .
#
# The second line contains n
#  integers a1,a2,…,an
#  (−109≤ai≤109)
#  — the elements of the array a
# .
#
# It is guaranteed that the sum of the values of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output a single number — the minimum possible maximum difference between the elements in pairs.
#
# Example
# InputCopy
# 5
# 2
# 1 2
# 4
# 10 1 2 9
# 6
# 3 8 9 3 3 2
# 8
# 5 5 5 5 5 5 5 5
# 4
# -5 -1 2 6
# OutputCopy
# 1
# 1
# 1
# 0
# 4
# Note
# In the first test case, the array is: [1,2]
# . The only possible (and therefore optimal) pair is (1,2)
# , its difference is |1−2|=1
# , the answer is 1
# .
#
# In the second test case, the array is: [10,1,2,9]
# . We can choose pairs — (1,2)
#  and (9,10)
# : both differences are equal to 1
# , therefore, the maximum difference is 1
# .
#
# In the third test case, the array is: [3,8,9,3,3,2]
# . We can choose pairs: (2,3)
# , (3,3)
# , (8,9)
# . The differences are: 1,0,1
#  — the largest is 1
# .