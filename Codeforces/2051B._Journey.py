# B. Journey
# time limit per test1 second
# memory limit per test256 megabytes
# Monocarp decided to embark on a long hiking journey.
#
# He decided that on the first day he would walk a
#  kilometers, on the second day he would walk b
#  kilometers, on the third day he would walk c
#  kilometers, on the fourth day, just like on the first, he would walk a
#  kilometers, on the fifth day, just like on the second, he would walk b
#  kilometers, on the sixth day, just like on the third, he would walk c
#  kilometers, and so on.
#
# Monocarp will complete his journey on the day when he has walked at least n
#  kilometers in total. Your task is to determine the day on which Monocarp will complete his journey.
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each test case consists of one line containing four integers n
# , a
# , b
# , c
#  (1≤n≤109
# ; 1≤a,b,c≤106
# ).
#
# Output
# For each test case, output one integer — the day on which Monocarp will have walked at least n
#  kilometers in total and will complete his journey.
#
# Example
# InputCopy
# 4
# 12 1 5 3
# 6 6 7 4
# 16 3 4 1
# 1000000000 1 1 1
# OutputCopy
# 5
# 1
# 6
# 1000000000
# Note
# In the first example, over the first four days, Monocarp will cover 1+5+3+1=10
#  kilometers. On the fifth day, he will cover another 5
#  kilometers, meaning that in total over five days he will have covered 10+5=15
#  kilometers. Since n=12
# , Monocarp will complete his journey on the fifth day.
#
# In the second example, Monocarp will cover 6
#  kilometers on the first day. Since n=6
# , Monocarp will complete his journey on the very first day.
#
# In the third example, Monocarp will cover 3+4+1+3+4+1=16
#  kilometers over the first six days. Since n=16
# , Monocarp will complete his journey on the sixth day.
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, a, b, c;
        std::scanf("%d %d %d %d", &n, &a, &b, &c);
        int leap = a + b + c;
        int wholes = n / leap;
        n %= leap;
        wholes *= 3;
        if (n > 0) {
            ++wholes;
            n -= a;
        }
        if (n > 0) {
            ++wholes;
            n -= b;
        }
        if (n > 0) ++wholes;
        std::printf("%d\n", wholes);
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
        n, a, b, c = map(int, sys.stdin.readline().rstrip().split())
        leap: int = a + b + c
        wholes: int = n // leap * 3
        n %= leap
        if n > 0:
            wholes += 1
            n -= a
        if n > 0:
            wholes += 1
            n -= b
        if n > 0: wholes += 1
        sys.stdout.write('{}\n'.format(wholes))


if __name__ == '__main__':
    solution()