# B. Blank Space
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a binary array a
#  of n
#  elements, a binary array is an array consisting only of 0
# s and 1
# s.
#
# A blank space is a segment of consecutive elements consisting of only 0
# s.
#
# Your task is to find the length of the longest blank space.
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤100
# ) — the length of the array.
#
# The second line of each test case contains n
#  space-separated integers ai
#  (0≤ai≤1
# ) — the elements of the array.
#
# Output
# For each test case, output a single integer — the length of the longest blank space.
#
# Example
# InputCopy
# 5
# 5
# 1 0 0 1 0
# 4
# 0 1 1 1
# 1
# 0
# 3
# 1 1 1
# 9
# 1 0 0 0 1 0 0 0 1
# OutputCopy
# 2
# 1
# 1
# 0
# 3
# Solution
# C++ O(N) O(1) Two Pointers
#include <iostream>
#include <vector>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::vector<int> nums;
        for (int j = 0; j < n; ++j) {
            int num;
            std::cin >> num;
            nums.push_back(num);
        }
        int output = 0;
        int left = 0;
        for (int right = left; right < nums.size(); ++right) {
            if (nums[right]) {
                left = right + 1;
            }
            output = std::max(output, right - left + 1);
        }
        std::cout << output << std::endl;
    }
}

# Python O(N) O(1) Two Pointers
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
        output: int = 0
        left: int = 0
        for right in range(left, n):
            if nums[right]:
                left = right + 1
            output = max(output, right - left + 1)
        sys.stdout.write(str(output) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
