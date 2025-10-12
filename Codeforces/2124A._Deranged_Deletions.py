# A. Deranged Deletions
# time limit per test1 second
# memory limit per test256 megabytes
# Call an array b
#  of length m
#  a derangement if the following property holds:
#
# Let c
#  be an array of length m
#  such that ci=bi
#  over all 1≤i≤m
# .
# Sort c
#  in non-decreasing order.
# If bi≠ci
#  over all 1≤i≤m
# , then b
#  is a derangement.
# For example,
#
# If b=[4,8,3,1]
# , then c=[1,3,4,8]
#  after getting sorted. Since bi≠ci
#  in all positions, b
#  is a derangement.
# If b=[3,2,1]
# , then c=[1,2,3]
#  after getting sorted. Since b2=c2
# , b
#  is not a derangement.
# You are given an array a
#  of length n
# . In one operation, you can delete an element from a
# . The order of the remaining elements is preserved after each deletion.
#
# Output whether it is possible to perform some (possibly none) operations such that the remaining elements form a derangement. If it is possible, output any possible remaining array. The remaining array must be non-empty.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The first line of each test case contains an integer n
#  (1≤n≤100
# ) — the length of array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤n
# ) — denoting the array a
# .
#
# Output
# For each test case, on a new line, if it is possible to perform operations such that the remaining array is a derangement, output YES. Otherwise, output NO.
#
# You can output in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# If your response was positive, output two more lines in the following format:
#
# The first line should contain an integer k
#  (1≤k≤n
# ), the number of elements that remain in the array.
# The second line should contain d1,d2…,dk
# , the elements that remain in the array. It must be possible to acquire array d
#  after performing some operations on a
# . Array d
#  must be a derangement.
# Example
# InputCopy
# 3
# 3
# 2 2 3
# 5
# 4 5 5 2 4
# 1
# 1
# OutputCopy
# NO
# YES
# 4
# 4 5 2 4
# NO
# Note
# In the second test case, we can delete one 5
#  from the array so that it becomes [4,5,2,4]
# . It can be shown this array is a derangement. This is not the only solution – it can be shown that the original array [4,5,5,2,4]
#  is another valid solution.