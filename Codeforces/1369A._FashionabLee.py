# A. FashionabLee
# time limit per test2 seconds
# memory limit per test256 megabytes
# Lee is going to fashionably decorate his house for a party, using some regular convex polygons...
#
# Lee thinks a regular n
# -sided (convex) polygon is beautiful if and only if he can rotate it in such a way that at least one of its edges is parallel to the OX
# -axis and at least one of its edges is parallel to the OY
# -axis at the same time.
#
# Recall that a regular n
# -sided polygon is a convex polygon with n
#  vertices such that all the edges and angles are equal.
#
# Now he is shopping: the market has t
#  regular polygons. For each of them print YES if it is beautiful and NO otherwise.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of polygons in the market.
#
# Each of the next t
#  lines contains a single integer ni
#  (3≤ni≤109
# ): it means that the i
# -th polygon is a regular ni
# -sided polygon.
#
# Output
# For each polygon, print YES if it's beautiful or NO otherwise (case insensitive).
#
# Example
# InputCopy
# 4
# 3
# 4
# 12
# 1000000000
# OutputCopy
# NO
# YES
# YES
# YES
# Note
# In the example, there are 4
#  polygons in the market. It's easy to see that an equilateral triangle (a regular 3
# -sided polygon) is not beautiful, a square (a regular 4
# -sided polygon) is beautiful and a regular 12
# -sided polygon (is shown below) is beautiful as well.
# Solution
# C++ O(1) O(1) Math
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::cout << (n % 4 == 0? "YES" : "NO") << "\n";
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
        n: int = int(sys.stdin.readline().rstrip())
        sys.stdout.write(['NO', 'YES'][n % 4 == 0] + '\n')


if __name__ == '__main__':
    solution()