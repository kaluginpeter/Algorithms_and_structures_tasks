# B. Ordinary Numbers
# time limit per test2 seconds
# memory limit per test256 megabytes
# Let's call a positive integer n
#  ordinary if in the decimal notation all its digits are the same. For example, 1
# , 2
#  and 99
#  are ordinary numbers, but 719
#  and 2021
#  are not ordinary numbers.
#
# For a given number n
# , find the number of ordinary numbers among the numbers from 1
#  to n
# .
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ). Then t
#  test cases follow.
#
# Each test case is characterized by one integer n
#  (1≤n≤109
# ).
#
# Output
# For each test case output the number of ordinary numbers among numbers from 1
#  to n
# .
#
# Example
# InputCopy
# 6
# 1
# 2
# 3
# 4
# 5
# 100
# OutputCopy
# 1
# 2
# 3
# 4
# 5
# 18
# Solution
# C++ O(logN) O(1) Math
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        long long n;
        std::cin >> n;
        long long mod = 1;
        int output = 0;
        bool isValid = true;
        while (isValid) {
            for (long long num = 1; num < 10; ++num) {
                if (num * mod <= n) {
                    ++output;
                } else {
                    isValid = false;
                    std::cout << output << "\n";
                    break;
                }
            }
            mod = mod * 10 + 1;
        }
    }
}

# Python O(logN) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        output: int = 0
        mod: int = 1
        is_valid: bool = True
        while is_valid:
            for num in range(1, 10):
                if num * mod <= n:
                    output += 1
                else:
                    sys.stdout.write(str(output) + '\n')
                    is_valid = False
                    break
            mod = mod * 10 + 1


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)