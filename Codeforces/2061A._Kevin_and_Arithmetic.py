# A. Kevin and Arithmetic
# time limit per test1 second
# memory limit per test256 megabytes
# To train young Kevin's arithmetic skills, his mother devised the following problem.
#
# Given n
#  integers a1,a2,…,an
#  and a sum s
#  initialized to 0
# , Kevin performs the following operation for i=1,2,…,n
#  in order:
#
# Add ai
#  to s
# . If the resulting s
#  is even, Kevin earns a point and repeatedly divides s
#  by 2
#  until it becomes odd.
# Note that Kevin can earn at most one point per operation, regardless of how many divisions he does.
#
# Since these divisions are considered more beneficial for Kevin's development, his mother wants to rearrange a
#  so that the number of Kevin's total points is maximized. Determine the maximum number of points.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤100
# ) — the number of integers.
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ).
#
# Output
# For each test case, output one integer — the maximum number of points.
#
# Example
# InputCopy
# 5
# 1
# 1
# 2
# 1 2
# 3
# 2 4 6
# 4
# 1000000000 999999999 999999998 999999997
# 10
# 3 1 4 1 5 9 2 6 5 3
# OutputCopy
# 0
# 2
# 1
# 3
# 8
# Note
# In the first test case, the only arrangement of a
#  is [1]
# . s
#  becomes 1
# . Kevin earns no points.
#
# In the second test case, the only possible arrangement of a
#  is [2,1]
# . s
#  becomes 1
#  and 1
#  successively. Kevin earns points in both operations.
#
# In the third test case, one possible arrangement of a
#  is [2,4,6]
# . s
#  becomes 1
# , 5
# , and 11
#  successively. Kevin earns a point in the first operation.
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>


void solution() {
    int n;
    std::cin >> n;
    int odd = 0, even = 0;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        if (x & 1) ++odd;
        else ++even;
    }
    int output = 0;
    if (even) std::cout << 1 + odd << std::endl;
    else std::cout << odd - 1 << std::endl;
}
// odd + odd = even
// odd + even = odd

int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    odd: int = 0
    even: int = 0
    for num in nums:
        if num & 1: odd += 1
        else: even += 1
    if even: sys.stdout.write('{}\n'.format(1 + odd))
    else: sys.stdout.write('{}\n'.format(odd - 1))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()