# B. Vlad and Shapes
# time limit per test1 second
# memory limit per test256 megabytes
# Vladislav has a binary square grid of n×n
#  cells. A triangle or a square is drawn on the grid with symbols 1
# . As he is too busy being cool, he asks you to tell him which shape is drawn on the grid.
#
# A triangle is a shape consisting of k
#  (k>1
# ) consecutive rows, where the i
# -th row has 2⋅i−1
#  consecutive characters 1
# , and the central 1s are located in one column. An upside down triangle is also considered a valid triangle (but not rotated by 90 degrees).
# Two left pictures contain examples of triangles: k=4
# , k=3
# . The two right pictures don't contain triangles.
# A square is a shape consisting of k
#  (k>1
# ) consecutive rows, where the i
# -th row has k
#  consecutive characters 1
# , which are positioned at an equal distance from the left edge of the grid.
# Examples of two squares: k=2
# , k=4
# .
# For the given grid, determine the type of shape that is drawn on it.
#
# Input
# The first line contains a single integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (2≤n≤10
# ) — the size of the grid.
#
# The next n
#  lines each contain n
#  characters 0
#  or 1
# .
#
# The grid contains exactly one triangle or exactly one square that contains all the 1
# s in the grid. It is guaranteed that the size of the triangle or square is greater than 1
#  (i.e., the shape cannot consist of exactly one 1).
#
# Output
# For each test case, output "SQUARE" if all the 1
# s in the grid form a square, and "TRIANGLE" otherwise (without quotes).
#
# Example
# InputCopy
# 6
# 3
# 000
# 011
# 011
# 4
# 0000
# 0000
# 0100
# 1110
# 2
# 11
# 11
# 5
# 00111
# 00010
# 00000
# 00000
# 00000
# 10
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 1111111110
# 0111111100
# 0011111000
# 0001110000
# 0000100000
# 3
# 111
# 111
# 111
# OutputCopy
# SQUARE
# TRIANGLE
# SQUARE
# TRIANGLE
# TRIANGLE
# SQUARE
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <vector>
#include <string>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::vector<std::string> grid;
        for (int j = 0; j < n; ++j) {
            std::string row;
            std::cin >> row;
            grid.push_back(row);
        }
        bool isSquare = false;
        for (int r = 0; r < n; ++r) {
            bool isBreak = false;
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == '1') {
                    int width = r;
                    int length = c;
                    while (width < n && grid[width][c] == '1') ++width;
                    while (length < n && grid[r][length] == '1') ++length;
                    if (width - r == length - c) isSquare = true;
                    isBreak = true;
                    break;
                }
            }
            if (isBreak) break;
        }
        std::cout << (isSquare ? "SQUARE" : "TRIANGLE") << "\n";
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
        grid: list[str] = []
        for _ in range(n):
            row: str = sys.stdin.readline().rstrip()
            grid.append(row)
        is_square: bool = False
        for r in range(n):
            is_break: bool = False
            for c in range(n):
                if grid[r][c] == '1':
                    is_break = True
                    width: int = r
                    while width < n and grid[width][c] == '1': width += 1
                    length: int = c
                    while length < n and grid[r][length] == '1': length += 1
                    if width - r == length - c: is_square = True
                    break
            if is_break: break
        sys.stdout.write('{}\n'.format(['TRIANGLE', 'SQUARE'][is_square]))


if __name__ == '__main__':
    solution()