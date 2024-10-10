# B. New Year's Number
# time limit per test2 seconds
# memory limit per test256 megabytes
# Polycarp remembered the 2020
# -th year, and he is happy with the arrival of the new 2021
# -th year. To remember such a wonderful moment, Polycarp wants to represent the number n
#  as the sum of a certain number of 2020
#  and a certain number of 2021
# .
#
# For example, if:
#
# n=4041
# , then the number n
#  can be represented as the sum 2020+2021
# ;
# n=4042
# , then the number n
#  can be represented as the sum 2021+2021
# ;
# n=8081
# , then the number n
#  can be represented as the sum 2020+2020+2020+2021
# ;
# n=8079
# , then the number n
#  cannot be represented as the sum of the numbers 2020
#  and 2021
# .
# Help Polycarp to find out whether the number n
#  can be represented as the sum of a certain number of numbers 2020
#  and a certain number of numbers 2021
# .
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases. Then t
#  test cases follow.
#
# Each test case contains one integer n
#  (1≤n≤106
# ) — the number that Polycarp wants to represent as the sum of the numbers 2020
#  and 2021
# .
#
# Output
# For each test case, output on a separate line:
#
# "YES" if the number n
#  is representable as the sum of a certain number of 2020
#  and a certain number of 2021
# ;
# "NO" otherwise.
# You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).
#
# Example
# inputCopy
# 5
# 1
# 4041
# 4042
# 8081
# 8079
# outputCopy
# NO
# YES
# YES
# YES
# NO
# Solution
# C++ O(1) O(1) Math
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        bool found = false;
        for (int x = 0; x <= n / 2020; ++x) {
            int remaining = n - 2020 * x;
            if (remaining >= 0 && remaining % 2021 == 0) {
                found = true;
                break;
            }
        }
        std::cout << (found ? "YES" : "NO") << std::endl;
    }
}
# Python O(1) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        valid: bool = False
        for x in range(n // 2020 + 1):
            remainder: int = n - 2020 * x
            if remainder >= 0 and remainder % 2021 == 0:
                valid = True
                break
        sys.stdout.write(['NO', 'YES'][valid] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
