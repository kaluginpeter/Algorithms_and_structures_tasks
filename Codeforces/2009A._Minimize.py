# A. Minimize!
# time limit per test1 second
# memory limit per test256 megabytes
# You are given two integers a
#  and b
#  (a≤b
# ). Over all possible integer values of c
#  (a≤c≤b
# ), find the minimum value of (c−a)+(b−c)
# .
#
# Input
# The first line contains t
#  (1≤t≤55
# ) — the number of test cases.
#
# Each test case contains two integers a
#  and b
#  (1≤a≤b≤10
# ).
#
# Output
# For each test case, output the minimum possible value of (c−a)+(b−c)
#  on a new line.
#
# Example
# inputCopy
# 3
# 1 2
# 3 10
# 5 5
# outputCopy
# 1
# 7
# 0
# Note
# In the first test case, you can choose c=1
#  and obtain an answer of (1−1)+(2−1)=1
# . It can be shown this is the minimum value possible.
#
# In the second test case, you can choose c=6
#  and obtain an answer of (6−3)+(10−6)=7
# . It can be shown this is the minimum value possible.
# Solution
# Python O(N) O(1) Math Simulation
import sys


def solution(t: int) -> None:
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(str(max((c - a) + (b - c) for c in range(a, b + 1))) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(N) O(1) Math Simulation
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int a, b;
        std::cin >> a >> b;
        int output = a + b;
        for (int c = a; c <= b; ++c) {
            output = std::min(output, (c - a) + (b - c));
        }
        std::cout << output << std::endl;
    }
}