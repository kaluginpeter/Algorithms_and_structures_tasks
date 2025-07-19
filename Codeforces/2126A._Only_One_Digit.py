# A. Only One Digit
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an integer x
# . You need to find the smallest non-negative integer y
#  such that the numbers x
#  and y
#  share at least one common digit. In other words, there must exist a decimal digit d
#  that appears in both the representation of the number x
#  and the number y
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains one integer x
#  (1≤x≤1000
# ).
#
# Output
# For each test case, output one integer y
#  — the minimum non-negative number that satisfies the condition.
#
# Example
# InputCopy
# 5
# 6
# 96
# 78
# 122
# 696
# OutputCopy
# 6
# 6
# 7
# 1
# 6
# Note
# In the first test case, the numbers 6
#  and 6
#  share the common digit '6'. Moreover, there is no natural number smaller than this that shares a common digit.
#
# In the second test case, the numbers 6
#  and 96
#  share the common digit '6'.
# Solution
# C++ O(logN) O(1) Greedy
#include <iostream>


void solution() {
    int n;
    std::cin >> n;
    int output = 9;
    while (n) {
        output = std::min(output, n % 10);
        n /= 10;
    }
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(logN) O(1) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    output: int = 9
    while n:
        output = min(output, n % 10)
        n //= 10
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()