# A. To Zero
# time limit per test2 seconds
# memory limit per test512 megabytes
# You are given two integers n
#  and k
# ; k
#  is an odd number not less than 3
# . Your task is to turn n
#  into 0
# .
#
# To do this, you can perform the following operation any number of times: choose a number x
#  from 1
#  to k
#  and subtract it from n
# . However, if the current value of n
#  is even (divisible by 2
# ), then x
#  must also be even, and if the current value of n
#  is odd (not divisible by 2
# ), then x
#  must be odd.
#
# In different operations, you can choose the same values of x
# , but you don't have to. So, there are no limitations on using the same value of x
# .
#
# Calculate the minimum number of operations required to turn n
#  into 0
# .
#
# Input
# The first line contains one integer t
#  (1≤t≤10000
# ) — the number of test cases.
#
# Each test case consists of one line containing two integers n
#  and k
#  (3≤k≤n≤109
# , k
#  is odd).
#
# Output
# For each test case, output one integer — the minimum number of operations required to turn n
#  into 0
# .
#
# Example
# InputCopy
# 8
# 39 7
# 9 3
# 6 3
# 999967802 3
# 5 5
# 6 5
# 999999999 3
# 1000000000 3
# OutputCopy
# 7
# 4
# 3
# 499983901
# 1
# 2
# 499999999
# 500000000
# Note
# In the first example from the statement, you can first subtract 5
#  from 39
#  to get 34
# . Then subtract 6
#  five times to get 4
# . Finally, subtract 4
#  to get 0
# .
#
# In the second example, you can subtract 3
#  once, and then subtract 2
#  three times.
#
# In the third example, you can subtract 2
#  three times.
# Solution
# C++ O(1) O(1) Math
#include <iostream>

void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        long long n, k;
        std::cin >> n >> k;
        if (n & 1) std::cout << 1 + ((n - k) + (k - 1) - 1) / (k - 1) << "\n";
        else std::cout << (n + (k - 1) - 1) / (k - 1) << "\n";
    }
}

int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().rstrip().split())
        if n & 1: sys.stdout.write('{}\n'.format(1 + ((n - k) + (k - 1) - 1) // (k - 1)))
        else: sys.stdout.write('{}\n'.format((n + (k - 1) - 1) // (k - 1)))


if __name__ == '__main__':
    solution()