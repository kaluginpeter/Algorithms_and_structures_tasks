# B. Not Quite Latin Square
# time limit per test1 second
# memory limit per test256 megabytes
# A Latin square is a 3×3
#  grid made up of the letters A
# , B
# , and C
#  such that:
#
# in each row, the letters A
# , B
# , and C
#  each appear once, and
# in each column, the letters A
# , B
# , and C
#  each appear once.
# For example, one possible Latin square is shown below.
# ⎡⎣⎢ACBBACCBA⎤⎦⎥
# You are given a Latin square, but one of the letters was replaced with a question mark ?
# . Find the letter that was replaced.
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤108
# ) — the number of testcases.
#
# Each test case contains three lines, each consisting of three characters, representing the Latin square. Each character is one of A
# , B
# , C
# , or ?
# .
#
# Each test case is a Latin square with exactly one of the letters replaced with a question mark ?
# .
#
# Output
# For each test case, output the letter that was replaced.
#
# Example
# InputCopy
# 3
# ABC
# C?B
# BCA
# BCA
# CA?
# ABC
# ?AB
# BCA
# ABC
# OutputCopy
# A
# B
# C
# Note
# The correct Latin squares for the three test cases are shown below:
#
# ⎡⎣⎢ACBBACCBA⎤⎦⎥⎡⎣⎢BCACABABC⎤⎦⎥⎡⎣⎢CBAACBBAC⎤⎦⎥
# Solution
# C++ O(N) O(1) Matrix
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

void solution(int t) {
    for (int i = 0; i < t; ++i) {
        for (int j = 0; j < 3; ++j) {
            std::string row;
            std::cin >> row;
            if (row.find('?') != std::string::npos) {
                std::vector<char> letters = {'A', 'B', 'C'};
                for (char l : row) {
                    auto it = std::find(letters.begin(), letters.end(), l);
                    if (it != letters.end()) {
                        letters.erase(it);
                    }
                }
                std::cout << letters[0] << "\n";
            }

        }
    }
}

int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(N) O(1) Matrix
import sys


def solution(t: int) -> None:
    for _ in range(t):
        for i in range(3):
            row: str = sys.stdin.readline().rstrip()
            if '?' in row:
                letters: list = ['A', 'B', 'C']
                for l in row:
                    if l in letters:
                        letters.remove(l)
                sys.stdout.write(letters[0] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
