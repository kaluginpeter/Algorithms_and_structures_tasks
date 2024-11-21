# A. Dreamoon and Stairs
# time limit per test1 second
# memory limit per test256 megabytes
# Dreamoon wants to climb up a stair of n steps. He can climb 1 or 2 steps at each move. Dreamoon wants the number of moves to be a multiple of an integer m.
#
# What is the minimal number of moves making him climb to the top of the stairs that satisfies his condition?
#
# Input
# The single line contains two space separated integers n, m (0 < n ≤ 10000, 1 < m ≤ 10).
#
# Output
# Print a single integer — the minimal number of moves being a multiple of m. If there is no way he can climb satisfying condition print  - 1 instead.
#
# Examples
# InputCopy
# 10 2
# OutputCopy
# 6
# InputCopy
# 3 5
# OutputCopy
# -1
# Note
# For the first sample, Dreamoon could climb in 6 moves with following sequence of steps: {2, 2, 2, 2, 1, 1}.
#
# For the second sample, there are only three valid sequence of steps {2, 1}, {1, 2}, {1, 1, 1} with 2, 2, and 3 steps respectively. All these numbers are not multiples of 5.
# Solution
# C++ O(logN) O(1) Math
#include <iostream>

void solution(int n, int m) {
    int big = n / 2;
    n %= 2;
    while ((big + n) % m != 0) {
        if (!big) {
            break;
        }
        --big;
        n += 2;
    }
    std::cout << ((big + n) % m == 0? big + n : -1) << "\n";
}

int main() {
    int n, m;
    std::cin >> n >> m;
    solution(n, m);
}
# Python O(logN) O(1) Math
import sys


def solution(n: int, m: int) -> None:
    big: int = n // 2
    n %= 2
    while (big + n) % m != 0:
        if not big:
            break
        big -= 1
        n += 2
    sys.stdout.write(str([-1, big + n][(big + n) % m == 0]) + '\n')
if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().rstrip().split())
    solution(n, m)