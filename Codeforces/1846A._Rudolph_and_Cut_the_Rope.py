# A. Rudolph and Cut the Rope
# time limit per test2 seconds
# memory limit per test256 megabytes
# There are n
#  nails driven into the wall, the i
# -th nail is driven ai
#  meters above the ground, one end of the bi
#  meters long rope is tied to it. All nails hang at different heights one above the other. One candy is tied to all ropes at once. Candy is tied to end of a rope that is not tied to a nail.
#
# To take the candy, you need to lower it to the ground. To do this, Rudolph can cut some ropes, one at a time. Help Rudolph find the minimum number of ropes that must be cut to get the candy.
#
# The figure shows an example of the first test:
#
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains one integer n
#  (1≤n≤50
# ) — the number of nails.
#
# The i
# -th of the next n
#  lines contains two integers ai
#  and bi
#  (1≤ai,bi≤200
# ) — the height of the i
# -th nail and the length of the rope tied to it, all ai
#  are different.
#
# It is guaranteed that the data is not contradictory, it is possible to build a configuration described in the statement.
#
# Output
# For each test case print one integer — the minimum number of ropes that need to be cut to make the candy fall to the ground.
#
# Example
# InputCopy
# 4
# 3
# 4 3
# 3 1
# 1 2
# 4
# 9 2
# 5 2
# 7 7
# 3 4
# 5
# 11 7
# 5 10
# 12 9
# 3 2
# 1 5
# 3
# 5 6
# 4 5
# 7 7
# OutputCopy
# 2
# 2
# 3
# 0
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        int cuts = 0;
        for (int j = 0; j < n; ++j) {
            int x, y;
            std::scanf("%d %d", &x, &y);
            if (x > y) ++cuts;
        }
        std::printf("%d\n", cuts);
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        cuts: int = 0
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().rstrip().split())
            if x > y: cuts += 1
        sys.stdout.write('{}\n'.format(cuts))


if __name__ == '__main__':
    solution()