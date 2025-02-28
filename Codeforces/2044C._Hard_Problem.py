# C. Hard Problem
# time limit per test1 second
# memory limit per test256 megabytes
# Ball is the teacher in Paperfold University. The seats of his classroom are arranged in 2
#  rows with m
#  seats each.
#
# Ball is teaching a+b+c
#  monkeys, and he wants to assign as many monkeys to a seat as possible. Ball knows that a
#  of them only want to sit in row 1
# , b
#  of them only want to sit in row 2
# , and c
#  of them have no preference. Only one monkey may sit in each seat, and each monkey's preference must be followed if it is seated.
#
# What is the maximum number of monkeys that Ball can seat?
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each test case contains four integers m
# , a
# , b
# , and c
#  (1≤m,a,b,c≤108
# ).
#
# Output
# For each test case, output the maximum number of monkeys you can seat.
#
# Example
# InputCopy
# 5
# 10 5 5 10
# 3 6 1 1
# 15 14 12 4
# 1 1 1 1
# 420 6 9 69
# OutputCopy
# 20
# 5
# 30
# 2
# 84
# Note
# In the second test case, 6
#  monkeys want to sit in the front row, but only 3
#  seats are available. The monkeys that have no preference and the monkeys who prefer sitting in the second row can sit in the second row together. Thus, the answer is 3+2=5
# .
# Solution
# C++ O(1) O(1) Math Greedy
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int m, a, b, c;
        std::scanf("%d %d %d %d", &m, &a, &b, &c);
        int seats = 0;
        seats += std::min(m, a);
        seats += std::min(m, b);
        seats += std::min(m - std::min(m, a) + m - std::min(m, b), c);
        std::printf("%d\n", seats);
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        m, a, b, c = map(int, sys.stdin.readline().rstrip().split())
        seats: int = 0
        seats += min(m, a)
        seats += min(m, b)
        seats += min(m - min(m, a) + m - min(m, b), c)
        sys.stdout.write(f'{seats}\n')


if __name__ == '__main__':
    solution()