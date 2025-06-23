# C. Those Who Are With Us
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a matrix of integers with n
#  rows and m
#  columns. The cell at the intersection of the i
# -th row and the j
# -th column contains the number aij
# .
#
# You can perform the following operation exactly once:
#
# Choose two numbers 1≤r≤n
#  and 1≤c≤m
# .
# For all cells (i,j)
#  in the matrix such that i=r
#  or j=c
# , decrease aij
#  by one.
# You need to find the minimal possible maximum value in the matrix a
#  after performing exactly one such operation.
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and m
#  (1≤n⋅m≤105
# ) — the number of rows and columns in the matrix.
#
# The next n
#  lines of each test case describe the matrix a
# . The i
# -th line contains m
#  integers ai1,ai2,…,aim
#  (1≤aij≤100
# ) — the elements in the i
# -th row of the matrix.
#
# It is guaranteed that the sum of n⋅m
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output the minimum maximum value in the matrix a
#  after performing exactly one operation.
#
# Example
# InputCopy
# 10
# 1 1
# 1
# 1 2
# 1 2
# 2 1
# 2
# 1
# 2 2
# 4 2
# 3 4
# 3 4
# 1 2 3 2
# 3 2 1 3
# 2 1 3 2
# 4 3
# 1 5 1
# 3 1 3
# 5 5 5
# 3 5 1
# 4 4
# 1 3 3 2
# 2 3 2 2
# 1 2 2 1
# 3 3 2 3
# 2 2
# 2 2
# 1 2
# 3 2
# 1 2
# 2 1
# 1 2
# 3 3
# 2 1 1
# 1 2 1
# 1 1 2
# OutputCopy
# 0
# 1
# 1
# 3
# 2
# 4
# 3
# 1
# 1
# 2
# Note
# In the first three test cases, you can choose r=1
#  and c=1
# .
#
# In the fourth test case, you can choose r=1
#  and c=2
# .
#
#
# In the fifth test case, you can choose r=2
#  and c=3
# .
#
#
# In the sixth test case, you can choose r=3
#  and c=2
# .
# Solution
# C++ O(NM) O(NM) Greedy HashSet
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

void solve() {
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> grid(n, std::vector<int>(m));
    int max_val = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            std::cin >> grid[i][j];
            if (grid[i][j] > max_val) max_val = grid[i][j];
        }
    }
    std::vector<std::pair<int, int>> max_locations;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == max_val) max_locations.push_back({i, j});
        }
    }
    if (max_locations.size() <= 1) {
        std::cout << max_val - 1 << std::endl;
        return;
    }
    bool can_cover_all = false;
    int r1 = max_locations[0].first;
    int c1 = max_locations[0].second;
    std::unordered_set<int> remaining_cols;
    for (const auto& loc : max_locations) {
        if (loc.first != r1) remaining_cols.insert(loc.second);
    }
    if (remaining_cols.size() <= 1) can_cover_all = true;

    if (!can_cover_all) {
        std::unordered_set<int> remaining_rows;
        for (const auto& loc : max_locations) {
            if (loc.second != c1) remaining_rows.insert(loc.first);
        }
        if (remaining_rows.size() <= 1) can_cover_all = true;
    }
    std::cout << (can_cover_all ? max_val - 1 : max_val) << std::endl;

}

void solution() {
    int t;
    std::cin >> t;
    while (t > 0) {
        solve();
        --t;
    }
}


int main() {
    solution();
}

# Python O(NM) O(NM) Greedy HashSet
import sys


def solve() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    grid: list[list[int]] = []
    for _ in range(n):
        row: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        grid.append(row)
    max_val: int = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > max_val: max_val = grid[i][j]
    max_locations: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == max_val: max_locations.append((i, j))

    if len(max_locations) <= 1:
        sys.stdout.write('{}\n'.format(max_val - 1))
        return
    can_cover_all: bool = False
    r1: int = max_locations[0][0]
    c1: int = max_locations[0][1]
    remaining_cols: set[int] = set()
    for r, c in max_locations:
        if r != r1: remaining_cols.add(c)
    if len(remaining_cols) <= 1: can_cover_all = True
    if not can_cover_all:
        remaining_rows: set[int] = set()
        for r, c in max_locations:
            if c != c1: remaining_rows.add(r)
        if len(remaining_rows) <= 1: can_cover_all = True

    sys.stdout.write('{}\n'.format([max_val, max_val - 1][can_cover_all]))


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solve()


if __name__ == '__main__':
    solution()