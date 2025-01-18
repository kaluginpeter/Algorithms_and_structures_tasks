# A. Easy Problem
# time limit per test1 second
# memory limit per test256 megabytes
# Cube is given an integer n
# . She wants to know how many ordered pairs of positive integers (a,b)
#  there are such that a=n−b
# . Since Cube is not very good at math, please help her!
#
# Input
# The first line contains an integer t
#  (1≤t≤99
# ) — the number of test cases.
#
# The only line of each test case contains an integer n
#  (2≤n≤100
# ).
#
# Output
# For each test case, output the number of ordered pairs (a,b)
#  on a new line.
#
# Example
# InputCopy
# 3
# 2
# 4
# 6
# OutputCopy
# 1
# 3
# 5
# Note
# In the first test case, the only ordered pair that works is (a,b)=(1,1)
# .
#
# In the second test case, the three ordered pairs of (a,b)
#  that work are (3,1),(2,2),(1,3)
# .
# Solution
# C++ O(1) O(1) Math
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::cout << n - 1 << "\n";
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        sys.stdout.write(str(n - 1) + '\n')


if __name__ == '__main__':
    solution()
