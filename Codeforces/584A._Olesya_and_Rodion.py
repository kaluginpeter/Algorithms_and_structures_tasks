584A. Olesya and Rodion
# A. Olesya and Rodion
# time limit per test1 second
# memory limit per test256 megabytes
# Olesya loves numbers consisting of n digits, and Rodion only likes numbers that are divisible by t. Find some number that satisfies both of them.
#
# Your task is: given the n and t print an integer strictly larger than zero consisting of n digits that is divisible by t. If such number doesn't exist, print  - 1.
#
# Input
# The single line contains two numbers, n and t (1 ≤ n ≤ 100, 2 ≤ t ≤ 10) — the length of the number and the number it should be divisible by.
#
# Output
# Print one such positive number without leading zeroes, — the answer to the problem, or  - 1, if such number doesn't exist. If there are multiple possible answers, you are allowed to print any of them.
#
# Examples
# InputCopy
# 3 2
# OutputCopy
# 712
# Solution
# C++ O(N) O(1) Math
#include <iostream>

int main() {
    int n, t;
    std::cin >> n >> t;
    if (t == 10) {
        if (n == 1) {
            std::cout << -1 << std::endl;
        } else {
            std::cout << "1";
            for (int i = 0; i < n - 1; ++i) {
                std::cout << "0";
            }
            std::cout << std::endl;
        }
    } else {
        for (int i = 0; i < n; ++i) {
            std::cout << t;
        }
        std::cout << std::endl;
    }
}

# Python O(N) O(1) Math
import sys


def solution(n: int, t: int) -> str:
    if t == 10:
        if n == 1:
            return '-1'
        return '1' + '0' * (n - 1)
    return str(t) * n

if __name__ == '__main__':
    n, t = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(solution(n, t) + '\n')