# A. Beautiful Average
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an array a
#  of length n
# .
#
# Your task is to find the maximum possible average value of any subarray∗
#  of the array a
# .
#
# Formally, for any indices l,r
#  such that 1≤l≤r≤n
# , define the average of the subarray al,al+1,…,ar
#  as the sum of elements divided by the number of elements or:
# avg(l,r)=1r−l+1∑i=lrai
# Output the maximum value of avg(l,r)
#  over all choices of l,r
# .
#
# ∗
# An array b
#  is a subarray of an array a
#  if b
#  can be obtained from a
#  by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. In particular, an array is a subarray of itself.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each testcase contains a single integer n
#  (1≤n≤10
# ) — the length of the array a
# .
#
# The second line of each testcase contains n
#  integers a1,a2,…,an
#  (1≤ai≤10
# ) — the elements of the array.
#
# Output
# For each testcase, output a single integer — the maximum average of any subarray of the given array.
#
# It can be shown that the answer is always an integer.
#
# Example
# InputCopy
# 3
# 4
# 3 3 3 3
# 5
# 7 1 6 9 9
# 5
# 3 4 4 4 3
# OutputCopy
# 3
# 9
# 4
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>


void solution() {
    size_t n;
    std::cin >> n;
    int output = 0;
    for (size_t i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        output = std::max(output, x);
    }
    std::cout << output << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write('{}\n'.format(max(nums)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()