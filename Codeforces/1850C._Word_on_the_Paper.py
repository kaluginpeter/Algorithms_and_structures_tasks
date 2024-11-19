# C. Word on the Paper
# time limit per test1 second
# memory limit per test256 megabytes
# On an 8×8
#  grid of dots, a word consisting of lowercase Latin letters is written vertically in one column, from top to bottom. What is it?
#
# Input
# The input consists of multiple test cases. The first line of the input contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case consists of 8
#  lines, each containing 8
#  characters. Each character in the grid is either .
#  (representing a dot) or a lowercase Latin letter (a
# –z
# ).
#
# The word lies entirely in a single column and is continuous from the beginning to the ending (without gaps). See the sample input for better understanding.
#
# Output
# For each test case, output a single line containing the word made up of lowercase Latin letters (a
# –z
# ) that is written vertically in one column from top to bottom.
#
# Example
# InputCopy
# 5
# ........
# ........
# ........
# ........
# ...i....
# ........
# ........
# ........
# ........
# .l......
# .o......
# .s......
# .t......
# ........
# ........
# ........
# ........
# ........
# ........
# ........
# ......t.
# ......h.
# ......e.
# ........
# ........
# ........
# ........
# ........
# .......g
# .......a
# .......m
# .......e
# a.......
# a.......
# a.......
# a.......
# a.......
# a.......
# a.......
# a.......
# OutputCopy
# i
# lost
# the
# game
# aaaaaaaa
# Solution
# C++ O(NM) O(1) Simulation Matrix
#include <iostream>
#include <vector>
#include <string>

void printMatrix(std::vector<std::string>& matrix) {
    for (int row = 0; row < 8; ++row) {
        for (int col = 0; col < 8; ++col) {
            if (matrix[row][col] != '.') {
                while (row < 8 && matrix[row][col] != '.') {
                    std::cout << matrix[row][col];
                    ++row;
                }
                std::cout << "\n";
                return;
            }
        }
    }
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::vector<std::string> matrix;
        for (int r = 0; r < 8; ++r) {
            std::string row;
            std::cin >> row;
            matrix.push_back(row);
        }
        printMatrix(matrix);
    }
}

# Python O(NM) O(1) Simulation Matrix
import sys

def print_matrix(matrix: list) -> None:
    for row in range(8):
        for col in range(8):
            if matrix[row][col] != '.':
                while row < 8 and matrix[row][col] != '.':
                    sys.stdout.write(matrix[row][col])
                    row += 1
                sys.stdout.write('\n')
                return

def solution(t: int) -> None:
    for _ in range(t):
        matrix: list = []
        for r in range(8):
            row: str = sys.stdin.readline().rstrip()
            matrix.append(row)
        print_matrix(matrix)


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)