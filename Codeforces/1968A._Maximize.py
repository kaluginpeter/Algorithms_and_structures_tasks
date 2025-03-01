# A. Maximize?
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an integer x
# . Your task is to find any integer y
#  (1≤y<x)
#  such that gcd(x,y)+y
#  is maximum possible.
#
# Note that if there is more than one y
#  which satisfies the statement, you are allowed to find any.
#
# gcd(a,b)
#  is the Greatest Common Divisor of a
#  and b
# . For example, gcd(6,4)=2
# .
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each of the following t
#  lines contains a single integer x
#  (2≤x≤1000
# ).
#
# Output
# For each test case, output any y
#  (1≤y<x
# ), which satisfies the statement.
#
# Example
# InputCopy
# 7
# 10
# 7
# 21
# 100
# 2
# 1000
# 6
# OutputCopy
# 5
# 6
# 18
# 98
# 1
# 750
# 3
# Solution
# C++ O(NlogN) O(1) Math
#include <bits/stdc++.h>
using namespace std;


void solution() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int x;
        scanf("%d", &x);
        int y = -1;
        int yValue = -1;
        for (int d = 1; d < x; ++d) {
            int gcdXD = gcd(x, d);
            if (gcdXD + d >= yValue) {
                yValue = gcdXD + d;
                y = d;
            }
        }
        printf("%d\n", y);
    }
}


int main() {
	solution();
}

# Python O(1) O(1) Number Theory
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        x: int = int(sys.stdin.readline().rstrip())
        sys.stdout.write(f'{x - 1}\n')


if __name__ == '__main__':
    solution()