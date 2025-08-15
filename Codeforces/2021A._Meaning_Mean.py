# A. Meaning Mean
# time limit per test1 second
# memory limit per test256 megabytes
# Pak Chanek has an array a
#  of n
#  positive integers. Since he is currently learning how to calculate the floored average of two numbers, he wants to practice it on his array a
# .
#
# While the array a
#  has at least two elements, Pak Chanek will perform the following three-step operation:
#
# Pick two different indices i
#  and j
#  (1≤i,j≤|a|
# ; i≠j
# ), note that |a|
#  denotes the current size of the array a
# .
# Append ⌊ai+aj2⌋
# ∗
#  to the end of the array.
# Remove elements ai
#  and aj
#  from the array and concatenate the remaining parts of the array.
# For example, suppose that a=[5,4,3,2,1,1]
# . If we choose i=1
#  and j=5
# , the resulting array will be a=[4,3,2,1,3]
# . If we choose i=4
#  and j=3
# , the resulting array will be a=[5,4,1,1,2]
# .
#
# After all operations, the array will consist of a single element x
# . Find the maximum possible value of x
#  if Pak Chanek performs the operations optimally.
#
# ∗
# ⌊x⌋
#  denotes the floor function of x
# , which is the greatest integer that is less than or equal to x
# . For example, ⌊6⌋=6
# , ⌊2.5⌋=2
# , ⌊−3.6⌋=−4
#  and ⌊π⌋=3
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤5000
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (2≤n≤50
# ) — the length of the array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the elements of the array a
# .
#
# Do note that the sum of n
#  over all test cases is not bounded.
#
# Output
# For each test case, output a single integer: the maximum possible value of x
#  after all numbers have been picked.
#
# Example
# InputCopy
# 3
# 5
# 1 7 8 4 5
# 3
# 2 6 5
# 5
# 5 5 5 5 5
# OutputCopy
# 6
# 4
# 5
# Note
# In the first test case, the array is initially a=[1,7,8,4,5]
# . Pak Chanek will perform the following operations:
#
# Pick i=1
#  and j=2
# , then a=[8,4,5,4]
# .
# Pick i=3
#  and j=2
# , then a=[8,4,4]
# .
# Pick i=2
#  and j=3
# , then a=[8,4]
# .
# Pick i=1
#  and j=2
# , then a=[6]
# .
# After all the operations, the array consists of a single element x=6
# . It can be proven that there is no series of operations that results in x
#  greater than 6
#  in the end.
# Solution
# C++ O(NlogN + N) O(1) Sorting Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    long long output = (nums[1] + nums[0]) / 2;
    for (int i = 2; i < n; ++i) {
        output = (output + nums[i]) / 2;
    }
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN + N) O(1) Sorting Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    output: int = (nums[0] + nums[1]) // 2
    for i in range(2, n):
        output = (output + nums[i]) // 2
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()