# A. A+B?
# time limit per test2 seconds
# memory limit per test512 megabytes
# You are given an expression of the form a+b
# , where a
#  and b
#  are integers from 0
#  to 9
# . You have to evaluate it and print the result.
#
# Input
# The first line contains one integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# Each test case consists of one line containing an expression of the form a+b
#  (0≤a,b≤9
# , both a
#  and b
#  are integers). The integers are not separated from the +
#  sign.
#
# Output
# For each test case, print one integer — the result of the expression.
#
# Example
# inputCopy
# 4
# 4+2
# 0+0
# 3+7
# 8+9
# outputCopy
# 6
# 0
# 10
# 17
# Solution
# C++ O(1) O(1) Math String
#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string n;
        std::cin >> n;
        std:: cout << n[0] - '0' + n[n.size() - 1] - '0' << std::endl;
    }
}

# Python O(1) O(1) Math String
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: str = sys.stdin.readline().rstrip()
        sys.stdout.write(str(eval(n)) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
