# A. Ideal Generator
# time limit per test1 second
# memory limit per test256 megabytes
# We call an array a
# , consisting of k
#  positive integers, palindromic if [a1,a2,…,ak]=[ak,ak−1,…,a1]
# . For example, the arrays [1,2,1]
#  and [5,1,1,5]
#  are palindromic, while the arrays [1,2,3]
#  and [21,12]
#  are not.
#
# We call a number k
#  an ideal generator if any integer n
#  (n≥k
# ) can be represented as the sum of the elements of a palindromic array of length exactly k
# . Each element of the array must be greater than 0
# .
#
# For example, the number 1
#  is an ideal generator because any natural number n
#  can be generated using the array [n]
# . However, the number 2
#  is not an ideal generator — there is no palindromic array of length 2
#  that sums to 3
# .
#
# Determine whether the given number k
#  is an ideal generator.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first and only line of each test case contains one integer k
#  (1≤k≤1000
# ).
#
# Output
# For each number k
# , you need to output the word "YES" if it is an ideal generator, or "NO" otherwise.
#
# You may output "Yes" and "No" in any case (for example, the strings "yES", "yes", and "Yes" will be recognized as a positive answer).
#
# Example
# InputCopy
# 5
# 1
# 2
# 3
# 73
# 1000
# OutputCopy
# YES
# NO
# YES
# YES
# NO