# B. Normal Problem
# time limit per test1 second
# memory limit per test256 megabytes
# A string consisting of only characters 'p', 'q', and 'w' is painted on a glass window of a store. Ship walks past the store, standing directly in front of the glass window, and observes string a
# . Ship then heads inside the store, looks directly at the same glass window, and observes string b
# .
#
# Ship gives you string a
# . Your job is to find and output b
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# The only line of each test case contains a string a
#  (1≤|a|≤100
# ) — the string Ship observes from outside the store. It is guaranteed that a
#  only contains characters 'p', 'q', and 'w'.
#
# Output
# For each test case, output string b
# , the string Ship observes from inside the store, on a new line.
#
# Example
# InputCopy
# 5
# qwq
# ppppp
# pppwwwqqq
# wqpqwpqwwqp
# pqpqpqpq
# OutputCopy
# pwp
# qqqqq
# pppwwwqqq
# qpwwpqwpqpw
# pqpqpqpq
# Solution
# C++ O(N) O(N) String
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string a;
        std::cin >> a;
        std::string b = "";
        for (int i = a.size() - 1; i >= 0; --i) {
            if (a[i] == 'p') b += 'q';
            else if (a[i] == 'q') b += 'p';
            else b += 'w';
        }
        std::cout << b << "\n";
    }
}


int main() {
    solution();
}

# Python O(N) O(N) String
from __future__ import annotations
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        a: str = sys.stdin.readline().rstrip()
        b: list[str] = []
        for ch in reversed(a):
            if ch == 'p': b.append('q')
            elif ch == 'q': b.append('p')
            else: b.append('w')
        sys.stdout.write(''.join(b) + '\n')


if __name__ == '__main__':
    solution()
