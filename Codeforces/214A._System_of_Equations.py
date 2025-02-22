# A. System of Equations
# time limit per test2 seconds
# memory limit per test256 megabytes
# Furik loves math lessons very much, so he doesn't attend them, unlike Rubik. But now Furik wants to get a good mark for math. For that Ms. Ivanova, his math teacher, gave him a new task. Furik solved the task immediately. Can you?
#
# You are given a system of equations:
#
#
# You should count, how many there are pairs of integers (a, b) (0 ≤ a, b) which satisfy the system.
#
# Input
# A single line contains two integers n, m (1 ≤ n, m ≤ 1000) — the parameters of the system. The numbers on the line are separated by a space.
#
# Output
# On a single line print the answer to the problem.
#
# Examples
# InputCopy
# 9 3
# OutputCopy
# 1
# InputCopy
# 14 28
# OutputCopy
# 1
# InputCopy
# 4 20
# OutputCopy
# 0
# Note
# In the first sample the suitable pair is integers (3, 0). In the second sample the suitable pair is integers (3, 5). In the third sample there is no suitable pair.
# Solution
# C++ O(a) O(1) Math
#include <bits/stdc++.h>

using namespace std;

void solution() {
    int n, m;
    scanf("%d %d", &n, &m);
    int pairs = 0;
    for (int a = 0; a <= n; ++a) {
        int b = n - pow(a, 2);
        if (b >= 0 && a + pow(b, 2) == m) ++pairs;
    }
    printf("%d\n", pairs);
}


int main() {
    solution();
}

# Python O(a) O(1) Math
import sys


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    pairs: int = 0
    for a in range(n + 1):
        b: int = int(n - a**2)
        if b >= 0 and a + b**2 == m: pairs += 1
    sys.stdout.write(f'{pairs}\n')


if __name__ == '__main__':
    solution()