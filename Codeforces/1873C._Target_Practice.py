# C. Target Practice
# time limit per test1 second
# memory limit per test256 megabytes
# A 10×10
#  target is made out of five "rings" as shown. Each ring has a different point value: the outermost ring — 1 point, the next ring — 2 points, ..., the center ring — 5 points.
#
#
# Vlad fired several arrows at the target. Help him determine how many points he got.
#
# Input
# The input consists of multiple test cases. The first line of the input contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case consists of 10 lines, each containing 10 characters. Each character in the grid is either X
#  (representing an arrow) or .
#  (representing no arrow).
#
# Output
# For each test case, output a single integer — the total number of points of the arrows.
#
# Example
# InputCopy
# 4
# X.........
# ..........
# .......X..
# .....X....
# ......X...
# ..........
# .........X
# ..X.......
# ..........
# .........X
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ....X.....
# ..........
# ..........
# ..........
# ..........
# ..........
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# OutputCopy
# 17
# 0
# 5
# 220
# Note
# In the first test case, there are three arrows on the outer ring worth 1 point each, two arrows on the ring worth 3 points each, and two arrows on the ring worth 4 points each. The total score is 3×1+2×3+2×4=17
# .
#
# In the second test case, there aren't any arrows, so the score is 0
# .
# Solution
# Python O(NM) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        score: int = 0
        for m in range(10):
            row: str = sys.stdin.readline().rstrip()
            for n in range(10):
                if row[n] == 'X':
                    score += min((10 - n - 1 if n >= 5 else n) + 1, (10 - m - 1 if m >= 5 else m) + 1)
        sys.stdout.write(str(score) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(NM) O(1) Math
#include <iostream>
#include <string>


void solution(int& t) {
    for (int i = 0; i < t; ++i) {
        int score = 0;
        for (int j = 0; j < 10; ++j) {
            std::string row;
            std::cin >> row;
            for (int k = 0; k < 10; ++k) {
                if (row[k] == 'X') {
                    score += std::min((j >= 5? 10 - j - 1 : j) + 1, (k >= 5? 10 - k - 1 : k) + 1);
                }
            }
        }
        std::cout << score << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}