# A. Remove Smallest
# time limit per test1 second
# memory limit per test256 megabytes
# You are given the array a
#  consisting of n
#  positive (greater than zero) integers.
#
# In one move, you can choose two indices i
#  and j
#  (i≠j
# ) such that the absolute difference between ai
#  and aj
#  is no more than one (|ai−aj|≤1
# ) and remove the smallest of these two elements. If two elements are equal, you can remove any of them (but exactly one).
#
# Your task is to find if it is possible to obtain the array consisting of only one element using several (possibly, zero) such moves or not.
#
# You have to answer t
#  independent test cases.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤1000
# ) — the number of test cases. Then t
#  test cases follow.
#
# The first line of the test case contains one integer n
#  (1≤n≤50
# ) — the length of a
# . The second line of the test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤100
# ), where ai
#  is the i
# -th element of a
# .
#
# Output
# For each test case, print the answer: "YES" if it is possible to obtain the array consisting of only one element using several (possibly, zero) moves described in the problem statement, or "NO" otherwise.
#
# Example
# inputCopy
# 5
# 3
# 1 2 2
# 4
# 5 5 5 5
# 3
# 1 2 4
# 4
# 1 3 4 4
# 1
# 100
# outputCopy
# YES
# YES
# NO
# NO
# YES
# Note
# In the first test case of the example, we can perform the following sequence of moves:
#
# choose i=1
#  and j=3
#  and remove ai
#  (so a
#  becomes [2;2]
# );
# choose i=1
#  and j=2
#  and remove aj
#  (so a
#  becomes [2]
# ).
# In the second test case of the example, we can choose any possible i
#  and j
#  any move and it doesn't matter which element we remove.
#
# In the third test case of the example, there is no way to get rid of 2
#  and 4
# .
# Solution Sorting Greedy O(NlogN) O(N)
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list = sorted(map(int, sys.stdin.readline().rstrip().split()))
        print(['NO', 'YES'][all(x - y <= 1 for y, x in zip(nums, nums[1:])) or len(nums) == 1])


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
