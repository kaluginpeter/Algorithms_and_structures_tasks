# B. Following Directions
# time limit per test1 second
# memory limit per test256 megabytes
# Alperen is standing at the point (0,0)
# . He is given a string s
#  of length n
#  and performs n
#  moves. The i
# -th move is as follows:
#
# if si=L
# , then move one unit left;
# if si=R
# , then move one unit right;
# if si=U
# , then move one unit up;
# if si=D
# , then move one unit down.
# If Alperen starts at the center point, he can make the four moves shown.
# There is a candy at (1,1)
#  (that is, one unit above and one unit to the right of Alperen's starting point). You need to determine if Alperen ever passes the candy.
# Alperen's path in the first test case.
# Input
# The first line of the input contains an integer t
#  (1≤t≤1000
# ) — the number of testcases.
#
# The first line of each test case contains an integer n
#  (1≤n≤50
# ) — the length of the string.
#
# The second line of each test case contains a string s
#  of length n
#  consisting of characters L
# , R
# , D
# , and U
# , denoting the moves Alperen makes.
#
# Output
# For each test case, output "YES" (without quotes) if Alperen passes the candy, and "NO" (without quotes) otherwise.
#
# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
#
# Example
# InputCopy
# 7
# 7
# UUURDDL
# 2
# UR
# 8
# RRRUUDDD
# 3
# LLL
# 4
# DUUR
# 5
# RUDLL
# 11
# LLLLDDRUDRD
# OutputCopy
# YES
# YES
# NO
# NO
# YES
# YES
# NO
# Note
# In the first test case, Alperen follows the path
# (0,0)→U(0,1)→U(0,2)→U(0,3)→R(1,3)→D(1,2)→D(1,1)→L(0,1).
# Note that Alperen doesn't need to end at the candy's location of (1,1)
# , he just needs to pass it at some point.
#
# In the second test case, Alperen follows the path
# (0,0)→U(0,1)→R(1,1).
# In the third test case, Alperen follows the path
# (0,0)→R(1,0)→R(2,0)→R(3,0)→U(3,1)→U(3,2)→D(3,1)→D(3,0)→D(3,−1).
# In the fourth test case, Alperen follows the path
# (0,0)→L(−1,0)→L(−2,0)→L(−3,0).
# Solution
# C++ O(N) O(1) Simulation
#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::string moves;
        std::cin >> moves;
        bool isValid = false;
        int row = 0, col = 0;
        for (char move : moves) {
            if (move == 'L') {
                --row;
            } else if (move == 'R') {
                ++row;
            } else if (move == 'U') {
                ++col;
            } else {
                --col;
            }
            if (row == 1 && col == 1) {
                isValid = true;
                break;
            }
        }
        std::cout << (isValid? "YES" : "NO") << "\n";
    }
}

# Python O(N) O(1) Simulation
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        moves: str = sys.stdin.readline().rstrip()
        is_valid: bool = False
        row = col = 0
        for move in moves:
            if move == 'L':
                row -= 1
            elif move == 'R':
                row += 1
            elif move == 'U':
                col += 1
            else:
                col -= 1
            if row == col == 1:
                is_valid = True
                break;
        sys.stdout.write('YES' if is_valid else 'NO')
        sys.stdout.write('\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)