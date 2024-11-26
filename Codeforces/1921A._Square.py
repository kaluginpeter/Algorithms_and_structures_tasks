# A. Square
# time limit per test1 second
# memory limit per test256 megabytes
# A square of positive (strictly greater than 0
# ) area is located on the coordinate plane, with sides parallel to the coordinate axes. You are given the coordinates of its corners, in random order. Your task is to find the area of the square.
#
# Input
# Each test consists of several testcases. The first line contains one integer t
#  (1≤t≤100
# ) — the number of testcases. The following is a description of the testcases.
#
# Each testcase contains four lines, each line contains two integers xi,yi
#  (−1000≤xi,yi≤1000
# ), coordinates of the corners of the square.
#
# It is guaranteed that there is a square with sides parallel to the coordinate axes, with positive (strictly greater than 0
# ) area, with corners in given points.
#
# Output
# For each test case, print a single integer, the area of the square.
#
# Example
# InputCopy
# 3
# 1 2
# 4 5
# 1 5
# 4 2
# -1 1
# 1 -1
# 1 1
# -1 -1
# 45 11
# 45 39
# 17 11
# 17 39
# OutputCopy
# 9
# 4
# 784
# Solution
# C++ O(NlogN) O(N) Math
#include <iostream>
#include <vector>
#include <algorithm>

void solution(int t) {
    for (int i = 0; i < t; ++i) {
        std::vector<std::pair<int, int>> plane;
        for (int j = 0; j < 4; ++j) {
            int x, y;
            std::cin >> x >> y;
            plane.push_back({x, y});
        }
        std::sort(plane.begin(), plane.end());
        std::cout << (plane[1].second - plane[0].second) * (plane[3].first - plane[1].first) << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(NlogN) O(N) Math
import sys

def solution(t: int) -> None:
    for _ in range(t):
        plane: list[list[int]] = []
        for i in range(4):
            x, y = map(int, sys.stdin.readline().rstrip().split())
            plane.append([x, y])
        plane.sort()
        sys.stdout.write(str((plane[1][1] - plane[0][1]) * (plane[3][0] - plane[1][0])) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
