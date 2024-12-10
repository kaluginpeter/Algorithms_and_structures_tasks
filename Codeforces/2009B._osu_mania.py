# B. osu!mania
# time limit per test1 second
# memory limit per test256 megabytes
# You are playing your favorite rhythm game, osu!mania. The layout of your beatmap consists of n
#  rows and 4
#  columns. Because notes at the bottom are closer, you will process the bottommost row first and the topmost row last. Each row will contain exactly one note, represented as a '#'.
#
# For each note 1,2,…,n
# , in the order of processing, output the column in which the note appears.
#
# Input
# The first line contains t
#  (1≤t≤100
# ) — the number of test cases.
#
# For each test case, the first line contains n
#  (1≤n≤500
# ) — the number of rows of the beatmap.
#
# The following n
#  lines contain 4
#  characters. The i
# -th line represents the i
# -th row of the beatmap from the top. It is guaranteed that the characters are either '.' or '#', and exactly one of the characters is '#'.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 500
# .
#
# Output
# For each test case, output n
#  integers on a new line, the column that the i
# -th note appears in for all i
#  from 1
#  to n
# .
#
# Example
# InputCopy
# 3
# 4
# #...
# .#..
# ..#.
# ...#
# 2
# .#..
# .#..
# 1
# ...#
# OutputCopy
# 4 3 2 1
# 2 2
# 4
# Solution
# C++ O(N) O(N) Simulation
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


void solution(int& t) {
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::vector<int> positions;
        for (int j = 0; j < n; ++j) {
            std::string row;
            std::cin >> row;
            for (int idx = 0; idx < 4; ++idx) {
                if (row[idx] == '#') {
                    positions.push_back(idx + 1);
                    break;
                }
            }
        }
        std::reverse(positions.begin(), positions.end());
        for (int idx = 0; idx < n; ++idx) {
            if (idx) {
                std::cout << " ";
            }
            std::cout << positions[idx];
        }
        std::cout << "\n";

    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(N) O(N) Simulation
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        positions: list = []
        for _ in range(n):
            row: str = sys.stdin.readline().rstrip()
            for idx in range(4):
                if row[idx] == '#':
                    positions.append(idx + 1)
                    break
        positions.reverse()
        for idx in range(n):
            if idx:
                sys.stdout.write(' ')
            sys.stdout.write(str(positions[idx]))
        sys.stdout.write('\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
