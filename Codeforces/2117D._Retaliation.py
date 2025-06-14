# D. Retaliation
# time limit per test2 seconds
# memory limit per test256 megabytes
# Yousef wants to explode an array a1,a2,…,an
# . An array gets exploded when all of its elements become equal to zero.
#
# In one operation, Yousef can do exactly one of the following:
#
# For every index i
#  in a
# , decrease ai
#  by i
# .
# For every index i
#  in a
# , decrease ai
#  by n−i+1
# .
# Your task is to help Yousef determine if it is possible to explode the array using any number of operations.
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains an integer n
#  (2≤n≤2⋅105
# ) — the size of the array.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the elements of the array.
#
# It is guaranteed that the sum of n
#  over all test cases doesn't exceed 2⋅105
# .
#
# Output
# For each test case, print "YES" if Yousef can explode the array, otherwise output "NO".
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 6
# 4
# 3 6 6 3
# 5
# 21 18 15 12 9
# 10
# 2 6 10 2 5 5 1 2 4 10
# 7
# 10 2 16 12 8 20 4
# 2
# 52 101
# 2
# 10 2
# OutputCopy
# NO
# YES
# NO
# NO
# YES
# NO
# Note
# In the second test case, we can do the following:
#
# Perform 1
#  operation of the first type. The array becomes [20,16,12,8,4]
# .
# Perform 4
#  operations of the second type. The array becomes [0,0,0,0,0]
# .
# In the first, third, fourth, and sixth test cases, it can be proven that it is impossible to make all elements equal to zero using any number of operations.
# Solution
# C++ O(N) O(1) Greedy Math
#include <iostream>
#include <vector>
#include <numeric>

void solution() {
    int n;
    std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; ++i) std::cin >> a[i];

    if (n < 2) {
        std::cout << "YES\n";
        return;
    }

    long long k_numerator = a[n - 1] - a[0];
    if (k_numerator % (n - 1) != 0) {
        std::cout << "NO\n";
        return;
    }
    long long k = k_numerator / (n - 1);
    for (int i = 0; i < n; ++i) {
        if (a[i] != a[0] + (long long)i * k) {
            std::cout << "NO\n";
            return;
        }
    }
    long long y_numerator = a[0] - k;

    if (y_numerator < 0 || y_numerator % (n + 1) != 0) {
        std::cout << "NO\n";
        return;
    }
    long long y = y_numerator / (n + 1);
    long long x = y + k;
    if (x < 0) {
        std::cout << "NO\n";
        return;
    }
    std::cout << "YES\n";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) solution();
    return 0;
}
# Python O(N) O(1) Greedy NumberTheory
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    a: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    if n < 2:
        sys.stdout.write('YES\n')
        return
    k_numerator: int = a[-1] - a[0]
    if k_numerator % (n - 1) != 0:
        sys.stdout.write('NO\n')
        return
    k: int = k_numerator // (n - 1)
    for i in range(n):
        if a[i] != a[0] + i * k:
            sys.stdout.write('NO\n')
            return
    y_numerator: int = a[0] - k
    if y_numerator < 0 or y_numerator % (n + 1) != 0:
        sys.stdout.write('NO\n')
        return
    y: int = y_numerator // (n + 1)
    x: int = y + k
    if x < 0:
        sys.stdout.write('NO\n')
        return
    sys.stdout.write('YES\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        solution()