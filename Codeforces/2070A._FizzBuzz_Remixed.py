# A. FizzBuzz Remixed
# time limit per test1 second
# memory limit per test512 megabytes
# FizzBuzz is one of the most well-known problems from coding interviews. In this problem, we will consider a remixed version of FizzBuzz:
#
# Given an integer n
# , process all integers from 0
#  to n
# . For every integer such that its remainders modulo 3
#  and modulo 5
#  are the same (so, for every integer i
#  such that imod3=imod5
# ), print FizzBuzz.
#
# However, you don't have to solve it. Instead, given the integer n
# , you have to report how many times the correct solution to that problem will print FizzBuzz.
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each test case contains one line consisting of one integer n
#  (0≤n≤109
# ).
#
# Output
# For each test case, print one integer — the number of times the correct solution will print FizzBuzz with the given value of n
# .
#
# Example
# InputCopy
# 7
# 0
# 5
# 15
# 42
# 1337
# 17101997
# 998244353
# OutputCopy
# 1
# 3
# 4
# 9
# 270
# 3420402
# 199648872
# Note
# In the first test case, the solution will print FizzBuzz for the integer 0
# .
#
# In the second test case, the solution will print FizzBuzz for the integers 0,1,2
# .
#
# In the third test case, the solution will print FizzBuzz for the integers 0,1,2,15
# .
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        long long count = 0;
        count += (n / 15) + 1;
        if (n >= 1) count += ((n - 1) / 15) + 1;
        if (n >= 2) count += ((n - 2) / 15) + 1;
        std::cout << count << "\n";
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
        count: int = n // 15 + 1
        if n >= 1: count += (n - 1) // 15 + 1
        if n >= 2: count += (n - 2) // 15 + 1
        sys.stdout.write('{}\n'.format(count))


if __name__ == '__main__':
    solution()