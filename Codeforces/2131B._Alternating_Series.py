# B. Alternating Series
# time limit per test2 seconds
# memory limit per test256 megabytes
#
# You are given an integer n
# . Call an array a
#  of length n
#  good if:
#
# For all 1≤i<n
# , ai⋅ai+1<0
#  (i.e., the product of adjacent elements is negative).
# For all subarrays∗
#  with length at least 2
# , the sum of all elements in the subarray is positive†
# .
# Additionally, we say a good array a
#  of length n
#  is better than another good array b
#  of length n
#  if [|a1|,|a2|,…,|an|]
#  is lexicographically smaller‡
#  than [|b1|,|b2|,…,|bn|]
# . Note that |z|
#  denotes the absolute value of integer z
# .
#
# Output a good array of length n
#  such that it is better than every other good array of length n
# .
#
# ∗
# An array c
#  is a subarray of an array d
#  if c
#  can be obtained from d
#  by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.
#
# †
# An integer x
#  is positive if x>0
# .
#
# ‡
# A sequence a
#  is lexicographically smaller than a sequence b
#  if and only if one of the following holds:
#
# a
#  is a prefix of b
# , but a≠b
# ; or
# in the first position where a
#  and b
#  differ, the sequence a
#  has a smaller element than the corresponding element in b
# .
# Input
# The first line contains an integer t
#  (1≤t≤500
# ) — the number of test cases.
#
# The single line of each test case contains one integer n
#  (2≤n≤2⋅105
# ) — the length of your array.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output n
#  integers a1,a2,…,an
#  (−109≤ai≤109
# ), the elements of your array on a new line.
#
# Example
# InputCopy
# 2
# 2
# 3
# OutputCopy
# -1 2
# -1 3 -1
# Note
# In the first test case, because a1⋅a2=−2<0
#  and a1+a2=1>0
# , it satisfies the two constraints. In addition, it can be shown that the corresponding b=[1,2]
#  is better than any other good array of length 2
# .
# Solution
# C++ O(N) O(1) Math Greedy
#include <iostream>
#include <vector>


void solution() {
    int n;
    std::cin >> n;
    for (int i = 0; i < n - 1; ++i) {
        std::cout << (i & 1 ? 3 : -1) << " ";
    }
    std::cout << (n & 1 ? -1 : 2) << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Math Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    for i in range(n - 1):
        sys.stdout.write('{} '.format(3 if i & 1 else -1))
    sys.stdout.write('{}\n'.format(-1 if n & 1 else 2))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()