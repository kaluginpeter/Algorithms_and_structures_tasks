# A. Dinner Time
# time limit per test1 second
# memory limit per test256 megabytes
# Given four integers n
# , m
# , p
# , and q
# , determine whether there exists an integer array a1,a2,…,an
#  (elements may be negative) satisfying the following conditions:
#
# The sum of all elements in the array is equal to m
# :
# a1+a2+…+an=m
# The sum of every p
#  consecutive elements is equal to q
# :
# ai+ai+1+…+ai+p−1=q, for all 1≤i≤n−p+1
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first and only line of each test case contains four integers n
# , m
# , p
# , and q
#  (1≤p≤n≤100
# , 1≤q,m≤100
# ) — the length of the array, the sum of elements, the length of a segment, and the sum of a segment, respectively.
#
# Output
# For each test case, output "YES" (without quotes) if there exists an array satisfying the above conditions, and "NO" (without quotes) otherwise.
#
# You can output "YES" and "NO" in any case (for example, strings "yES", "yes", and "Yes" will all be recognized as valid responses).
#
# Example
# InputCopy
# 5
# 3 2 2 1
# 1 1 1 1
# 5 4 2 3
# 10 7 5 2
# 4 4 1 3
# OutputCopy
# YES
# YES
# YES
# NO
# NO
# Note
# In the first test case, an example of an array satisfying the condition is [1,0,1]
# . This is because:
#
# a1+a2+a3=1+0+1=2=m
# a1+a2=1+0=1=q
# a2+a3=0+1=1=q
# In the second test case, the only array satisfying the condition is [1]
# .
#
# In the third test case, an example of an array satisfying the condition is [−2,5,−2,5,−2]
# .
#
# In the fourth test case, it can be proven that there is no array satisfying the condition.
# Solution
# C++ O(1) O(1) Math
#include <iostream>

void solution() {
    long long n, m, p, q;
    std::cin >> n >> m >> p >> q;

    if (n % p == 0) {
        if (m == (n / p) * q) std::cout << "YES\n";
        else std::cout << "NO\n";
    } else std::cout << "YES\n";
}

int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    n, m, p, q = map(int, sys.stdin.readline().rstrip().split())
    if n % p == 0:
        if m == n // p * q: sys.stdout.write('YES\n')
        else: sys.stdout.write('NO\n')
    else: sys.stdout.write('YES\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()