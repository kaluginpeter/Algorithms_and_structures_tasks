# B. No Casino in the Mountains
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an array a
#  of n
#  numbers and a number k
# . The value ai
#  describes the weather on the i
# -th day: if it rains on the i
# -th day, then ai=1
# ; otherwise, if the weather is good on the i
# -th day, then ai=0
# .
#
# Jean wants to visit as many peaks as possible. One hike to a peak takes exactly k
#  days, and during each of these days, the weather must be good (ai=0
# ). That is, formally, he can start a hike on day i
#  only if all aj=0
#  for all j
#  (i≤j≤i+k−1)
# .
#
# After each hike, before starting the next one, Jean must take a break of at least one day, meaning that on the day following a hike, he cannot go on another hike.
#
# Find the maximum number of peaks that Jean can visit.
#
# Input
# Each test consists of several test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤n≤105
# , 1≤k≤n
# ).
#
# The second line contains n
#  numbers ai
#  (ai∈{0,1}
# ), where ai
#  denotes the weather on the i
# -th day.
#
# It is guaranteed that the total value of n
#  across all test cases does not exceed 105
# .
#
# Output
# For each test case, output a single integer: the maximum number of hikes that Jean can make.
#
# Example
# InputCopy
# 5
# 5 1
# 0 1 0 0 0
# 7 3
# 0 0 0 0 0 0 0
# 3 1
# 1 1 1
# 4 2
# 0 1 0 1
# 6 2
# 0 0 1 0 0 0
# OutputCopy
# 3
# 2
# 0
# 0
# 2
# Note
# In the first sample:
#
# Day 1
#  — good weather, Jean goes on a hike. (a1=0
# )
# Day 2
#  — mandatory break.
# Day 3
#  — again good weather, Jean goes on the second hike. (a3=0
# )
# Day 4
#  — break.
# Day 5
#  — good weather, third hike. (a5=0
# )
# Thus, Jean can make 3 hikes, alternating each with a mandatory day of rest.
# In the second sample:
#
# From day 1
#  to day 3
#  — three days of good weather, Jean goes on a hike. (a1=a2=a3=0
# )
# Day 4
#  — mandatory break.
# From day 5
#  to day 7
#  — again three days of good weather, Jean goes on the second hike. (a5=a6=a7=0
# )
# In total, Jean makes 2 hikes.
# In the third sample:
#
# There are no days with good weather (ai=1
#  for all i
# )
# Jean cannot make any hikes. Answer: 0
# Solution
# C++ O(N) O(1) TwoPointers
#include <iostream>
#include <vector>


void solution() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    int output = 0, left = 0;
    bool isBreak = false;
    for (int right = 0; right < n; ++right) {
        if (isBreak) {
            isBreak = false;
            left = right + 1;
            continue;
        }
        if (!nums[right]) {
            if (right - left + 1 == k) {
                ++output;
                isBreak = true;
                left = right + 1;
            }
        }
        else left = right + 1;
    }
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) TwoPointers
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    output: int = 0
    left: int = 0
    is_break: bool = False
    for right in range(n):
        if is_break:
            left = right + 1
            is_break = False
            continue
        elif not nums[right]:
            if right - left + 1 == k:
                is_break = True
                left = right + 1
                output += 1
                continue
        else: left = right + 1
        is_break = False
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()