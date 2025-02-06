# A. Rook
# time limit per test1 second
# memory limit per test256 megabytes
# As you probably know, chess is a game that is played on a board with 64 squares arranged in an 8×8
#  grid. Columns of this board are labeled with letters from a to h, and rows are labeled with digits from 1 to 8. Each square is described by the row and column it belongs to.
#
#
# The rook is a piece in the game of chess. During its turn, it may move any non-zero number of squares horizontally or vertically. Your task is to find all possible moves for a rook on an empty chessboard.
#
# Input
# The first line of input contains single integer t
#  (1≤t≤64
# ) — the number of test cases. The descriptions of test cases follow.
#
# Each test case contains one string of two characters, description of the square where rook is positioned. The first character is a letter from a to h, the label of column, and the second character is a digit from 1 to 8, the label of row.
#
# The same position may occur in more than one test case.
#
# Output
# For each test case, output descriptions of all squares where the rook can move, in the same format as in the input.
#
# You can output squares in any order per test case.
#
# Example
# InputCopy
# 1
# d5
# OutputCopy
# d1
# d2
# b5
# g5
# h5
# d3
# e5
# f5
# d8
# a5
# d6
# d7
# c5
# d4
# Solution
# C++ O(1) O(1) Simulation
#include <bits/stdc++.h>


void solution() {
    std::string moves = "abcdefgh";
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string pos;
        std::cin >> pos;
        for (int d = 1; d <= 8; ++d) {
            if ((pos[1] - '0') == d) continue;
            std::cout << pos[0] << d << "\n";
        }
        for (char& ch : moves) {
            if (ch == pos[0]) continue;
            std::cout << ch << pos[1] << "\n";
        }
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Simulation
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        pos: str = sys.stdin.readline().rstrip()
        for d in range(1, 9):
            if d == int(pos[1]): continue
            sys.stdout.write(f'{pos[0]}{d}\n')
        for ch in 'abcdefgh':
            if ch == pos[0]: continue
            sys.stdout.write(f'{ch}{pos[1]}\n')


if __name__ == '__main__':
    solution()