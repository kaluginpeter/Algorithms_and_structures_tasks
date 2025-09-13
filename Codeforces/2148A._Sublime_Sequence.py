# A. Sublime Sequence
# time limit per test1 second
# memory limit per test256 megabytes
# Farmer John has an integer x
# . He creates a sequence of length n
#  by alternating integers x
#  and −x
# , starting with x
# .
#
# For example, if n=5
# , the sequence looks like: x,−x,x,−x,x
# .
#
# He asks you to find the sum of all integers in the sequence.
#
# Input
# The first line contains an integer t
#  (1≤t≤100
# )  — the number of test cases.
#
# The only line of input for each test case is two integers x
#  and n
#  (1≤x,n≤10
# ).
#
# Output
# For each test case, output the sum of all integers in the sequence.
#
# Example
# InputCopy
# 4
# 1 4
# 2 5
# 3 6
# 4 7
# OutputCopy
# 0
# 2
# 0
# 4
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int k, n;
    std::cin >> k >> n;
    std::cout << (n & 1 ? k : 0) << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    k, n = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write('{}\n'.format([0, k][n & 1]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()