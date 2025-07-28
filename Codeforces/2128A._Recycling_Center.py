# A. Recycling Center
# time limit per test1 second
# memory limit per test256 megabytes
# In the recycling center, there are n
#  trash bags, the i
# -th bag has a weight of ai
# . At each second, two actions will happen successively:
#
# First, you must choose a trash bag and destroy it. It will cost 1
#  coin if the weight of the trash bag is strictly greater than c
# , and it will cost 0
#  coins otherwise.
# Then, the weight of each remaining trash bag will get multiplied by two.
# What is the minimum number of coins you have to spend to get rid of all trash bags?
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and c
#  (1≤n≤30
# , 1≤c≤109)
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the weight of each trash bag.
#
# Output
# For each test case, you must output a single integer — the minimum number of coins you have to spend to destroy all trash bags.
#
# Example
# InputCopy
# 4
# 5 10
# 10 4 15 1 8
# 3 42
# 1000000000 1000000000 1000000000
# 10 30
# 29 25 2 12 15 42 14 6 16 9
# 10 1000000
# 1 1 1 1 1 1 1 1 1 864026633
# OutputCopy
# 2
# 3
# 6
# 1
# Note
# In the following explanation:
#
# Numbers in blue represent trash bags that have been destroyed for free,
# Numbers in red represent trash bags that have been destroyed for 1
#  coin,
# Numbers in black represent trash bags that have not been destroyed yet.
# In the first test case, one solution is:
#
# [10,4,15,1,8]
# [10,8,30,2,16]
# , 10
#  is destroyed for free because 10≤10
# .
# [10,8,60,4,32]
# , 8
#  is destroyed for free because 8≤10
# .
# [10,8,120,8,32]
# , 32
#  is destroyed for 1
#  coin because 32>10
# .
# [10,8,240,8,32]
# , 8
#  is destroyed for free because 8≤10
# .
# [10,8,240,8,32]
# , 240
#  is destroyed for 1
#  coin because 240>10
# .
# In total, you paid 2
#  coins, and we can prove it is optimal.
#
# In the second test case, one solution is:
#
# [1000000000,1000000000,1000000000]
# [1000000000,2000000000,2000000000]
# , 1000000000
#  is destroyed for 1
#  coin because 1000000000>42
# .
# [1000000000,2000000000,4000000000]
# , 2000000000
#  is destroyed for 1
#  coin because 2000000000>42
# .
# [1000000000,2000000000,4000000000]
# , 4000000000
#  is destroyed for 1
#  coin because 4000000000>42
# .
# Solution
# C++ O(NlogN) O(1) Sorting BinarySearch Greedy
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>


void solution() {
    int n, c;
    std::cin >> n >> c;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    int left = 0, right = n - 1;
    int start = -1;
    while (left <= right) {
        int middle = left + ((right - left) >> 1);
        if (nums[middle] <= c) {
            start = middle;
            left = middle + 1;
        } else right = middle - 1;
    }
    int p = 0, extra = 0;
    for (int i = start; i >= 0; --i) {
        if (static_cast<long long>(nums[i]) * std::pow(2.0, p) <= c) {
            ++extra;
            ++p;
        }
    }
    std::cout << (n - extra) << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN) O(1) Sorting Greedy BinarySearch
import sys


def solution() -> None:
    n, c = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    left: int = 0
    right: int = n - 1
    start: int = -1
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if nums[middle] <= c:
            start = middle
            left = middle + 1
        else: right = middle - 1
    extra: int = 0
    p: int = 0
    for i in range(start, -1, -1):
        if nums[i] * pow(2, p) <= c:
            p += 1
            extra += 1
    sys.stdout.write('{}\n'.format(n - extra))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()