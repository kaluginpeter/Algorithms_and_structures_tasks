# C. Prefix Min and Suffix Max
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an array a
#  of distinct integers.
#
# In one operation, you may either:
#
# choose a nonempty prefix∗
#  of a
#  and replace it with its minimum value, or
# choose a nonempty suffix†
#  of a
#  and replace it with its maximum value.
# Note that you may choose the entire array a
# .
#
# For each element ai
# , determine if there exists some sequence of operations to transform a
#  into [ai]
# ; that is, make the array a
#  consist of only one element, which is ai
# . Output your answer as a binary string of length n
# , where the i
# -th character is 1
#  if there exists a sequence to transform a
#  into [ai]
# , and 0
#  otherwise.
#
# ∗
# A prefix of an array is a subarray consisting of the first k
#  elements of the array, for some integer k
# .
#
# †
# A suffix of an array is a subarray consisting of the last k
#  elements of the array, for some integer k
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# )  — the number of test cases.
#
# The first line of each test case contains one integer n
#  (2≤n≤2⋅105
# ) — the size of the array a
# .
#
# The second line of each test case contains n
#  integers, a1,a2,…,an
#  (1≤ai≤106
# ). It is guaranteed that all ai
#  are distinct.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output a binary string of length n
#   — the i
# -th character should be 1
#  if there exists a sequence of operations as described above, and 0
#  otherwise.
#
# Example
# InputCopy
# 3
# 6
# 1 3 5 4 7 2
# 4
# 13 10 12 20
# 7
# 1 2 3 4 5 6 7
# OutputCopy
# 100011
# 1101
# 1000001
# Note
# In the first sample, you can first choose the prefix of size 3
# . Then the array is transformed into
#
# 1	4	7	2
# Next, you can choose the suffix of size 2
# . Then the array is transformed into
# 1	4	7
# Finally, you can choose the prefix of size 3
# . Then the array is transformed into
# 1
# So we see that it is possible to transform a
#  into [1]
# .
# It can be shown that it is impossible to transform a
#  into [3]
# .
# Solution
# C++ O(N) O(N) Greedy
#include <iostream>
#include <vector>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    // for each number we should find leftmost Greater and rightmost Less
    std::vector<int> checker(n, 0);
    int minValue = 1e6 + 1;
    for (int i = 0; i < n; ++i) {
        if (minValue < nums[i]) ++checker[i];
        minValue = std::min(minValue, nums[i]);
    }
    int maxValue = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (maxValue > nums[i]) ++checker[i];
        maxValue = std::max(maxValue, nums[i]);
    }
    for (int i = 0; i < n; ++i) {
        std::cout << (checker[i] == 2 ? "0" : "1");
    }
    std::cout << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(N) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    checker: list[int] = [0] * n
    min_value: int = 1000001
    for i in range(n):
        if min_value < nums[i]: checker[i] += 1
        min_value = min(min_value, nums[i])
    max_value: int = 0
    for i in range(n - 1, -1, -1):
        if max_value > nums[i]: checker[i] += 1
        max_value = max(max_value, nums[i])
    for i in range(n):
        sys.stdout.write("{}".format(['1', '0'][checker[i] == 2]))
    sys.stdout.write('\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()