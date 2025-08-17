# A. Max Plus Size
# time limit per test1 second
# memory limit per test256 megabytes
# EnV - Dynasty
# ⠀
# You are given an array a1,a2,…,an
#  of positive integers.
#
# You can color some elements of the array red, but there cannot be two adjacent red elements (i.e., for 1≤i≤n−1
# , at least one of ai
#  and ai+1
#  must not be red).
#
# Your score is the maximum value of a red element plus the number of red elements. Find the maximum score you can get.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤100
# ) — the length of the array.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤1000
# ) — the given array.
#
# Output
# For each test case, output a single integer: the maximum possible score you can get after coloring some elements red according to the statement.
#
# Example
# InputCopy
# 4
# 3
# 5 4 5
# 3
# 4 5 4
# 10
# 3 3 3 3 4 1 2 3 4 5
# 9
# 17 89 92 42 29 92 14 70 45
# OutputCopy
# 7
# 6
# 10
# 97
# Note
# In the first test case, you can color the array as follows: [5,4,5]
# . Your score is max([5,5])+size([5,5])=5+2=7
# . This is the maximum score you can get.
#
# In the second test case, you can color the array as follows: [4,5,4]
# . Your score is max([4,4])+size([4,4])=4+2=6
# . This is the maximum score you can get.
#
# In the third test case, you can color the array as follows: [3,3,3,3,4,1,2,3,4,5]
# . Your score is max([3,3,4,3,5])+size([3,3,4,3,5])=5+5=10
# . This is the maximum score you can get.
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <vector>
#include <cstdint>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    int maxEven = 0, maxOdd = 0;
    for (int i = 0; i < n; ++i) {
        if (i + 1 & 1) maxOdd = std::max(maxOdd, nums[i]);
        else maxEven = std::max(maxEven, nums[i]);
    }
    int first = maxEven + n / 2, second = maxOdd + (n + 1) / 2;
    std::cout << std::max(first, second) << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    max_even: int = 0
    max_odd: int = 0
    for i in range(n):
        if i + 1 & 1: max_odd = max(max_odd, nums[i])
        else: max_even = max(max_even, nums[i])
    first: int = max_even + n // 2
    second: int = max_odd + (n + 1) // 2
    sys.stdout.write('{}\n'.format(max(first, second)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()