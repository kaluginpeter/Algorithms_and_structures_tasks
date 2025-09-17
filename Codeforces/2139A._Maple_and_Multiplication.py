# A. Maple and Multiplication
# time limit per test1 second
# memory limit per test256 megabytes
# Maple has two positive integers a
#  and b
# . She may perform the following operation any number of times (possibly zero) to make a
#  equal to b
# :
#
# Choose any positive integer x
# , and multiply either a
#  or b
#  by x
# .
# Your task is to determine the minimum number of operations required to make a
#  equal to b
# . It can be proven that this is always possible.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The first and only line of each test case contains two positive integers a
#  and b
#  (1≤a,b≤1000
# ) — the numbers Maple currently has.
#
# Output
# For each test case, output a single integer representing the minimum number of operations Maple needs to make a
#  equal to b
# .
#
# Example
# InputCopy
# 3
# 1 2
# 10 3
# 1000 1000
# OutputCopy
# 1
# 2
# 0
# Note
# In the first test case, you can multiply a=1
#  by 2
#  to obtain a=b=2
# . This requires one operation.
#
# In the second test case, you can multiply a=10
#  by 300
#  to get a=3000
# , then multiply b=3
#  by 1000
#  to get b=3000
# . This requires two operations. Note that the numbers may exceed 1000
#  after the operations.
#
# In the third test case, a
#  and b
#  are already equal, so no operations are required.
# Solution
# C++ O(sqrt(max(N, M))) O(D) Math
#include <iostream>
#include <unordered_map>
#include <cmath>

void factorize(int x, std::unordered_map<int, int>& common, int direction) {
    while (!(x & 1)) {
        common[2] += direction;
        x >>= 1;
    }
    int bound = std::sqrt(x) + 1;
    for (int d = 3; d < bound; d += 2) {
        while (x % d == 0) {
            common[d] += direction;
            x /= d;
        }
    }
    if (x > 1) common[x] += direction;
}

void solution() {
    int n, m;
    std::cin >> n >> m;
    std::unordered_map<int, int> common;
    factorize(n, common, 1);
    factorize(m, common, -1);
    int first = 0, second = 0;
    for (const auto& p : common) {
        if (p.second) (p.second > 0 ? ++first : ++second);
    }
    std::cout << std::min(1, first) + std::min(1, second) << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(sqrt(max(N, M))) O(D) Math
import sys
from collections import defaultdict


def factorize(x: int, common: dict[int, int], direction: int) -> None:
    while not (x & 1):
        common[2] += direction
        x >>= 1
    bound: int = int(x**.5) + 1
    for d in range(3, bound, 2):
        while x % d == 0:
            common[d] += direction
            x //= d
    if x > 1: common[x] += direction


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    common: dict[int, int] = defaultdict(int)
    factorize(n, common, 1)
    factorize(m, common, -1)
    first: int = 0
    second: int = 0
    for prime, freq in common.items():
        if freq:
            if freq < 0: first += 1
            else: second  += 1
    sys.stdout.write('{}\n'.format(min(1, first) + min(1, second)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()