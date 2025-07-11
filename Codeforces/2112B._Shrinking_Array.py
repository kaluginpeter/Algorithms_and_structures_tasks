# B. Shrinking Array
# time limit per test2 seconds
# memory limit per test256 megabytes
# Let's call an array b
#  beautiful if it consists of at least two elements and there exists a position i
#  such that |bi−bi+1|≤1
#  (where |x|
#  is the absolute value of x
# ).
#
# You are given an array a
# , and as long as it consists of at least two elements, you can perform the following operation:
#
# Choose two adjacent positions i
#  and i+1
#  in the array a
# .
# Choose an integer x
#  such that min(ai,ai+1)≤x≤max(ai,ai+1)
# .
# Remove the numbers ai
#  and ai+1
#  from the array, and insert the number x
#  in their place. Obviously, the size of the array will decrease by 1
# .
# Calculate the minimum number of operations required to make the array beautiful, or report that it is impossible.
#
# Input
# The first line contains one integer t
#  (1≤t≤200
# ) — the number of test cases.
#
# The first line of each test case contains one integer n
#  (2≤n≤1000
# ) — the size of the array a
# .
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤106
# ) — the array a
#  itself.
#
# Output
# For each test case, output one integer — the minimum number of operations needed to make the array a
#  beautiful, or −1
#  if it is impossible to make it beautiful.
#
# Example
# InputCopy
# 4
# 4
# 1 3 3 7
# 2
# 6 9
# 4
# 3 1 3 7
# 4
# 1 3 5 2
# OutputCopy
# 0
# -1
# 1
# 1
# Note
# In the first test case, the given array is already beautiful, as |a2−a3|=|3−3|=0
# .
#
# In the second test case, it is impossible to make the array beautiful, as applying the operation would reduce its size to less than two.
#
# In the third test case, you can, for example, choose a1
#  and a2
#  and replace them with the number 2
# . The resulting array [2,3,7]
#  is beautiful.
#
# In the fourth test case, you can, for example, choose a2
#  and a3
#  and replace them with the number 3
# . The resulting array [1,3,2]
#  is beautiful.