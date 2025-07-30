# C. Brr Brrr Patapim
# time limit per test2 seconds
# memory limit per test256 megabytes
# Brr Brrr Patapim is trying to learn of Tiramisù's secret passcode, which is a permutation∗
#  of 2⋅n
#  elements. To help Patapim guess, Tiramisù gave him an n×n
#  grid G
# , in which Gi,j
#  (or the element in the i
# -th row and j
# -th column of the grid) contains pi+j
# , or the (i+j)
# -th element in the permutation.
#
# Given this grid, please help Patapim crack the forgotten code. It is guaranteed that the permutation exists, and it can be shown that the permutation can be determined uniquely.
#
# ∗
# A permutation of m
#  integers is a sequence of m
#  integers which contains each of 1,2,…,m
#  exactly once. For example, [1,3,2]
#  and [2,1]
#  are permutations, while [1,2,4]
#  and [1,3,2,3]
#  are not.
#
# Input
# The first line contains an integer t
#  — the number of test cases (1≤t≤200
# ).
#
# The first line of each test case contains an integer n
#  (1≤n≤800
# ).
#
# Each of the following n
#  lines contains n
#  integers, giving the grid G
# . The first of these lines contains G1,1,G1,2,…,G1,n
# ; the second of these lines contains G2,1,G2,2,…,G2,n
# , and so on. (1≤Gi,j≤2⋅n
# ).
#
# It is guaranteed that the grid encodes a valid permutation, and the sum of n
#  over all test cases does not exceed 800
# .
#
# Output
# For each test case, please output 2n
#  numbers on a new line: p1,p2,…,p2n
# .
#
# Example
# InputCopy
# 3
# 3
# 1 6 2
# 6 2 4
# 2 4 3
# 1
# 1
# 2
# 2 3
# 3 4
# OutputCopy
# 5 1 6 2 4 3
# 2 1
# 1 2 3 4
# Solution
# C++ O(N) O(N) Greedy
#include <iostream>
#include <vector>


void solution() {
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> grid(n, std::vector<int>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) std::cin >> grid[i][j];
    }
    std::vector<int> nums(2 * n + 1, -1);
    std::vector<bool> seen(2 * n + 1, false);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            nums[i + j + 2] = grid[i][j];
            seen[grid[i][j]] = true;
        }
    }
    int missed = 0;
    for (int i = 1; i <= 2 * n; ++i) {
        if (!seen[i]) {
            missed = i;
            break;
        }
    }
    for (int i = 1; i <= 2 * n; ++i) {
        if (nums[i] != -1) std::cout << nums[i];
        else std::cout << missed;
        std::cout << " ";
    }
    std::cout << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(N) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    seen: list[int] = [False] * (2 * n + 1)
    nums: list[int] = [-1] * (2 * n + 1)
    for i in range(n):
        row: iter[int] = map(int, sys.stdin.readline().rstrip().split())
        for j in range(n):
            x: int = next(row)
            nums[i + j + 2] = x
            seen[x] = True
    missed: int = 0
    for i in range(1, 2 * n + 1):
        if not seen[i]:
            missed = i
            break
    for i in range(1, 2 * n + 1):
        if nums[i] != -1: sys.stdout.write('{} '.format(str(nums[i])))
        else: sys.stdout.write('{} '.format(str(missed)))
    sys.stdout.write('\n')



if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()