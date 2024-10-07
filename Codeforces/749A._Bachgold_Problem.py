# A. Bachgold Problem
# time limit per test1 second
# memory limit per test256 megabytes
# Bachgold problem is very easy to formulate. Given a positive integer n represent it as a sum of maximum possible number of prime numbers. One can prove that such representation exists for any integer greater than 1.
#
# Recall that integer k is called prime if it is greater than 1 and has exactly two positive integer divisors — 1 and k.
#
# Input
# The only line of the input contains a single integer n (2 ≤ n ≤ 100 000).
#
# Output
# The first line of the output contains a single integer k — maximum possible number of primes in representation.
#
# The second line should contain k primes with their sum equal to n. You can print them in any order. If there are several optimal solution, print any of them.
#
# Examples
# inputCopy
# 5
# outputCopy
# 2
# 2 3
# inputCopy
# 6
# outputCopy
# 3
# 2 2 2
# Solution
# Python O(N) O(1) Math
import sys


def solution(n: int) -> str:
    modules: list = [2, 3]
    sys.stdout.write(str(n // 2) + '\n')
    if n & 1 == 0:
        return ' '.join('2' for _ in range(n // 2))
    return ' '.join('2' for _ in range(n // 2 - 1)) + ' 3'


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(solution(n))

# C++ O(N) O(1) Math
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    std::cout << n / 2 << std::endl;
    if (n % 2 == 0) {
        for (int rep = 0; rep < n / 2; ++rep) {
            if (rep != 0) {
                std::cout << " ";
            }
            std::cout << 2;
        }
    } else {
        for (int rep = 0; rep < n / 2 - 1; ++rep) {
            if (rep != 0) {
                std::cout << " ";
            }
            std::cout << 2;
        }
        std::cout << " 3";
    }
}