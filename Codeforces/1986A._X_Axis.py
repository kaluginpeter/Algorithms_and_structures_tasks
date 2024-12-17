# A. X Axis
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given three points with integer coordinates x1
# , x2
# , and x3
#  on the X
#  axis (1≤xi≤10
# ). You can choose any point with an integer coordinate a
#  on the X
#  axis. Note that the point a
#  may coincide with x1
# , x2
# , or x3
# . Let f(a)
#  be the total distance from the given points to the point a
# . Find the smallest value of f(a)
# .
#
# The distance between points a
#  and b
#  is equal to |a−b|
# . For example, the distance between points a=5
#  and b=2
#  is 3
# .
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤103
# ) — the number of test cases. Then follows their descriptions.
#
# The single line of each test case contains three integers x1
# , x2
# , and x3
#  (1≤xi≤10
# ) — the coordinates of the points.
#
# Output
# For each test case, output the smallest value of f(a)
# .
#
# Example
# InputCopy
# 8
# 1 1 1
# 1 5 9
# 8 2 8
# 10 9 3
# 2 1 1
# 2 4 1
# 7 3 5
# 1 9 4
# OutputCopy
# 0
# 8
# 6
# 7
# 1
# 3
# 4
# 8
# Note
# In the first test case, the smallest value of f(a)
#  is achieved when a=1
# : f(1)=|1−1|+|1−1|+|1−1|=0
# .
#
# In the second test case, the smallest value of f(a)
#  is achieved when a=5
# : f(5)=|1−5|+|5−5|+|9−5|=8
# .
#
# In the third test case, the smallest value of f(a)
#  is achieved when a=8
# : f(8)=|8−8|+|2−8|+|8−8|=6
# .
#
# In the fourth test case, the smallest value of f(a)
#  is achieved when a=9
# : f(10)=|10−9|+|9−9|+|3−9|=7
# .
# Solution
# C++ O(1) O(1) Brute Force Math
#include <iostream>


void solution(int& t) {
    for (int i = 0; i < t; ++i) {
        int x, y, z;
        std::cin >> x >> y >> z;
        int minDiff = 10;
        for (int a = 1; a <= 10; ++a) {
            minDiff = std::min(minDiff, std::abs(x - a) + std::abs(y - a) + std::abs(z - a));
        }
        std::cout << minDiff << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(1) O(1) Brute Force Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        x, y, z = map(int, sys.stdin.readline().rstrip().split())
        min_diff: int = 10
        for a in range(1, 11):
            min_diff = min(min_diff, abs(x - a) + abs(y - a) + abs(z - a))
        sys.stdout.write(str(min_diff) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
