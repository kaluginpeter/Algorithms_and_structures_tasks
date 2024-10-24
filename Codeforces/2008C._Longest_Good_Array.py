# C. Longest Good Array
# time limit per test2 seconds
# memory limit per test256 megabytes
# Today, Sakurako was studying arrays. An array a
#  of length n
#  is considered good if and only if:
#
# the array a
#  is increasing, meaning ai−1<ai
#  for all 2≤i≤n
# ;
# the differences between adjacent elements are increasing, meaning ai−ai−1<ai+1−ai
#  for all 2≤i<n
# .
# Sakurako has come up with boundaries l
#  and r
#  and wants to construct a good array of maximum length, where l≤ai≤r
#  for all ai
# .
#
# Help Sakurako find the maximum length of a good array for the given l
#  and r
# .
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# )  — the number of test cases.
#
# The only line of each test case contains two integers l
#  and r
#  (1≤l≤r≤109
# ).
#
# Output
# For each test case, output a single integer  — the length of the longest good array Sakurako can form given l
#  and r
# .
#
# Example
# inputCopy
# 5
# 1 2
# 1 5
# 2 2
# 10 20
# 1 1000000000
# outputCopy
# 2
# 3
# 1
# 5
# 44721
# Note
# For l=1
#  and r=5
# , one possible array could be (1,2,5)
# . It can be proven that an array of length 4
#  does not exist for the given l
#  and r
# .
#
# For l=2
#  and r=2
# , the only possible array is (2)
# .
#
# For l=10
#  and r=20
# , the only possible array is (10,11,13,16,20)
# .
# Solution
# C++ O(1) O(1) Math
#include <iostream>
#include <cmath>

long long highest_n_for_value(long long value, long long s) {
    if (value < s) {
        return -1; // No valid n
    }
    long long target = 2 * (value - s);
    if (target < 0) {
        return -1;
    }

    long long n = static_cast<long long>((-1 + std::sqrt(1 + 8 * (value - s))) / 2);
    return n;
}

long long count_in_sequence(long long l, long long r) {
    long long n_max = highest_n_for_value(r, l);
    long long n_min = highest_n_for_value(l - 1, l);
    return n_max - n_min;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        long long l, r;
        std::cin >> l >> r;
        std::cout << count_in_sequence(l, r) << std::endl;
    }
}

# Python O(1) O(1) Math
import math
import sys

def count_in_sequence(l, r):
    def highest_n_for_value(value):
        if value < 1:
            return -1
        s = l
        target = 2 * (value - s)
        if target < 0:
            return -1
        n = int((-1 + math.sqrt(1 + 8 * (value - s))) / 2)
        return n
    n_max = highest_n_for_value(r)
    n_min = highest_n_for_value(l - 1)
    return n_max - n_min

def solution(t: int) -> None:
    for _ in range(t):
        l, r = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(str(count_in_sequence(l, r)) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)