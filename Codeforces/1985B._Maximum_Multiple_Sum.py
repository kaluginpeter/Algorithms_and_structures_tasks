# B. Maximum Multiple Sum
# time limit per test1 second
# memory limit per test256 megabytes
# Given an integer n
# , find an integer x
#  such that:
#
# 2≤x≤n
# .
# The sum of multiples of x
#  that are less than or equal to n
#  is maximized. Formally, x+2x+3x+⋯+kx
#  where kx≤n
#  is maximized over all possible values of x
# .
# Input
# The first line contains t
#  (1≤t≤100
# ) — the number of test cases.
#
# Each test case contains a single integer n
#  (2≤n≤100
# ).
#
# Output
# For each test case, output an integer, the optimal value of x
# . It can be shown there is only one unique answer.
#
# Example
# InputCopy
# 2
# 3
# 15
# OutputCopy
# 3
# 2
# Note
# For n=3
# , the possible values of x
#  are 2
#  and 3
# . The sum of all multiples of 2
#  less than or equal to n
#  is just 2
# , and the sum of all multiples of 3
#  less than or equal to n
#  is 3
# . Therefore, 3
#  is the optimal value of x
# .
#
# For n=15
# , the optimal value of x
#  is 2
# . The sum of all multiples of 2
#  less than or equal to n
#  is 2+4+6+8+10+12+14=56
# , which can be proven to be the maximal over all other possible values of x
# .
# Solution
# C++ O(N) O(1) Math Brute Force
#include <iostream>


int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        int totalSum = 0;
        int choice = 0;
        for (int num = 2; num <= n; ++num) {
            int curSum = 0;
            int mod = num;
            while (mod <= n) {
                curSum += mod;
                mod += num;
            }
            if (curSum > totalSum) {
                totalSum = curSum;
                choice = num;
            }
        }
        std::cout << choice << std::endl;
    }
}

# Python O(N) O(1) Math Brute Force
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        total_sum: int = 0
        choice: int = 0
        for num in range(2, n + 1):
            cur_sum: int = 0
            mod: int = num
            while mod <= n:
                cur_sum += mod
                mod += num
            if cur_sum > total_sum:
                total_sum = cur_sum
                choice = num
        sys.stdout.write(str(choice) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
