# B. Move to the End
# time limit per test2 seconds
# memory limit per test512 megabytes
# You are given an array a
#  consisting of n
#  integers.
#
# For every integer k
#  from 1
#  to n
# , you have to do the following:
#
# choose an arbitrary element of a
#  and move it to the right end of the array (you can choose the last element, then the array won't change);
# print the sum of k
#  last elements of a
# ;
# move the element you've chosen on the first step to its original position (restore the original array a
# ).
# For every k
# , you choose the element which you move so that the value you print is the maximum possible.
#
# Calculate the value you print for every k
# .
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each test case consists of two lines:
#
# the first line contains one integer n
#  (1≤n≤2⋅105
# );
# the second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ).
# Additional constraint on the input: the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, print n
#  integers. The i
# -th of these integers should be equal to the maximum value you can print if k=i
# .
#
# Example
# InputCopy
# 4
# 7
# 13 5 10 14 8 15 13
# 6
# 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
# 1
# 42
# 2
# 7 5
# OutputCopy
# 15 28 42 50 63 73 78
# 1000000000 2000000000 3000000000 4000000000 5000000000 6000000000
# 42
# 7 12
# Note
# Let's consider the first test case from the statement:
#
# when k=1
# , you can move the 6
# -th element to the end, the array becomes [13,5,10,14,8,13,15]
# , and the value you print is 15
# ;
# when k=2
# , you can move the 6
# -th element to the end, the array becomes [13,5,10,14,8,13,15]
# , and the value you print is 13+15=28
# ;
# when k=3
# , you can move the 4
# -th element to the end, the array becomes [13,5,10,8,15,13,14]
# , and the value you print is 15+13+14=42
# ;
# when k=4
# , you can move the 5
# -th element to the end, the array becomes [13,5,10,14,15,13,8]
# , and the value you print is 14+15+13+8=50
# ;
# when k=5
# , you can move the 1
# -st element to the end, the array becomes [5,10,14,8,15,13,13]
# , and the value you print is 14+8+15+13+13=63
# ;
# when k=6
# , you can move the 1
# -st element to the end, the array becomes [5,10,14,8,15,13,13]
# , and the value you print is 10+14+8+15+13+13=73
# ;
# when k=7
# , you can move the 6
# -th element to the end, the array becomes [13,5,10,14,8,13,15]
# , and the value you print is 13+5+10+14+8+13+15=78
# .
# Solution
# C++ O(N + K) O(N) DynamicProgramming PrefixSum
#include <iostream>
#include <vector>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    std::vector<int> dp;
    int prev = 0;
    for (int i = 0; i < n; ++i) {
        prev = std::max(prev, nums[i]);
        dp.push_back(prev);
    }
    std::vector<long long> prefixSum(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        prefixSum[i] = prefixSum[i - 1] + nums[i - 1];
    }
    for (int k = 1; k <= n; ++k) {
        long long take = dp[n - k] + (prefixSum[n] - prefixSum[n - k + 1]);
        long long notTake = prefixSum[n] - prefixSum[n - k];
        std::cout << std::max(take, notTake) << " ";
    }
    std::cout << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N + K) O(N) DynamicProgramming PrefixSum
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    dp: list[int] = []
    prefix_sum: list[int] = [0]
    prev: int = 0
    for i in range(n):
        prev = max(prev, nums[i])
        dp.append(prev)
        prefix_sum.append(prefix_sum[-1] + nums[i])
    for k in range(1, n + 1):
        take: int = dp[n - k] + (prefix_sum[n] - prefix_sum[n - k + 1])
        not_take: int = prefix_sum[n] - prefix_sum[n - k]
        sys.stdout.write('{} '.format(max(take, not_take)))
    sys.stdout.write('\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    while t:
        solution();
        t -= 1