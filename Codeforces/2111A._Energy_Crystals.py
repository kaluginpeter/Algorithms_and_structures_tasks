# A. Energy Crystals
# time limit per test2 seconds
# memory limit per test512 megabytes
# There are three energy crystals numbered 1
# , 2
# , and 3
# ; let's denote the energy level of the i
# -th crystal as ai
# . Initially, all of them are discharged, meaning their energy levels are equal to 0
# . Each crystal needs to be charged to level x
#  (exactly x
# , not greater).
#
# In one action, you can increase the energy level of any one crystal by any positive amount; however, the energy crystals are synchronized with each other, so an action can only be performed if the following condition is met afterward:
#
# for each pair of crystals i
# , j
# , it must hold that ai≥⌊aj2⌋
# .
# What is the minimum number of actions required to charge all the crystals?
#
# Input
# Each test consists of several test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The only line of each test case contains a single integer x
#  (1≤x≤109
# ).
#
# Output
# For each test case, output a single integer — the minimum number of actions required to charge all energy crystals to level x
# .
#
# Example
# InputCopy
# 7
# 1
# 5
# 14
# 2025
# 31415
# 536870910
# 1000000000
# OutputCopy
# 3
# 7
# 9
# 23
# 31
# 59
# 61
# Note
# In the first test case, one possible sequence of actions is:
#
# [0,0,0]→[1,0,0]→[1,0,1]→[1,1,1]
#
# One of the possible sequences of actions in the second test case is:
#
# [0,0,0]→[1,0,0]→[1,1,0]→[1,1,2]→[3,1,2]→[3,5,2]→[5,5,2]→[5,5,5]
# Solution
# C++ O(log(N)) O(1) Math Greedy
#include <iostream>
#include <algorithm>
#include <vector>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int x;
        std::cin >> x;
        std::vector<int> nums = {0, 0, 0};
        int ops = 0;
        while (nums[0] != x) {
            nums[0] = std::min(nums[1] * 2 + 1, x);
            std::sort(nums.begin(), nums.end());
            ++ops;
        }
        std::cout << ops << "\n";
    }
}


int main() {
    solution();
}

# Python O(log(N)) O(1) Math Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        x: int = int(sys.stdin.readline().rstrip())
        nums: list[int] = [0, 0, 0]
        ops: int = 0
        while nums[0] != x:
            ops += 1
            nums[0] = min(x, nums[1] * 2 + 1)
            nums.sort()
        sys.stdout.write('{}\n'.format(ops))


if __name__ == '__main__':
    solution()