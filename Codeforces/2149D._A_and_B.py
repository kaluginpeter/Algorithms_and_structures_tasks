# D. A and B
# time limit per test2 seconds
# memory limit per test256 megabytes
# Given a string s
#  of length n
# , consisting only of the characters 'a' and 'b'.
#
# In one operation, you can choose a position i
#  (1≤i≤n−1
# ) and swap the neighboring characters si
#  and si+1
# .
#
# You need to perform the minimum number of operations to ensure that all characters of one type (either a
#  or b
# ) are located strictly together, forming exactly one continuous block.
#
# Characters of the other type can be positioned either before or after this block, forming two (possibly empty) blocks.
#
# Examples of valid final forms:
#
# 'aaabbbaaa' — all 'b's are located together (one block), 'a's can be both before and after this block;
# 'bbbaaaaaabbb' — all 'a's together, 'b's are at the edges of the string;
# 'aaaaabbbb' or 'bbbbaaaaa' — both types of characters form one continuous block each.
# You need to find the minimum number of described operations required to achieve the specified state.
#
# Input
# Each test consists of several test cases.
#
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases. The description of test cases follows.
#
# The first line of each test case contains one integer n
#  (1≤n≤2⋅105
# ) — the length of the string s
# .
#
# The second line contains the string s
#  of length n
# , consisting only of the characters 'a' and 'b'.
#
# It is guaranteed that the sum of the values of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output one integer — the minimum number of operations required for all characters of one of the two types to form a single continuous block.
#
# Example
# InputCopy
# 5
# 4
# abab
# 6
# bababa
# 7
# abababa
# 2
# ab
# 1
# b
# OutputCopy
# 1
# 2
# 2
# 0
# 0
# Note
# In the first test case, the initial string is 'abab':
#
# by swapping the neighboring characters at positions 2
#  and 3
# , we get the string 'aabb';
# or by swapping the characters at positions 1
#  and 2
# , we get the string 'baab'.
# In both cases, exactly one operation is performed, after which all letters of one type form a single block, so the minimum number of operations is 1
# .
# In the fifth input test case, the string consists of a single character 'b'. The single character already forms a continuous block, no swaps are needed, so the minimum number of operations is 0
# .