# D. 1D Eraser
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a strip of paper s
#  that is n
#  cells long. Each cell is either black or white. In an operation you can take any k
#  consecutive cells and make them all white.
#
# Find the minimum number of operations needed to remove all black cells.
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤k≤n≤2⋅105
# ) — the length of the paper and the integer used in the operation.
#
# The second line of each test case contains a string s
#  of length n
#  consisting of characters B
#  (representing a black cell) or W
#  (representing a white cell).
#
# The sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output a single integer — the minimum number of operations needed to remove all black cells.
#
# Example
# InputCopy
# 8
# 6 3
# WBWWWB
# 7 3
# WWBWBWW
# 5 4
# BWBWB
# 5 5
# BBBBB
# 8 2
# BWBWBBBB
# 10 2
# WBBWBBWBBW
# 4 1
# BBBB
# 3 2
# WWW
# OutputCopy
# 2
# 1
# 2
# 1
# 4
# 3
# 4
# 0
# Note
# In the first test case you can perform the following operations:
# WBWWWB→WWWWWB→WWWWWW
#
# In the second test case you can perform the following operations:
# WWBWBWW→WWWWWWW
#
# In the third test case you can perform the following operations:
# BWBWB→BWWWW→WWWWW
# Solution
# C++ O(N) O(1) Sliding Window Greedy
#include <bits/stdc++.h>
using namespace std;


void solution() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, k;
        cin >> n >> k;
        string pattern;
        cin >> pattern;
        int operations = 0;
        int left = 0;
        while (left < n) {
            if (pattern[left] == 'B') {
                left += k - 1;
                ++operations;
            }
            ++left;
        }
        printf("%d\n", operations);
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Sliding Window Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().rstrip().split())
        pattern: str = sys.stdin.readline().rstrip()
        left: int = 0
        operations: int = 0
        while left < n:
            if pattern[left] == 'B':
                left += k - 1
                operations += 1
            left += 1
        sys.stdout.write(f'{operations}\n')


if __name__ == '__main__':
    solution()