# D. Same Differences
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an array a
#  of n
#  integers. Count the number of pairs of indices (i,j)
#  such that i<j
#  and aj−ai=j−i
# .
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ). Then t
#  test cases follow.
#
# The first line of each test case contains one integer n
#  (1≤n≤2⋅105
# ).
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤n
# ) — array a
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case output the number of pairs of indices (i,j)
#  such that i<j
#  and aj−ai=j−i
# .
#
# Example
# InputCopy
# 4
# 6
# 3 5 1 4 6 6
# 3
# 1 2 3
# 4
# 1 3 3 4
# 6
# 1 6 3 4 5 6
# OutputCopy
# 1
# 3
# 3
# 10
# Solution
# C++ O(N) O(N) HashMap Math
#include <iostream>
#include <unordered_map>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        long long n;
        std::cin >> n;
        std::unordered_map<long long, long long> hashmap;
        long long output = 0;
        for (long long j = 0; j < n; ++j) {
            long long num;
            std::cin >> num;
            output += hashmap[j - num + 1];
            ++hashmap[j - num + 1];
        }
        std::cout << output << std::endl;
    }
}

# Python O(N) O(N) Hashmap Greedy
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
        hashmap: dict = dict()
        output: int = 0
        for j in range(n):
            output += hashmap.get(nums[j] - j + 1, 0)
            hashmap[nums[j] - j + 1] = hashmap.get(nums[j] - j + 1, 0) + 1
        sys.stdout.write(str(output) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
