# A. C+=
# time limit per test2 seconds
# memory limit per test512 megabytes
# Leo has developed a new programming language C+=. In C+=, integer variables can only be changed with a "+=" operation that adds the right-hand side value to the left-hand side variable. For example, performing "a += b" when a = 2
# , b = 3
#  changes the value of a to 5
#  (the value of b does not change).
#
# In a prototype program Leo has two integer variables a and b, initialized with some positive values. He can perform any number of operations "a += b" or "b += a". Leo wants to test handling large integers, so he wants to make the value of either a or b strictly greater than a given value n
# . What is the smallest number of operations he has to perform?
#
# Input
# The first line contains a single integer T
#  (1≤T≤100
# ) — the number of test cases.
#
# Each of the following T
#  lines describes a single test case, and contains three integers a,b,n
#  (1≤a,b≤n≤109
# ) — initial values of a and b, and the value one of the variables has to exceed, respectively.
#
# Output
# For each test case print a single integer — the smallest number of operations needed. Separate answers with line breaks.
#
# Example
# InputCopy
# 2
# 1 2 3
# 5 4 100
# OutputCopy
# 2
# 7
# Note
# In the first case we cannot make a variable exceed 3
#  in one operation. One way of achieving this in two operations is to perform "b += a" twice.
# Solution
# C++ O(logN) O(1) Math
#include <iostream>


void solution(int& t) {
    for (int i = 0; i < t; ++i) {
        int a, b, n;
        std::cin >> a >> b >> n;
        int steps = 0;
        if (a < b) {
            int c = a;
            a = b;
            b = c;
        }
        while (std::max(a, b) <= n) {
            ++steps;
            if (steps % 2 != 0) {
                b += a;
            } else {
                a += b;
            }
        }
        std::cout << steps << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}
# Python O(logN) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        a, b, n = map(int, sys.stdin.readline().rstrip().split())
        if a < b:
            a, b = b, a
        steps: int = 0
        while max(a, b) <= n:
            steps += 1
            if steps & 1:
                b += a
            else:
                a += b
        sys.stdout.write(f'{steps}\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
