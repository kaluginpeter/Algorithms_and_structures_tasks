# A. Pashmak and Garden
# time limit per test1 second
# memory limit per test256 megabytes
# Pashmak has fallen in love with an attractive girl called Parmida since one year ago...
#
# Today, Pashmak set up a meeting with his partner in a romantic garden. Unfortunately, Pashmak has forgotten where the garden is. But he remembers that the garden looks like a square with sides parallel to the coordinate axes. He also remembers that there is exactly one tree on each vertex of the square. Now, Pashmak knows the position of only two of the trees. Help him to find the position of two remaining ones.
#
# Input
# The first line contains four space-separated x1, y1, x2, y2 ( - 100 ≤ x1, y1, x2, y2 ≤ 100) integers, where x1 and y1 are coordinates of the first tree and x2 and y2 are coordinates of the second tree. It's guaranteed that the given points are distinct.
#
# Output
# If there is no solution to the problem, print -1. Otherwise print four space-separated integers x3, y3, x4, y4 that correspond to the coordinates of the two other trees. If there are several solutions you can output any of them.
#
# Note that x3, y3, x4, y4 must be in the range ( - 1000 ≤ x3, y3, x4, y4 ≤ 1000).
#
# Examples
# InputCopy
# 0 0 0 1
# OutputCopy
# 1 0 1 1
# InputCopy
# 0 0 1 1
# OutputCopy
# 0 1 1 0
# InputCopy
# 0 0 1 2
# OutputCopy
# -1
# Solution
# C++ O(1) O(1) ConstructiveAlgorithm
#include <iostream>
#include <cmath>


void solution() {
    int x1, y1, x2, y2;
    std::scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    if (x1 == x2) {
        int diff = std::abs(y1 - y2);
        if (x1 + diff <= 1000) {
            std::printf("%d %d %d %d\n", x1 + diff, y1, x2 + diff, y2);
            return;
        } else {
            std::printf("%d %d %d %d\n", x1 - diff, y1, x2 - diff, y2);
            return;
        }
    } else if (y1 == y2) {
        int diff = std::abs(x1 - x2);
        if (y1 + diff <= 1000) {
            std::printf("%d %d %d %d\n", x1, y1 + diff, x2, y2 + diff);
            return;
        } else {
            std::printf("%d %d %d %d\n", x1, y1 - diff, x2, y2 - diff);
            return;
        }
    } else if (y1 > y2) {
        if (x1 > x2) {
            int diff = x1 - x2;
            if (diff != y1 - y2) {
                std::printf("-1\n");
                return;
            }
            std::printf("%d %d %d %d\n", x1, y1 - diff, x1 - diff, y1);
            return;
        } else {
            int diff = y1 - y2;
            if (diff != x2 - x1) {
                std::printf("-1\n");
                return;
            }
            std::printf("%d %d %d %d\n", x1 + diff, y1, x1, y1 - diff);
            return;
        }
    } else {
        if (x2 > x1) {
            int diff = x2 - x1;
            if (diff != y2 - y1) {
                std::printf("-1\n");
                return;
            }
            std::printf("%d %d %d %d\n", x2, y2 - diff, x2 - diff, y2);
            return;
        } else {
            int diff = y2 - y1;
            if (diff != x1 - x2) {
                std::printf("-1\n");
                return;
            }
            std::printf("%d %d %d %d\n", x2 + diff, y2, x2, y2 - diff);
            return;
        }
    }
}


int main() {
    solution();
}

# Python O(1) O(1) ConstructiveAlgorithm
import sys


def solution() -> None:
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    if x1 == x2:
        diff: int = abs(y1 - y2)
        if x1 + diff <= 1000:
            sys.stdout.write('{} {} {} {}\n'.format(x1 + diff, y1, x2 + diff, y2))
            return
        else:
            sys.stdout.write('{} {} {} {}\n'.format(x1 - diff, y1, x2 - diff, y2))
            return
    elif y1 == y2:
        diff: int = abs(x1 - x2)
        if y1 + diff <= 1000:
            sys.stdout.write('{} {} {} {}\n'.format(x1, y1 + diff, x2, y2 + diff))
            return
        else:
            sys.stdout.write('{} {} {} {}\n'.format(x1, y1 - diff, x2, y2 - diff))
            return
    elif y1 > y2:
        if x1 > x2:
            diff: int = x1 - x2
            if diff != y1 - y2:
                sys.stdout.write('-1\n')
                return
            sys.stdout.write('{} {} {} {}\n'.format(x1, y1 - diff, x1 - diff, y1))
            return
        else:
            diff: int = y1 - y2
            if diff != x2 - x1:
                sys.stdout.write('-1\n')
                return
            sys.stdout.write('{} {} {} {}\n'.format(x1 + diff, y1, x1, y1 - diff))
            return
    else:
        if x2 > x1:
            diff: int = x2 - x1
            if diff != y2 - y1:
                sys.stdout.write('-1\n')
                return
            sys.stdout.write('{} {} {} {}\n'.format(x2, y2 - diff, x2 - diff, y2))
            return
        else:
            diff: int = y2 - y1
            if diff != x1 - x2:
                sys.stdout.write('-1\n')
                return
            sys.stdout.write('{} {} {} {}\n'.format(x2 + diff, y2, x2, y2 - diff))
            return



if __name__ == '__main__':
    solution()