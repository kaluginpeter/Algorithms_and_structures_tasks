# A. Fibonacciness
# time limit per test1 second
# memory limit per test256 megabytes
# There is an array of 5
#  integers. Initially, you only know a1,a2,a4,a5
# . You may set a3
#  to any positive integer, negative integer, or zero. The Fibonacciness of the array is the number of integers i
#  (1≤i≤3
# ) such that ai+2=ai+ai+1
# . Find the maximum Fibonacciness over all integer values of a3
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤500
# ) — the number of test cases.
#
# The only line of each test case contains four integers a1,a2,a4,a5
#  (1≤ai≤100
# ).
#
# Output
# For each test case, output the maximum Fibonacciness on a new line.
#
# Example
# InputCopy
# 6
# 1 1 3 5
# 1 3 2 1
# 8 10 28 100
# 100 1 100 1
# 1 100 1 100
# 100 100 100 100
# OutputCopy
# 3
# 2
# 2
# 1
# 1
# 2
# Note
# In the first test case, we can set a3
#  to 2
#  to achieve the maximal Fibonacciness of 3
# .
#
# In the third test case, it can be shown that 2
#  is the maximum Fibonacciness that can be achieved. This can be done by setting a3
#  to 18
# .
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int a1, a2, a4, a5;
        std::scanf("%d %d %d %d", &a1, &a2, &a4, &a5);
        int maxFib = 1;
        // 1 case a1 + a2
        int x = a1 + a2;
        if (a2 + x == a4) ++maxFib;
        if (x + a4 == a5) ++maxFib;
        // 2 case a4 - a2
        x = a4 - a2;
        int fibs = 1;
        if (a1 + a2 == x) ++fibs;
        if (x + a4 == a5) ++fibs;
        std::printf("%d\n", std::max(maxFib, fibs));
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
        a1, a2, a4, a5 = map(int, sys.stdin.readline().rstrip().split())
        max_fibs: int = 1
        x: int = a1 + a2
        if a2 + x == a4: max_fibs += 1
        if x + a4 == a5: max_fibs += 1
        fibs: int = 1
        x = a4 - a2
        if a1 + a2 == x: fibs += 1
        if x + a4 == a5: fibs += 1
        sys.stdout.write('{}\n'.format(max(max_fibs, fibs)))


if __name__ == '__main__':
    solution()