# A. A+B Again?
# time limit per test1 second
# memory limit per test256 megabytes
# Given a two-digit positive integer n
# , find the sum of its digits.
#
# Input
# The first line contains an integer t
#  (1≤t≤90
# ) — the number of test cases.
#
# The only line of each test case contains a single two-digit positive integer n
#  (10≤n≤99
# ).
#
# Output
# For each test case, output a single integer — the sum of the digits of n
# .
#
# Example
# inputCopy
# 8
# 77
# 21
# 40
# 34
# 19
# 84
# 10
# 99
# outputCopy
# 14
# 3
# 4
# 7
# 10
# 12
# 1
# 18
# Solution
# C++ O(1) O(1) String Math
#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string n;
        std::cin >> n;
        std::cout << (n[0] - '0') + (n[1] - '0') << std::endl;
    }
}

# Python O(1) O(1) Math String
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: str = sys.stdin.readline().rstrip()
        sys.stdout.write(str(int(n[0]) + int(n[1])) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
