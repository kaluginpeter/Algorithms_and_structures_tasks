# A. Food for Animals
# time limit per test1 second
# memory limit per test256 megabytes
# In the pet store on sale there are:
#
# a
#  packs of dog food;
# b
#  packs of cat food;
# c
#  packs of universal food (such food is suitable for both dogs and cats).
# Polycarp has x
#  dogs and y
#  cats. Is it possible that he will be able to buy food for all his animals in the store? Each of his dogs and each of his cats should receive one pack of suitable food for it.
#
# Input
# The first line of input contains an integer t
#  (1≤t≤104
# ) — the number of test cases in the input.
#
# Then t
#  lines are given, each containing a description of one test case. Each description consists of five integers a,b,c,x
#  and y
#  (0≤a,b,c,x,y≤108
# ).
#
# Output
# For each test case in a separate line, output:
#
# YES, if suitable food can be bought for each of x
#  dogs and for each of y
#  cats;
# NO else.
# You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as a positive response).
#
# Example
# InputCopy
# 7
# 1 1 4 2 3
# 0 0 0 0 0
# 5 5 0 4 6
# 1 1 1 1 1
# 50000000 50000000 100000000 100000000 100000000
# 0 0 0 100000000 100000000
# 1 3 2 2 5
# OutputCopy
# YES
# YES
# NO
# YES
# YES
# NO
# NO
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int a, b, c, x, y;
        std::scanf("%d %d %d %d %d", &a, &b, &c, &x, &y);
        if (x <= a) x = 0;
        else {
            int extra = x - a;
            if (extra > c) {
                std::cout << "NO\n";
                continue;
            }
            c -= extra;
        }
        if (y <= b) y = 0;
        else {
            int extra = y - b;
            if (extra && extra > c) {
                std::cout << "NO\n";
                continue;
            }
        }
        std::cout << "YES\n";
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        a, b, c, x, y = map(int, sys.stdin.readline().rstrip().split())
        if x > a:
            extra: int = x - a
            if extra > c:
                sys.stdout.write('NO\n')
                continue
            c -= extra
        if y > b:
            extra: int = y - b
            if extra > c:
                sys.stdout.write('NO\n')
                continue
        sys.stdout.write('YES\n')


if __name__ == '__main__':
    solution()