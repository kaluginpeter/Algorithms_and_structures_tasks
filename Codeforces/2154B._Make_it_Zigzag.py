# B. Make it Zigzag
# time limit per test1.5 seconds
# memory limit per test256 megabytes
# An arbitrary array of integers b
#  of length m
#  is considered awesome if for all i
#  (1≤i<m
# ):
#
# if i
#  is odd then bi<bi+1
#  holds.
# if i
#  is even then bi>bi+1
#  holds.
# In other words, the following inequality is true: b1<b2>b3<b4…
#
# You are given an array of positive integers a
#  of length n
# . You may do either of the following operations any number of times, in any order:
#
# operation 1
# : select an integer i
#  (1≤i≤n
# ) and do: ai:=max(a1,…,ai)
# , that is, replace ai
#  with the prefix max up to i
# .
# operation 2
# : select an integer i
#  (1≤i≤n
# ) and then decrease ai
#  by 1
# .
# Determine the minimum number of times you need to do operation 2
#  to make a
#  awesome. Note that you do not need to minimise the number of times you perform operation 1
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains an integer n
#  (2≤n≤2⋅105
# ) — the length of the array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ).
#
# The sum of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each testcase, output the minimum cost to make a
#  awesome.
#
# Example
# InputCopy
# 7
# 5
# 1 4 2 5 3
# 4
# 3 3 2 1
# 5
# 6 6 6 6 6
# 7
# 1 2 3 4 5 6 7
# 3
# 3 2 1
# 2
# 1 2
# 9
# 65 85 19 53 21 79 92 29 96
# OutputCopy
# 0
# 1
# 3
# 6
# 1
# 0
# 13
# Note
# In the first test case, the array is already awesome so no operations need to be done.
#
# In the second test case, a
#  can be made awesome as follows:
#
# use operation 2
#  and decrease a1
#  by 1
# . [3,3,2,1]→[2,3,2,1]
# .
# use operation 1
#  and change a4
#  to max(2,3,2,1)=3
# . [2,3,2,1]→[2,3,2,3]
# .
# [2,3,2,3]
#  is awesome as 2<3>2<3
# . It can be proven that this is the minimum number of times operation 2
#  needs to be performed.
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <algorithm>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    int mx = 0;
    for (size_t i = 0; i < n; ++i) {
        std::cin >> nums[i];
        mx = std::max(mx, nums[i]);
        if (i & 1) nums[i] = mx;
    }
    int output = 0;
    for (int i = 1; i < n; i += 2) {
        bool left = !(nums[i - 1] < nums[i]);
        bool right = (i + 1 < n ? nums[i] <= nums[i + 1] : false);
        if (left) {
            int cost = nums[i - 1] - nums[i] + 1;
            output += cost;
        }
        if (right) {
            int cost = nums[i + 1] - nums[i] + 1;
            output += cost;
            nums[i + 1] -= cost;
        }
    }
    std::cout << output << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    mx: int = 0
    for i in range(n):
        mx = max(mx, nums[i])
        if i & 1: nums[i] = mx
    output: int = 0
    for i in range(1, n, 2):
        if not (nums[i] > nums[i - 1]):
            cost: int = nums[i - 1] - nums[i] + 1
            output += cost
        if i + 1 < n and not (nums[i] > nums[i + 1]):
            cost: int = nums[i + 1] - nums[i] + 1
            output += cost
            nums[i + 1] -= cost
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()