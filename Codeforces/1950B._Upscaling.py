# B. Upscaling
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an integer n
# . Output a 2n×2n
#  checkerboard made of 2×2
#  squares alternating '#
# ' and '.
# ', with the top-left cell being '#
# '.
#
#
# The picture above shows the answers for n=1,2,3,4
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤20
# ) — the number of test cases.
#
# The only line of each test case contains a single integer n
#  (1≤n≤20
# ) — it means you need to output a checkerboard of side length 2n
# .
#
# Output
# For each test case, output 2n
#  lines, each containing 2n
#  characters without spaces — the checkerboard, as described in the statement. Do not output empty lines between test cases.
#
# Example
# InputCopy
# 4
# 1
# 2
# 3
# 4
# OutputCopy
# ##
# ##
# ##..
# ##..
# ..##
# ..##
# ##..##
# ##..##
# ..##..
# ..##..
# ##..##
# ##..##
# ##..##..
# ##..##..
# ..##..##
# ..##..##
# ##..##..
# ##..##..
# ..##..##
# ..##..##
# Solution
# C++ O(N**2) O(N) Simulation
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        for (int j = 0; j < n; ++j) {
            std::string row = "";
            char first = (j % 2 == 0? '#' : '.');
            char second = (j % 2 == 0? '.' : '#');
            bool flag = false;
            for (int k = 0; k < 2 * n; ++k) {
                if (k % 2 == 0) flag = !flag;
                if (flag) row += first;
                else row += second;
            }
            std::cout << row << "\n" << row << "\n";
        }
    }
}


int main() {
    solution();
}

# Python O(N**2) O(N) Simulation
from __future__ import annotations
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        for j in range(n):
            first: str = '#' if j % 2 == 0 else '.'
            second: str = '.' if j % 2 == 0 else '#'
            flag: bool = False
            row: list[str] = []
            for k in range(2*n):
                if k % 2 == 0: flag = not flag
                if flag: row.append(first)
                else: row.append(second)
            sys.stdout.write(''.join(row) + '\n')
            sys.stdout.write(''.join(row) + '\n')


if __name__ == '__main__':
    solution()
