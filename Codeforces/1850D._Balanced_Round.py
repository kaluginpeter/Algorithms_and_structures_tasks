# D. Balanced Round
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are the author of a Codeforces round and have prepared n
#  problems you are going to set, problem i
#  having difficulty ai
# . You will do the following process:
#
# remove some (possibly zero) problems from the list;
# rearrange the remaining problems in any order you wish.
# A round is considered balanced if and only if the absolute difference between the difficulty of any two consecutive problems is at most k
#  (less or equal than k
# ).
#
# What is the minimum number of problems you have to remove so that an arrangement of problems is balanced?
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains two positive integers n
#  (1≤n≤2⋅105
# ) and k
#  (1≤k≤109
# ) — the number of problems, and the maximum allowed absolute difference between consecutive problems.
#
# The second line of each test case contains n
#  space-separated integers ai
#  (1≤ai≤109
# ) — the difficulty of each problem.
#
# Note that the sum of n
#  over all test cases doesn't exceed 2⋅105
# .
#
# Output
# For each test case, output a single integer — the minimum number of problems you have to remove so that an arrangement of problems is balanced.
#
# Example
# InputCopy
# 7
# 5 1
# 1 2 4 5 6
# 1 2
# 10
# 8 3
# 17 3 1 20 12 5 17 12
# 4 2
# 2 4 6 8
# 5 3
# 2 3 19 10 8
# 3 4
# 1 10 5
# 8 1
# 8 3 1 4 5 10 7 3
# OutputCopy
# 2
# 0
# 5
# 0
# 3
# 1
# 4
# Note
# For the first test case, we can remove the first 2
#  problems and construct a set using problems with the difficulties [4,5,6]
# , with difficulties between adjacent problems equal to |5−4|=1≤1
#  and |6−5|=1≤1
# .
#
# For the second test case, we can take the single problem and compose a round using the problem with difficulty 10
# .
# Solution
# C++ O(NlogN) O(1) Sorting Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, k;
        std::scanf("%d %d", &n, &k);
        std::vector<int> tasks;
        for (int j = 0; j < n; ++j) {
            int task;
            std::cin >> task;
            tasks.push_back(task);
        }
        std::sort(tasks.begin(), tasks.end());
        int max_segment = 1;
        int left = 0;
        for (int right = 1; right < n; ++right) {
            if (tasks[right] - tasks[right - 1] > k) {
                max_segment = std::max(max_segment, right - left);
                left = right;
            } else {
                max_segment = std::max(max_segment, right - left + 1);
            }
        }
        std::cout << n - max_segment << "\n";
    }
}

int main() {
    solution();
}

# Python O(NlogN) O(1) Sorting Greedy
from __future__ import annotations
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().rstrip().split())
        tasks: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
        max_segment: int = 1
        left: int = 0
        for right in range(1, n):
            if tasks[right] - tasks[right - 1] > k:
                max_segment = max(max_segment, right - left)
                left = right
            else:
                max_segment = max(max_segment, right - left + 1)
        sys.stdout.write(str(n - max_segment) + '\n')


if __name__ == '__main__':
    solution()
