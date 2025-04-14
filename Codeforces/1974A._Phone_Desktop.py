# A. Phone Desktop
# time limit per test1 second
# memory limit per test256 megabytes
# Little Rosie has a phone with a desktop (or launcher, as it is also called). The desktop can consist of several screens. Each screen is represented as a grid of size 5×3
# , i.e., five rows and three columns.
#
# There are x
#  applications with an icon size of 1×1
#  cells; such an icon occupies only one cell of the screen. There are also y
#  applications with an icon size of 2×2
#  cells; such an icon occupies a square of 4
#  cells on the screen. Each cell of each screen can be occupied by no more than one icon.
#
# Rosie wants to place the application icons on the minimum number of screens. Help her find the minimum number of screens needed.
#
# Input
# The first line of the input contains t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first and only line of each test case contains two integers x
#  and y
#  (0≤x,y≤99
# ) — the number of applications with a 1×1
#  icon and the number of applications with a 2×2
#  icon, respectively.
#
# Output
# For each test case, output the minimal number of required screens on a separate line.
#
# Example
# InputCopy
# 11
# 1 1
# 7 2
# 12 4
# 0 3
# 1 0
# 8 1
# 0 0
# 2 0
# 15 0
# 8 2
# 0 9
# OutputCopy
# 1
# 1
# 2
# 2
# 1
# 1
# 0
# 1
# 1
# 2
# 5
# Note
# The solution for the first test case can look as follows:
#
# Blue squares represent empty spaces for icons, green squares represent 1×1
#  icons, red squares represent 2×2
#  icons
# The solution for the third test case can look as follows:
# Solution
# C++ O(1) O(1) Math Greedy
#include <iostream>
#include <cmath>

void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int x, y;
        std::cin >> x >> y;
        int screens = 0;
        int screensForY = (y + 1) / 2;
        screens = screensForY;
        int remainingCells;
        if (y % 2 == 1) remainingCells = 11;
        else remainingCells = 0;
        int totalRemainingCells = screensForY * 15 - y * 4;
        x = std::max(0, x - totalRemainingCells);
        if (x > 0) screens += (x + 14) / 15;
        std::cout << screens << std::endl;
    }
}

int main() {
    solution();
    return 0;
}

# Python O(1) O(1) Math Greedy
import sys

def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        screens_for_y: int = (y + 1) // 2
        screens: int = screens_for_y
        remaining_cells: int = 0
        if y & 1: remaining_cells = 11
        total_remaining_cells: int = screens_for_y * 15 - y * 4
        x = max(0, x - total_remaining_cells)
        if x > 0: screens += (x + 14) // 15
        sys.stdout.write('{}\n'.format(screens))


if __name__ == '__main__':
    solution()