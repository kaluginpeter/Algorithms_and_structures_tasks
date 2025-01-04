# A. Park Lighting
# time limit per test2 seconds
# memory limit per test256 megabytes
# Due to the coronavirus pandemic, city authorities obligated citizens to keep a social distance. The mayor of the city Semyon wants to light up Gluharniki park so that people could see each other even at night to keep the social distance.
#
# The park is a rectangular table with n
#  rows and m
#  columns, where the cells of the table are squares, and the boundaries between the cells are streets. External borders are also streets. Every street has length 1
# . For example, park with n=m=2
#  has 12
#  streets.
#
# You were assigned to develop a plan for lighting the park. You can put lanterns in the middle of the streets. The lamp lights two squares near it (or only one square if it stands on the border of the park).
#
# The park sizes are: n=4
# , m=5
# . The lighted squares are marked yellow. Please note that all streets have length 1
# . Lanterns are placed in the middle of the streets. In the picture not all the squares are lit.
# Semyon wants to spend the least possible amount of money on lighting but also wants people throughout the park to keep a social distance. So he asks you to find the minimum number of lanterns that are required to light all the squares.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases in the input. Then t
#  test cases follow.
#
# Each test case is a line containing two integers n
# , m
#  (1≤n,m≤104
# ) — park sizes.
#
# Output
# Print t
#  answers to the test cases. Each answer must be a single integer — the minimum number of lanterns that are required to light all the squares.
#
# Example
# InputCopy
# 5
# 1 1
# 1 3
# 2 2
# 3 3
# 5 3
# OutputCopy
# 1
# 2
# 2
# 5
# 8
# Note
# Possible optimal arrangement of the lanterns for the 2
# -nd test case of input data example:
#
# Possible optimal arrangement of the lanterns for the 3
# -rd test case of input data example:
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, m;
        std::cin >> n >> m;
        std::cout << (n * m + 1) / 2 << "\n";
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math
from __future__ import annotations
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(f'{(n * m + 1) // 2}\n')


if __name__ == '__main__':
    solution()