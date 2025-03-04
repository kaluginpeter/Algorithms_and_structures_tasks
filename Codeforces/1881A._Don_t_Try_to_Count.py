# A. Don't Try to Count
# time limit per test2 seconds
# memory limit per test256 megabytes
# Given a string x
#  of length n
#  and a string s
#  of length m
#  (n⋅m≤25
# ), consisting of lowercase Latin letters, you can apply any number of operations to the string x
# .
#
# In one operation, you append the current value of x
#  to the end of the string x
# . Note that the value of x
#  will change after this.
#
# For example, if x=
# "aba", then after applying operations, x
#  will change as follows: "aba" →
#  "abaaba" →
#  "abaabaabaaba".
#
# After what minimum number of operations s
#  will appear in x
#  as a substring? A substring of a string is defined as a contiguous segment of it.
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two numbers n
#  and m
#  (1≤n⋅m≤25
# ) — the lengths of strings x
#  and s
# , respectively.
#
# The second line of each test case contains the string x
#  of length n
# .
#
# The third line of each test case contains the string s
#  of length m
# .
#
# Output
# For each test case, output a single number — the minimum number of operations after which s
#  will appear in x
#  as a substring. If this is not possible, output −1
# .
#
# Example
# InputCopy
# 12
# 1 5
# a
# aaaaa
# 5 5
# eforc
# force
# 2 5
# ab
# ababa
# 3 5
# aba
# ababa
# 4 3
# babb
# bbb
# 5 1
# aaaaa
# a
# 4 2
# aabb
# ba
# 2 8
# bk
# kbkbkbkb
# 12 2
# fjdgmujlcont
# tf
# 2 2
# aa
# aa
# 3 5
# abb
# babba
# 1 19
# m
# mmmmmmmmmmmmmmmmmmm
# OutputCopy
# 3
# 1
# 2
# -1
# 1
# 0
# 1
# 3
# 1
# 0
# 2
# 5
# Note
# In the first test case of the example, after 2
#  operations, the string will become "aaaa", and after 3
#  operations, it will become "aaaaaaaa", so the answer is 3
# .
#
# In the second test case of the example, after applying 1
#  operation, the string will become "eforceforc
# ", where the substring is highlighted in red.
#
# In the fourth test case of the example, it can be shown that it is impossible to obtain the desired string as a substring.
# Solution
# C++ O(M) O(N) String
#include <iostream>
#include <string>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, m;
        std::scanf("%d %d", &n, &m);
        std::string a, b;
        std::cin >> a >> b;
        bool isMatch = false;
        int move = 0;
        while (n <= m * 25) {
            if (a.find(b) != std::string::npos) {
                isMatch = true;
                break;
            }
            ++move;
            n += n;
            a = a + a;
        }
        std::cout << (isMatch? move : -1) << "\n";
    }
}


int main() {
    solution();
}

# Python O(M) O(N) String
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        a: str = sys.stdin.readline().rstrip()
        b: str = sys.stdin.readline().rstrip()
        is_valid: bool = False
        move: int = 0
        while n <= m * 25:
            if b in a:
                is_valid = True
                break;
            n += n
            a = a + a
            move += 1
        sys.stdout.write(str([-1, move][is_valid]) + '\n')


if __name__ == '__main__':
    solution()