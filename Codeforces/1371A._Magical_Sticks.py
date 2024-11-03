# A. Magical Sticks
# time limit per test1 second
# memory limit per test256 megabytes
# A penguin Rocher has n
#  sticks. He has exactly one stick with length i
#  for all 1≤i≤n
# .
#
# He can connect some sticks. If he connects two sticks that have lengths a
#  and b
# , he gets one stick with length a+b
# . Two sticks, that were used in the operation disappear from his set and the new connected stick appears in his set and can be used for the next connections.
#
# He wants to create the maximum number of sticks that have the same length. It is not necessary to make all sticks have the same length, some sticks can have the other length. How many sticks with the equal length he can create?
#
# Input
# The input consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases. Next t
#  lines contain descriptions of test cases.
#
# For each test case, the only line contains a single integer n
#  (1≤n≤109
# ).
#
# Output
# For each test case, print a single integer  — the answer to the problem.
#
# Example
# InputCopy
# 4
# 1
# 2
# 3
# 4
# OutputCopy
# 1
# 1
# 2
# 2
# Note
# In the third case, he can connect two sticks with lengths 1
#  and 2
#  and he will get one stick with length 3
# . So, he will have two sticks with lengths 3
# .
#
# In the fourth case, he can connect two sticks with lengths 1
#  and 3
#  and he will get one stick with length 4
# . After that, he will have three sticks with lengths {2,4,4}
# , so two sticks have the same length, and one stick has the other length.
# Solution
# C++ O(1) O(1) Math
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::cout << (n + 1) / 2 << std::endl;
    }
}

# Python O(1) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        sys.stdout.write(str((n + 1) // 2) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
