# C. Equal Values
# time limit per test2 seconds
# memory limit per test512 megabytes
# You are given an array a1,a2,…,an
# , consisting of n
#  integers.
#
# In one operation, you are allowed to perform one of the following actions:
#
# Choose a position i
#  (1<i≤n
# ) and make all elements to the left of i
#  equal to ai
# . That is, assign the value ai
#  to all aj
#  (1≤j<i
# ). The cost of such an operation is (i−1)⋅ai
# .
# Choose a position i
#  (1≤i<n
# ) and make all elements to the right of i
#  equal to ai
# . That is, assign the value ai
#  to all aj
#  (i<j≤n
# ). The cost of such an operation is (n−i)⋅ai
# .
# Note that the elements affected by an operation may already be equal to ai
# , but that doesn't change the cost.
#
# You are allowed to perform any number of operations (including zero). What is the minimum total cost to make all elements of the array equal?
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (2≤n≤5⋅105
# ).
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤n
# ).
#
# The sum of n
#  over all test cases does not exceed 5⋅105
# .
#
# Output
# For each test case, print a single integer — the minimum total cost of operations to make all elements of the array equal.
#
# Example
# InputCopy
# 3
# 4
# 2 4 1 3
# 3
# 1 1 1
# 10
# 7 5 5 5 10 9 9 4 6 10
# OutputCopy
# 3
# 0
# 35
# Note
# In the first test case, you can perform the operation twice:
#
# choose i=3
#  and make all elements to the left of it equal to it, the cost will be 2⋅1=2
# ;
# choose i=3
#  and make all elements to the right of it equal to it, the cost will be 1⋅1=1
# .
# The total cost is 2+1=3
# .
#
# In the second test case, all elements are already equal, so no operations need to be performed.
# Solution
# C++ O(N) O(N) TwoPointers
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cstdint>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    long long output = INT64_MAX;
    std::unordered_map<int, std::pair<int, int>> segments;
    int left = 0;
    for (int right = 1; right < n; ++right) {
        if (nums[right] != nums[left]) {
            if (!segments.count(nums[left])) segments[nums[left]] = {left, right};
            else {
                if (right - left > segments[nums[left]].second - segments[nums[left]].first) segments[nums[left]] = {left, right};
            }
            left = right;
        }
    }
    if (!segments.count(nums[left])) segments[nums[left]] = {left, n};
    else {
        if (n - left > segments[nums[left]].second - segments[nums[left]].first) segments[nums[left]] = {left, n};
    }
    for (auto p : segments) {
        output = std::min(output, static_cast<long long>(p.second.first) * p.first + static_cast<long long>(n - p.second.second) * p.first);
    }

    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(N) TwoPointers
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    segments: dict[int, tuple[int, int]] = dict()
    left: int = 0
    for right in range(1, n):
        if nums[left] != nums[right]:
            if nums[left] not in segments: segments[nums[left]] = (left, right)
            elif right - left > segments[nums[left]][1] - segments[nums[left]][0]: segments[nums[left]] = (left, right)
            left = right
    if nums[left] not in segments: segments[nums[left]] = (left, n)
    elif n - left > segments[nums[left]][1] - segments[nums[left]][0]: segments[nums[left]] = (left, n)
    output: int = min(left * v + (n - right) * v for v, (left, right) in segments.items())
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()