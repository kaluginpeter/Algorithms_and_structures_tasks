# A. Find Minimum Operations
# time limit per test1 second
# memory limit per test256 megabytes
# You are given two integers n
#  and k
# .
#
# In one operation, you can subtract any power of k
#  from n
# . Formally, in one operation, you can replace n
#  by (n−kx)
#  for any non-negative integer x
# .
#
# Find the minimum number of operations required to make n
#  equal to 0
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The only line of each test case contains two integers n
#  and k
#  (1≤n,k≤109
# ).
#
# Output
# For each test case, output the minimum number of operations on a new line.
#
# Example
# InputCopy
# 6
# 5 2
# 3 5
# 16 4
# 100 3
# 6492 10
# 10 1
# OutputCopy
# 2
# 3
# 1
# 4
# 21
# 10
# Note
# In the first test case, n=5
#  and k=2
# . We can perform the following sequence of operations:
#
# Subtract 20=1
#  from 5
# . The current value of n
#  becomes 5−1=4
# .
# Subtract 22=4
#  from 4
# . The current value of n
#  becomes 4−4=0
# .
# It can be shown that there is no way to make n
#  equal to 0
#  in less than 2
#  operations. Thus, 2
#  is the answer.
#
# In the second test case, n=3
#  and k=5
# . We can perform the following sequence of operations:
#
# Subtract 50=1
#  from 3
# . The current value of n
#  becomes 3−1=2
# .
# Subtract 50=1
#  from 2
# . The current value of n
#  becomes 2−1=1
# .
# Subtract 50=1
#  from 1
# . The current value of n
#  becomes 1−1=0
# .
# It can be shown that there is no way to make n
#  equal to 0
#  in less than 3
#  operations. Thus, 3
#  is the answer.
# Solution
# C++ O(logk(N)) O(1) Math
#include <iostream>


void solution() {
    long long n, k;
    std::cin >> n >> k;
    if (k == 1) {
        std::cout << n << std::endl;
        return;
    }
    int steps = 0;
    while (n) {
        int subtrct = 1;
        while (subtrct * k <= n) subtrct *= k;
        n -= subtrct;
        ++steps;
        if (n && n < k) {
            steps += n;
            n = 0;
        }
    }
    std::cout << steps << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(logk(N)) O(1) Math
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    if k == 1:
        sys.stdout.write('{}\n'.format(n))
        return
    steps: int = 0
    while n:
        power: int = 1
        while power * k <= n: power *= k
        n -= power
        steps += 1
        if n and n < k:
            steps += n
            n = 0
    sys.stdout.write('{}\n'.format(steps))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()