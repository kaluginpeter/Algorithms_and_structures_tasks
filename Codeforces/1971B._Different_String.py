# B. Different String
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a string s
#  consisting of lowercase English letters.
#
# Rearrange the characters of s
#  to form a new string r
#  that is not equal to s
# , or report that it's impossible.
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The only line of each test case contains a string s
#  of length at most 10
#  consisting of lowercase English letters.
#
# Output
# For each test case, if no such string r
#  exists as described in the statement, output "NO" (without quotes).
#
# Otherwise, output "YES" (without quotes). Then, output one line — the string r
# , consisting of letters of string s
# .
#
# You can output "YES" and "NO" in any case (for example, strings "yEs", "yes", and "Yes" will be recognized as a positive response).
#
# If multiple answers are possible, you can output any of them.
#
# Example
# InputCopy
# 8
# codeforces
# aaaaa
# xxxxy
# co
# d
# nutdealer
# mwistht
# hhhhhhhhhh
# OutputCopy
# YES
# forcodesec
# NO
# YES
# xxyxx
# YES
# oc
# NO
# YES
# undertale
# YES
# thtsiwm
# NO
# Note
# In the first test case, another possible answer is forcescode
# .
#
# In the second test case, all rearrangements of aaaaa
#  are equal to aaaaa
# .
# Solution
# Python O(N) O(1) String
from __future__ import annotations
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        s: list[str] = list(sys.stdin.readline().rstrip())
        is_valid: bool = False
        x: int = 0
        y: int = 0
        for idx in range(1, len(s)):
            if s[idx] != s[idx - 1]:
                is_valid = True
                x = idx
                y = idx - 1
                break
        if is_valid:
            sys.stdout.write('YES\n')
            s[x], s[y] = s[y], s[x]
            sys.stdout.write(''.join(s) + '\n')
        else:
            sys.stdout.write('NO\n')


if __name__ == '__main__':
    solution()

# C++ O(N) O(1)
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string s;
        std::cin >> s;
        bool isValid = false;
        int x = 0;
        int y = 0;
        for (int idx = 1; idx < s.size(); ++idx) {
            if (s[idx] != s[idx - 1]) {
                isValid = true;
                x = idx - 1;
                y = idx;
                break;
            }
        }
        if (isValid) {
            std::cout << "YES\n";
            std::swap(s[x], s[y]);
            std::cout << s << "\n";
        } else {
            std::cout << "NO\n";
        }
    }
}


int main() {
    solution();
}