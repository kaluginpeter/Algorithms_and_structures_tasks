# A. Brogramming Contest
# time limit per test1 second
# memory limit per test256 megabytes
# One day after waking up, your friend challenged you to a brogramming contest. In a brogramming contest, you are given a binary string∗
#  s
#  of length n
#  and an initially empty binary string t
# . During a brogramming contest, you can make either of the following moves any number of times:
#
# remove some suffix†
#  from s
#  and place it at the end of t
# , or
# remove some suffix from t
#  and place it at the end of s
# .
# To win the brogramming contest, you must make the minimum number of moves required to make s
#  contain only the character 0
#  and t
#  contain only the character 1
# . Find the minimum number of moves required.
# ∗
# A binary string is a string consisting of characters 0
#  and 1
# .
#
# †
# A string a
#  is a suffix of a string b
#  if a
#  can be obtained from deletion of several (possibly, zero or all) elements from the beginning of b
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# The first line of each test case is an integer n
#  (1≤n≤1000
# ) — the length of the string s
# .
#
# The second line of each test case contains the binary string s
# .
#
# The sum of n
#  across all test cases does not exceed 1000
# .
#
# Output
# For each testcase, output the minimum number of moves required.
#
# Example
# InputCopy
# 5
# 5
# 00110
# 4
# 1111
# 3
# 001
# 5
# 00000
# 3
# 101
# OutputCopy
# 2
# 1
# 1
# 0
# 3
# Note
# An optimal solution to the first test case is as follows:
#
# s=00110
# , t=
#  empty string.
# s=00
# , t=110
# .
# s=000
# , t=11
# .
# It can be proven that there is no solution using less than 2
#  moves.
#
# In the second test case, you have to move the whole string from s
#  to t
#  in one move.
#
# In the fourth test case, you don't have to do any moves.
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    int n;
    std::cin >> n;
    std::string s;
    std::cin >> s;
    int output = 0, ones = 0;
    for (const char &ch : s) {
        if (ch == '1') ++ones;
    }
    int i = n - 1;
    while (i >= 0 && ones) {
        if (s[i] == '0') {
            while (i >= 0 && s[i] == '0') -- i;
            while (i >= 0 && s[i] == '1') {
                --i;
                --ones;
            }
            output += 2;
        } else {
            while (i >= 0 && s[i] == '1') {
                --i;
                --ones;
            }
            ++output;
        }
    }
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    s: str = sys.stdin.readline().rstrip()
    ones: int = s.count('1')
    output: int = 0
    i: int = n - 1
    while i >= 0 and ones:
        if s[i] == '0':
            while i >= 0 and s[i] == '0': i -= 1
            while i >= 0 and s[i] == '1':
                ones -= 1
                i -= 1
            output += 2
        else:
            while i >= 0 and s[i] == '1':
                ones -= 1
                i -= 1
            output += 1
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()