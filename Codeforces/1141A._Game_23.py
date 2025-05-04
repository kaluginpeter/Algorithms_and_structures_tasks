# A. Game 23
# time limit per test1 second
# memory limit per test256 megabytes
# Polycarp plays "Game 23". Initially he has a number n
#  and his goal is to transform it to m
# . In one move, he can multiply n
#  by 2
#  or multiply n
#  by 3
# . He can perform any number of moves.
#
# Print the number of moves needed to transform n
#  to m
# . Print -1 if it is impossible to do so.
#
# It is easy to prove that any way to transform n
#  to m
#  contains the same number of moves (i.e. number of moves doesn't depend on the way of transformation).
#
# Input
# The only line of the input contains two integers n
#  and m
#  (1≤n≤m≤5⋅108
# ).
#
# Output
# Print the number of moves to transform n
#  to m
# , or -1 if there is no solution.
#
# Examples
# InputCopy
# 120 51840
# OutputCopy
# 7
# InputCopy
# 42 42
# OutputCopy
# 0
# InputCopy
# 48 72
# OutputCopy
# -1
# Note
# In the first example, the possible sequence of moves is: 120→240→720→1440→4320→12960→25920→51840.
#  The are 7
#  steps in total.
#
# In the second example, no moves are needed. Thus, the answer is 0
# .
#
# In the third example, it is impossible to transform 48
#  to 72
# .
# Solution
# C++ O(logN) O(1) Math
#include <iostream>


void solution() {
    int n, m;
    std::scanf("%d %d", &n, &m);
    if (n == m) {
        std::printf("0\n");
        return;
    }
    if (m % n != 0) {
        std::printf("-1\n");
        return;
    }
    int q = m / n;
    int moves = 0;
    while (q % 2 == 0) {
        ++moves;
        q /= 2;
    }
    while (q % 3 == 0) {
        ++moves;
        q /= 3;
    }
    std::printf("%d\n", (q == 1 ? moves : -1));
}


int main() {
    solution();
}

# Python O(logN) O(1) Math
import sys


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == m:
        sys.stdout.write('0\n')
        return
    if m % n != 0:
        sys.stdout.write('-1\n')
        return
    q: int = m // n
    moves: int = 0
    while q % 2 == 0:
        moves += 1
        q //= 2
    while q % 3 == 0:
        moves += 1
        q //= 3
    sys.stdout.write('{}\n'.format([-1, moves][q == 1]))


if __name__ == '__main__':
    solution()