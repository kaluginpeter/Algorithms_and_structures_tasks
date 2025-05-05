# A. Gift Carpet
# time limit per test1 second
# memory limit per test256 megabytes
# Recently, Tema and Vika celebrated Family Day. Their friend Arina gave them a carpet, which can be represented as an n⋅m
#  table of lowercase Latin letters.
#
# Vika hasn't seen the gift yet, but Tema knows what kind of carpets she likes. Vika will like the carpet if she can read her name on. She reads column by column from left to right and chooses one or zero letters from current column.
#
# Formally, the girl will like the carpet if it is possible to select four distinct columns in order from left to right such that the first column contains "v", the second one contains "i", the third one contains "k", and the fourth one contains "a".
#
# Help Tema understand in advance whether Vika will like Arina's gift.
#
# Input
# Each test consists of multiple test cases. The first line of input contains a single integer t
#  (1≤t≤100
# ) — the number of test cases. Then follows the description of the test cases.
#
# The first line of each test case contains two integers n
# , m
#  (1≤n,m≤20
# ) — the sizes of the carpet.
#
# The next n
#  lines contain m
#  lowercase Latin letters each, describing the given carpet.
#
# Output
# For each set of input data, output "YES" if Vika will like the carpet, otherwise output "NO".
#
# You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
#
# Example
# InputCopy
# 5
# 1 4
# vika
# 3 3
# bad
# car
# pet
# 4 4
# vvvv
# iiii
# kkkk
# aaaa
# 4 4
# vkak
# iiai
# avvk
# viaa
# 4 7
# vbickda
# vbickda
# vbickda
# vbickda
# OutputCopy
# YES
# NO
# YES
# NO
# YES
# Note
# In the first sample, Vika can read her name from left to right.
#
# In the second sample, Vika cannot read the character "v", so she will not like the carpet.
# Solution
# C++ O(NM) O(1) Greedy
#include <iostream>
#include <vector>
#include <string>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, m;
        std::scanf("%d %d", &n, &m);
        std::vector<std::string> grid;
        for (int j = 0; j < n; ++j) {
            std::string row;
            std::cin >> row;
            grid.push_back(row);
        }
        std::string name = "vika";
        int idx = 0;
        for (int c = 0; c < m; ++c) {
            for (int r = 0; r < n; ++r) {
                if (grid[r][c] == name[idx]) {
                    ++idx;
                    break;
                }
            }
            if (idx == 4) break;
        }
        std::cout << (idx == 4 ? "YES" : "NO") << "\n";
    }
}


int main() {
    solution();
}

# Python O(NM) O(1) Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        grid: list[str] = []
        for _ in range(n):
            row: str = sys.stdin.readline().rstrip()
            grid.append(row)
        name: str = 'vika'
        idx: int = 0
        for c in range(m):
            for r in range(n):
                if grid[r][c] == name[idx]:
                    idx += 1
                    break
            if idx == 4: break
        sys.stdout.write('{}\n'.format(['NO', 'YES'][idx == 4]))


if __name__ == '__main__':
    solution()