# A. My First Sorting Problem
# time limit per test1 second
# memory limit per test256 megabytes
# You are given two integers x
#  and y
# .
#
# Output two integers: the minimum of x
#  and y
# , followed by the maximum of x
#  and y
# .
#
# Input
# The first line contains a single integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# The only line of each test case contains two space-separated integers x
#  and y
#  (0≤x,y≤9
# ).
#
# Output
# For each test case, output two integers: the minimum of x
#  and y
# , followed by the maximum of x
#  and y
# .
#
# Example
# InputCopy
# 10
# 1 9
# 8 4
# 1 4
# 3 4
# 2 0
# 2 4
# 6 9
# 3 3
# 0 0
# 9 9
# OutputCopy
# 1 9
# 4 8
# 1 4
# 3 4
# 0 2
# 2 4
# 6 9
# 3 3
# 0 0
# 9 9
# Solution
# C++ O(1) O(1) Math
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int x, y;
        std::cin >> x >> y;
        std::cout << std::min(x, y) << " " << std::max(x, y) << std::endl;
    }
}

# Python O(1) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(f'{min(x, y)} {max(x, y)}\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

