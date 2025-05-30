# A. Square Year
# time limit per test1 second
# memory limit per test256 megabytes
# One can notice the following remarkable mathematical fact: the number 2025
#  can be represented as (20+25)2
# .
#
# You are given a year represented by a string s
# , consisting of exactly 4
#  characters. Thus, leading zeros are allowed in the year representation. For example, "0001", "0185", "1375" are valid year representations. You need to express it in the form (a+b)2
# , where a
#  and b
#  are non-negative integers, or determine that it is impossible.
#
# For example, if s
#  = "0001", you can choose a=0
# , b=1
# , and write the year as (0+1)2=1
# .
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The following lines describe the test cases.
#
# The only line of each test case contains a string s
# , consisting of exactly 4
#  characters. Each character is a digit from 0
#  to 9
# .
#
# Output
# On a separate line for each test case, output:
#
# Two numbers a
#  and b
#  (a,b≥0
# ) such that (a+b)2=s
# , if they exist. If there are multiple suitable pairs, you may output any of them.
# The number −1
#  otherwise.
# Example
# InputCopy
# 5
# 0001
# 1001
# 1000
# 4900
# 2025
# OutputCopy
# 0 1
# -1
# -1
# 34 36
# 20 25
# Solution
# C++ O(sqrt(N)) O(1) Math
#include <iostream>
#include <cmath>


int getPair(int n) {
    int bound = std::sqrt(n);
    return (bound * bound == n? bound : -1);
}


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        int output = getPair(n);
        if (output == -1) std::printf("-1\n");
        else std::printf("%d %d\n", output, 0);
    }
}


int main() {
    solution();
}

# Python O(sqrt(N)) O(1) Math
import sys
import math


def get_pair(n: int) -> int:
    bound: int = int(math.sqrt(n))
    return [-1, bound][bound * bound == n]


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        output: int = get_pair(n)
        if output == -1: sys.stdout.write('-1\n')
        else: sys.stdout.write('{} {}\n'.format(output, 0))


if __name__ == '__main__':
    solution()