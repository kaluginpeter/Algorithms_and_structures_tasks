# A. Plus One on the Subset
# time limit per test2 seconds
# memory limit per test256 megabytes
# Polycarp got an array of integers a[1…n]
#  as a gift. Now he wants to perform a certain number of operations (possibly zero) so that all elements of the array become the same (that is, to become a1=a2=⋯=an
# ).
#
# In one operation, he can take some indices in the array and increase the elements of the array at those indices by 1
# .
# For example, let a=[4,2,1,6,2]
# . He can perform the following operation: select indices 1, 2, and 4 and increase elements of the array in those indices by 1
# . As a result, in one operation, he can get a new state of the array a=[5,3,1,7,2]
# .
#
# What is the minimum number of operations it can take so that all elements of the array become equal to each other (that is, to become a1=a2=⋯=an
# )?
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# )  — the number of test cases in the test.
#
# The following are descriptions of the input test cases.
#
# The first line of the description of each test case contains one integer n
#  (1≤n≤50
# )  — the array a
# .
#
# The second line of the description of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# )  — elements of the array a
# .
#
# Output
# For each test case, print one integer  — the minimum number of operations to make all elements of the array a
#  equal.
#
# Example
# inputCopy
# 3
# 6
# 3 4 2 4 1 2
# 3
# 1000 1002 998
# 2
# 12 11
# outputCopy
# 3
# 4
# 1
# Note
# First test case:
#
# a=[3,4,2,4,1,2]
#  take a3,a5
#  and perform an operation plus one on them, as a result we get a=[3,4,3,4,2,2]
# .
# a=[3,4,3,4,2,2]
#  we take a1,a5,a6
#  and perform an operation on them plus one, as a result we get a=[4,4,3,4,3,3]
# .
# a=[4,4,3,4,3,3]
#  we take a3,a5,a6
#  and perform an operation on them plus one, as a result we get a=[4,4,4,4,4,4]
# .
# There are other sequences of 3
#  operations, after the application of which all elements become equal.
#
# Second test case:
#
# a=[1000,1002,998]
#  2 times we take a1,a3
#  and perform an operation plus one on them, as a result we get a=[1002,1002,1000]
# .
# a=[1002,1002,1000]
#  also take a3
#  2 times and perform an operation plus one on it, as a result we get a=[1002,1002,1002]
# .
# Third test case:
#
# a=[12,11]
#  take a2
#  and perform an operation plus one on it, as a result we get a=[12,12]
# .
# Solution
# Python O(N) O(1)
from typing import List
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        numbers: List[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        print(max(numbers) - min(numbers))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
# C++ O(1) O(1)
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        int min_num = 10000000000;
        int max_num = 1;
        for (int j = 0; j < n; ++j) {
            int number;
            std::cin >> number;
            min_num = std::min(min_num, number);
            max_num = std::max(max_num, number);
        }
        std::cout << max_num - min_num << std::endl;
    }
}