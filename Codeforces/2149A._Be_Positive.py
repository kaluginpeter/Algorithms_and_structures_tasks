# A. Be Positive
# time limit per test1 second
# memory limit per test256 megabytes
# Given an array a
#  of n
#  elements, where each element is equal to −1
# , 0
# , or 1
# . In one operation, you can choose an index i
#  and increase ai
#  by 1
#  (that is, assign ai:=ai+1
# ). Operations can be performed any number of times, choosing any indices.
#
# The goal is to make the product of all elements in the array strictly positive with the minimum number of operations, that is, a1⋅a2⋅a3⋅…⋅an>0
# . Find the minimum number of operations.
#
# It is guaranteed that this is always possible.
#
# Input
# Each test consists of several test cases.
#
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains one integer n
#  (1≤n≤8
# ) — the length of the array a
# .
#
# The second line contains n
#  integers a1,a2,…,an
# , where −1≤ai≤1
#  — the elements of the array a
# .
#
# Output
# For each test case, output one integer — the minimum number of operations required to make the product of the elements in the array strictly positive.
#
# Example
# InputCopy
# 3
# 3
# -1 0 1
# 4
# -1 -1 0 1
# 5
# -1 -1 -1 0 0
# OutputCopy
# 3
# 1
# 4
# Note
# In the first test case: from [−1,0,1]
# , you can obtain [1,1,1]
#  in 3
#  operations.
#
# In the second test case: it is enough to perform 0→1
#  (1 operation). In the resulting array a=[−1,−1,1,1]
# , the product of all elements is 1
# .
#
# In the third test case: turning two zeros into ones (2 operations), and one −1
#  into 1
#  (another 2 operations), for a total of 4
# .
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>


void solution() {
    size_t n;
    std::cin >> n;
    int negative = 0, zeros = 0;
    for (size_t i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        if (x < 0) ++negative;
        else if (!x) ++zeros;
    }
    std::cout << zeros + (negative & 1 ? 2 : 0) << std::endl;
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
    negative: int = 0
    zeros: int = 0
    for _ in range(n):
        x: int = next(nums)
        if x < 0: negative += 1
        elif not x: zeros += 1
    sys.stdout.write('{}\n'.format(zeros + (2 if negative & 1 else 0)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()