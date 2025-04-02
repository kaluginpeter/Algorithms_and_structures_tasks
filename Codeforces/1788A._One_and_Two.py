# A. One and Two
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a sequence a1,a2,…,an
# . Each element of a
#  is 1
#  or 2
# .
#
# Find out if an integer k
#  exists so that the following conditions are met.
#
# 1≤k≤n−1
# , and
# a1⋅a2⋅…⋅ak=ak+1⋅ak+2⋅…⋅an
# .
# If there exist multiple k
#  that satisfy the given condition, print the smallest.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). Description of the test cases follows.
#
# The first line of each test case contains one integer n
#  (2≤n≤1000
# ).
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤2
# ).
#
# Output
# For each test case, if there is no such k
# , print −1
# .
#
# Otherwise, print the smallest possible k
# .
#
# Example
# InputCopy
# 3
# 6
# 2 2 1 2 1 2
# 3
# 1 2 1
# 4
# 1 1 1 1
# OutputCopy
# 2
# -1
# 1
# Note
# For the first test case, k=2
#  satisfies the condition since a1⋅a2=a3⋅a4⋅a5⋅a6=4
# . k=3
#  also satisfies the given condition, but the smallest should be printed.
#
# For the second test case, there is no k
#  that satisfies a1⋅a2⋅…⋅ak=ak+1⋅ak+2⋅…⋅an
#
# For the third test case, k=1
# , 2
# , and 3
#  satisfy the given condition, so the answer is 1
# .
# Solution
# Python O(N) O(N) Prefix Sum
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
        prefix_sum: list[int] = [0]
        for _ in range(n):
            prefix_sum.append(prefix_sum[-1] + (next(nums) == 2))
        answer: int = -1
        for k in range(1, n):
            if prefix_sum[k] == prefix_sum[n] - prefix_sum[k]:
                answer = k
                break
        sys.stdout.write('{}\n'.format(answer))


if __name__ == '__main__':
    solution()

# C++ O(N) O(N) PrefixSum
#include <iostream>
#include <vector>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::vector<int> prefixSum = {0};
        for (int j = 0; j < n; ++j) {
            int num;
            std::scanf("%d", &num);
            prefixSum.push_back(prefixSum.back() + static_cast<int>(num == 2));
        }
        int answer = -1;
        for (int k = 1; k < n; ++k) {
            if (prefixSum[k] == prefixSum[n] - prefixSum[k]) {
                answer = k;
                break;
            }
        }
        std::printf("%d\n", answer);
    }
}


int main() {
    solution();
}