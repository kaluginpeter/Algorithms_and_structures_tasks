# B. Lady Bug
# time limit per test1 second
# memory limit per test256 megabytes
# As soon as Dasha Purova crossed the border of France, the villain Markaron kidnapped her and placed her in a prison under his large castle. Fortunately, the wonderful Lady Bug, upon hearing the news about Dasha, immediately ran to save her in Markaron's castle. However, to get there, she needs to crack a complex password.
#
# The password consists of two bit strings a
#  and b
# , each of which has a length of n
# . In one operation, Lady Bug can choose any index 2≤i≤n
#  and perform one of the following actions:
#
# swap(ai
# , bi−1
# ) (swap the values of ai
#  and bi−1
# ), or
# swap(bi
# , ai−1
# ) (swap the values of bi
#  and ai−1
# ).
# Lady Bug can perform any number of operations. The password is considered cracked if she can ensure that the first string consists only of zeros. Help her understand whether or not she will be able to save the unfortunate Dasha.
#
# Input
# Each test consists of several test cases. The first line of the input data contains one integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains one integer n
#  (2≤n≤2⋅105
# ) — the length of the bit strings of the password.
#
# The next two lines contain the bit strings of length n
# , a
#  and b
# , which represent the password. Each of the strings contains only the characters 0 and '1'.
#
# It is guaranteed that the sum of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output "YES" if Lady Bug can crack the password after any number of operations; otherwise, output "NO".
#
# You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
#
# Example
# InputCopy
# 4
# 3
# 000
# 000
# 6
# 010001
# 010111
# 5
# 10000
# 01010
# 2
# 11
# 00
# OutputCopy
# YES
# YES
# NO
# YES
# Note
# In the first test case, the string a
#  immediately consists only of zeros.
#
# In the second test case, a possible sequence of operations is:
#
# swap(a2, b1)
#
# 010001
#
# 010111
#
# swap(b5, a4)
#
# 000001
#
# 110111
#
# swap(a4, b3)
#
# 000101
#
# 110101
#
# swap(a5, b4)
#
# 000001
#
# 111101
# Solution
# C++ O(N) O(1) Greedy Constructive
#include <iostream>
#include <string>


void solution() {
    int n;
    std::cin >> n;
    std::string a, b;
    std::cin >> a >> b;
    int odd = 0, even = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] == '1') {
            if (i & 1) ++even;
            else ++odd;
        }
    }
    for (int i = 0; i < n; ++i) {
        if (b[i] == '0') {
            if (i & 1) --odd;
            else --even;
        }
    }
    std::cout << (odd <= 0 && even <= 0 ? "YES" : "NO") << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy Constructive
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    a: str = sys.stdin.readline().rstrip()
    b: str = sys.stdin.readline().rstrip()
    odd: int = 0
    even: int = 0
    for i in range(n):
        if a[i] == '1':
            if i & 1: even += 1
            else: odd += 1
    for i in range(n):
        if b[i] == '0':
            if i & 1: odd -= 1
            else: even -= 1
    sys.stdout.write('{}\n'.format(['NO', 'YES'][odd <= 0 and even <= 0]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()