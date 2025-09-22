# A. Cut the Array
# time limit per test2 seconds
# memory limit per test512 megabytes
# You are given an array of n
#  non-negative integers [a1,a2,…,an]
# .
#
# Your task is to cut it into three non-empty parts: a prefix, a middle part, and a suffix. Formally, you need to choose two integers l
#  and r
#  such that 1≤l<r<n
# , and obtain three parts:
#
# the prefix up the element at index l
#  inclusive (i.e., [a1,a2,…,al]
# );
# the central part from the element at index l+1
#  to the element at index r
#  inclusive (i.e., [al+1,al+2,…,ar]
# );
# the suffix from the element at index r+1
#  to n
#  inclusive (i.e., [ar+1,ar+2,…,an]
# ).
# Let s1,s2,s3
#  be the remainders of the sums of these parts modulo 3
# . In other words:
#
# s1=(∑i=1lai)mod3
# ;
# s2=(∑i=l+1rai)mod3
# ;
# s3=(∑i=r+1nai)mod3
# .
# Your task is to find such boundaries l
#  and r
#  that either all numbers s1,s2,s3
#  are different, or all numbers s1,s2,s3
#  are the same.
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case consists of two lines:
#
# the first line contains a single integer n
#  (3≤n≤40
# );
# the second line contains n
#  integers a1,a2,…,an
#  (0≤ai≤40
# ).
# Output
# For each test case, if a suitable pair of integers l
#  and r
#  (1≤l<r<n
# ) exists, output these two integers (if there are multiple suitable pairs, you can output any of them). Otherwise, output two integers equal to 0
# .
#
# Example
# InputCopy
# 4
# 6
# 1 2 3 4 5 6
# 4
# 1 3 3 7
# 3
# 2 1 0
# 5
# 7 2 6 2 4
# OutputCopy
# 3 5
# 0 0
# 1 2
# 2 4
# Note
# Consider the examples from the statement:
#
# in the first example, the array is cut into parts [1,2,3]
# , [4,5]
# , [6]
# ; s1=s2=s3=0
# ;
# in the second example, there is no suitable cut;
# in the third example, the array is cut into parts [2]
# , [1]
# , [0]
# ; s1=2
# , s2=1
# , s3=0
# ;
# in the fourth example, the array is cut into parts [7,2]
# , [6,2]
# , [4]
# ; s1=0
# , s2=2
# , s3=1
# .
# Solution
# C++ O(N^3) O(1) Constructive
#include <iostream>
#include <vector>
#include <numeric>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    bool isValid = false;
    int left = 0, right = 0;
    for (size_t l = 1; l <= n - 2; ++l) {
        for (size_t r = l + 1; r <= n - 1; ++r) {
            int first = std::accumulate(nums.begin(), nums.begin() + l + 1, 0) % 3;
            int middle = std::accumulate(nums.begin() + l + 1, nums.begin() + r + 1, 0) % 3;
            int end = std::accumulate(nums.begin() + r + 1, nums.end(), 0) % 3;
            if (first == middle && middle == end) {
                left = l;
                right = r;
                isValid = true;
                break;
            } else if (first != middle && middle != end && first != end) {
                left = l;
                right = r;
                isValid = true;
                break;
            }
        }
        if (isValid) break;
    }
    std::cout << left << " " << right << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N^3) O(1) Constructive
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    left: int = 0
    right: int = 0
    is_valid: bool = False
    for l in range(1, n - 1):
        for r in range(l + 1, n):
            first: int = sum(nums[:l + 1]) % 3
            middle: int = sum(nums[l + 1:r + 1]) % 3
            end: int = sum(nums[r + 1:]) % 3
            if (first == middle == end) or len(set([first, middle, end])) == 3:
                left = l
                right = r
                is_valid = True
                break
        if is_valid: break
    sys.stdout.write('{} {}\n'.format(left, right))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()