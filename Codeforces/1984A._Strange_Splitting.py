# A. Strange Splitting
# time limit per test1 second
# memory limit per test256 megabytes
# Define the range of a non-empty array to be the maximum value minus the minimum value. For example, the range of [1,4,2]
#  is 4−1=3
# .
#
# You are given an array a1,a2,…,an
#  of length n≥3
# . It is guaranteed a
#  is sorted.
#
# You have to color each element of a
#  red or blue so that:
#
# the range of the red elements does not equal the range of the blue elements, and
# there is at least one element of each color.
# If there does not exist any such coloring, you should report it. If there are multiple valid colorings, you can print any of them.
#
# Input
# The first line contains a single integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# The first line of each test case contains an integer n
#  (3≤n≤50
# ) — the length of the array.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ). It is guaranteed a1≤a2≤…≤an−1≤an
# .
#
# Output
# For each test case, if it is impossible to color a
#  to satisfy all the constraints, output NO
# .
#
# Otherwise, first output YES
# .
#
# Then, output a string s
#  of length n
# . For 1≤i≤n
# , if you color ai
#  red, si
#  should be R
# . For 1≤i≤n
# , if you color ai
#  blue, si
#  should be B
# .
#
# Example
# InputCopy
# 7
# 4
# 1 1 2 2
# 5
# 1 2 3 4 5
# 3
# 3 3 3
# 4
# 1 2 2 2
# 3
# 1 2 2
# 3
# 1 1 2
# 3
# 1 9 84
# OutputCopy
# YES
# RBRR
# YES
# BBRBB
# NO
# YES
# RBBR
# YES
# RRB
# YES
# BRR
# YES
# BRB
# Note
# In the first test case, given the array [1,1,2,2]
# , we can color the second element blue and the remaining elements red; then the range of the red elements [1,2,2]
#  is 2−1=1
# , and the range of the blue elements [1]
#  is 1−1=0
# .
#
# In the second test case, we can color the first, second, fourth and fifth elements [1,2,4,5]
#  blue and the remaining elements [3]
#  red.
#
# The range of the red elements is 3−3=0
#  and the range of the blue elements is 5−1=4
# , which are different.
#
# In the third test case, it can be shown there is no way to color a=[3,3,3]
#  to satisfy the constraints.
# Solution
# C++ O(N) O(1) String
#include <iostream>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    if (nums[0] == nums[n - 1]) {
        std::cout << "NO\n";
        return;
    }
    std::cout << "YES\n";
    if (nums[2] == nums[1]) std::cout << "BRB";
    else std::cout << "RBB";
    for (size_t i = 3; i < n; ++i) std::cout << "B";
    std::cout << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) String
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    if nums[0] == nums[-1]:
        sys.stdout.write('NO\n')
        return
    sys.stdout.write('YES\n')
    if nums[2] == nums[1]: sys.stdout.write('BRB')
    else: sys.stdout.write('RBB')
    sys.stdout.write('B' * (n - 3))
    sys.stdout.write('\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()