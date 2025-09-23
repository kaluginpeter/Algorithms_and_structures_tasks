# B. Cake Collection
# time limit per test1 second
# memory limit per test512 megabytes
#
# Maple wants to bake some cakes for Chocola and Vanilla.
#
# One day, she discovers n
#  magical cake ovens. The i
# -th oven bakes ai
#  cakes every second. The cakes remain in their respective ovens until they are collected.
#
# At the end of each second, she may teleport to any oven (including the one she is currently at) and collect all the cakes that have accumulated in that oven up to that point.
#
# Your task is to determine the maximum number of cakes Maple can collect in m
#  seconds.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and m
#  (1≤n≤105
# , 1≤m≤108
# ) — the number of magical ovens and the number of seconds during which Maple will collect cakes.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤105
# ) — the number of cakes the i
# -th oven bakes every second.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output a single integer representing the maximum number of cakes Maple can collect in m
#  seconds.
#
# Example
# InputCopy
# 3
# 3 4
# 1 2 3
# 3 2
# 1 2 3
# 1 1000
# 100000
# OutputCopy
# 20
# 8
# 100000000
# Note
# For the first test case, one optimal solution is as follows:
#
# At the end of the first second, the ovens contain 1
# , 2
# , and 3
#  cakes respectively. Maple teleports to oven 3
#  and collects all 3
#  cakes. Oven 3
#  now has 0
#  cakes remaining.
# At the end of the second second, the ovens contain 2
# , 4
# , and 3
#  cakes respectively. Maple teleports to oven 1
#  and collects all 2
#  cakes. Oven 1
#  now has 0
#  cakes remaining.
# At the end of the third second, the ovens contain 1
# , 6
# , and 6
#  cakes respectively. Maple teleports to oven 2
#  and collects all 6
#  cakes. Oven 2
#  now has 0
#  cakes remaining.
# At the end of the fourth second, the ovens contain 2
# , 2
# , and 9
#  cakes respectively. Maple teleports to oven 3
#  and collects all 9
#  cakes. Oven 3
#  now has 0
#  cakes remaining.
# In total, Maple collects 3+2+6+9=20
#  cakes.
#
# For the second test case, one optimal solution is as follows:
#
# At the end of the first second, the ovens contain 1
# , 2
# , and 3
#  cakes respectively. Maple teleports to oven 2
#  and collects all 2
#  cakes. Oven 2
#  now has 0
#  cakes remaining.
# At the end of the second second, the ovens contain 2
# , 2
# , and 6
#  cakes respectively. Maple teleports to oven 3
#  and collects all 6
#  cakes. Oven 3
#  now has 0
#  cakes remaining.
# In total, Maple collects 2+6=8
#  cakes.
# Solution
# C++ O(NlogN + N) O(1) Greedy Math
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n, m;
    std::cin >> n >> m;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    long long output = 0;
    int seconds = 0;
    if (m > n) {
        output += static_cast<long long>(nums[0]) * (m - n);
        seconds += m - n;
        m = n;
    }
    bool isFirst = true;
    for (size_t i = n - m; i < n; ++i) {
        ++seconds;
        output += static_cast<long long>(nums[i]) * (isFirst ? 1 : seconds);
        isFirst = false;
    }
    std::cout << output << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN + N) O(1) Greedy Math
import sys


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    output: int = 0
    seconds: int = 0
    if m > n:
        output += nums[0] * (m - n)
        seconds += m - n
        m = n
    is_first: bool = True
    for i in range(n - m, n):
        seconds += 1
        output += nums[i] * [seconds, 1][is_first]
        is_first = False
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()