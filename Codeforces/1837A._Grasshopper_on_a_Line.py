# A. Grasshopper on a Line
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given two integers x
#  and k
# . Grasshopper starts in a point 0
#  on an OX axis. In one move, it can jump some integer distance, that is not divisible by k
# , to the left or to the right.
#
# What's the smallest number of moves it takes the grasshopper to reach point x
# ? What are these moves? If there are multiple answers, print any of them.
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of testcases.
#
# The only line of each testcase contains two integers x
#  and k
#  (1≤x≤100
# ; 2≤k≤100
# ) — the endpoint and the constraint on the jumps, respectively.
#
# Output
# For each testcase, in the first line, print a single integer n
#  — the smallest number of moves it takes the grasshopper to reach point x
# .
#
# In the second line, print n
#  integers, each of them not divisible by k
# . A positive integer would mean jumping to the right, a negative integer would mean jumping to the left. The endpoint after the jumps should be exactly x
# .
#
# Each jump distance should be from −109
#  to 109
# . In can be shown that, for any solution with the smallest number of jumps, there exists a solution with the same number of jumps such that each jump is from −109
#  to 109
# .
#
# It can be shown that the answer always exists under the given constraints. If there are multiple answers, print any of them.
#
# Example
# inputCopy
# 3
# 10 2
# 10 3
# 3 4
# outputCopy
# 2
# 7 3
# 1
# 10
# 1
# 3
# Solution
# Python O(1) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        x, k = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(['1\n' + str(x), '2\n' + str(x - 1) + ' ' + '1'][x % k == 0] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(1) O(1) Math
#include <iostream>

int main() {
    size_t t;
    std::cin >> t;
    for (size_t rep = 0; rep < t; ++rep) {
        int x, k;
        std::cin >> x >> k;
        if (x % k != 0) {
            std::cout << 1 << std::endl << x << std::endl;
        } else {
            std::cout << 2 << std::endl << x - 1 << " " << 1 << std::endl;
        }
    }
}