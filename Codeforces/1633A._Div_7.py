# A. Div. 7
# time limit per test2 seconds
# memory limit per test512 megabytes
# You are given an integer n
# . You have to change the minimum number of digits in it in such a way that the resulting number does not have any leading zeroes and is divisible by 7
# .
#
# If there are multiple ways to do it, print any of them. If the given number is already divisible by 7
# , leave it unchanged.
#
# Input
# The first line contains one integer t
#  (1≤t≤990
# ) — the number of test cases.
#
# Then the test cases follow, each test case consists of one line containing one integer n
#  (10≤n≤999
# ).
#
# Output
# For each test case, print one integer without any leading zeroes — the result of your changes (i. e. the integer that is divisible by 7
#  and can be obtained by changing the minimum possible number of digits in n
# ).
#
# If there are multiple ways to apply changes, print any resulting number. If the given number is already divisible by 7
# , just print it.
#
# Example
# InputCopy
# 3
# 42
# 23
# 377
# OutputCopy
# 42
# 28
# 777
# Note
# In the first test case of the example, 42
#  is already divisible by 7
# , so there's no need to change it.
#
# In the second test case of the example, there are multiple answers — 28
# , 21
#  or 63
# .
#
# In the third test case of the example, other possible answers are 357
# , 371
#  and 378
# . Note that you cannot print 077
#  or 77
# .
# Solution
# C++ O(logN) O(1) Math Greedy
#include <iostream>
#include <cmath>


int diff(int other, int n) {
    int output = 0;
    while (other && n) {
        if (other % 10 != n % 10) ++output;
        other /= 10;
        n /= 10;
    }
    int extraOther = 0, extraN = 0;
    while (other) {
        ++extraOther;
        other /= 10;
    }
    while (n) {
        ++extraN;
        n /= 10;
    }
    return output + std::abs(extraOther - extraN);
}


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        if (n % 7 == 0) {
            std::printf("%d\n", n);
            continue;
        }
        int upper = 7 - n % 7, lower = n % 7;
        std::printf("%d\n", n + (diff(n + upper, n) <= diff(n - lower, n)? upper : -lower));
    }
}


int main() {
    solution();
}

# Python O(logN) O(1) Math Greedy
import sys


def diff(other: int, n: int) -> int:
    output: int = 0
    while other and n:
        if other % 10 != n % 10:
            output += 1
        other //= 10
        n //= 10
    extra_other: int = 0
    extra_n: int = 0
    while other:
        extra_other += 1
        other //= 10
    while n:
        extra_n += 1
        n //= 10
    return output + abs(extra_other - extra_n)


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        if n % 7 == 0:
            sys.stdout.write('{}\n'.format(n))
            continue
        upper: int = 7 - n % 7
        lower: int = n % 7
        sys.stdout.write('{}\n'.format(n + [-lower, upper][diff(n + upper, n) <= diff(n - lower, n)]))


if __name__ == '__main__':
    solution()