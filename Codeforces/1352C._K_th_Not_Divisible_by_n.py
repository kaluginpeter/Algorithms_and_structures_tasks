# C. K-th Not Divisible by n
# time limit per test1 second
# memory limit per test256 megabytes
# You are given two positive integers n
#  and k
# . Print the k
# -th positive integer that is not divisible by n
# .
#
# For example, if n=3
# , and k=7
# , then all numbers that are not divisible by 3
#  are: 1,2,4,5,7,8,10,11,13…
# . The 7
# -th number among them is 10
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases in the input. Next, t
#  test cases are given, one per line.
#
# Each test case is two positive integers n
#  (2≤n≤109
# ) and k
#  (1≤k≤109
# ).
#
# Output
# For each test case print the k
# -th positive integer that is not divisible by n
# .
#
# Example
# inputCopy
# 6
# 3 7
# 4 12
# 2 1000000000
# 7 97
# 1000000000 1000000000
# 2 1
# outputCopy
# 10
# 15
# 1999999999
# 113
# 1000000001
# 1
# Solution
# Python O(log(K * K)) O(1) Math
import sys


def binary_search(n: int, target: int) -> str:
    left: int = 0
    right: int = target * n
    while left <= right:
        middle: int = left + (right - left) // 2
        not_divisible: int = middle - middle // n
        if not_divisible > target:
            right = middle - 1
        elif not_divisible < target:
            left = middle + 1
        else: return str(middle) if middle % n != 0 else str(middle - 1)


def solution(t: int) -> None:
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(binary_search(n, k) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(log(K * K)) O(1) Math
#include <iostream>


long long binary_search(long long n, long long k) {
    long long left = 0;
    long long right = n * k;
    while (left <= right) {
        long long middle = left + (right - left) / 2;
        long long not_divisible = middle - middle / n;
        if (not_divisible > k) {
            right = middle - 1;
        } else if (not_divisible < k) {
            left = middle + 1;
        } else {
            if (middle % n == 0) {
                return middle - 1;
            } else {
                return middle;
            }
        }
    }
};


int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; i++) {
        long long n, k;
        std::cin >> n >> k;
        std::cout << binary_search(n, k) << std::endl;
    }
    return 0;
};
