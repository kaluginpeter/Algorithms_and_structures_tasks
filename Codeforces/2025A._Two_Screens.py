# A. Two Screens
# time limit per test2 seconds
# memory limit per test512 megabytes
# There are two screens which can display sequences of uppercase Latin letters. Initially, both screens display nothing.
#
# In one second, you can do one of the following two actions:
#
# choose a screen and an uppercase Latin letter, and append that letter to the end of the sequence displayed on that screen;
# choose a screen and copy the sequence from it to the other screen, overwriting the sequence that was displayed on the other screen.
# You have to calculate the minimum number of seconds you have to spend so that the first screen displays the sequence s
# , and the second screen displays the sequence t
# .
#
# Input
# The first line contains one integer q
#  (1≤q≤500
# ) — the number of test cases.
#
# Each test case consists of two lines. The first line contains the string s
# , and the second line contains the string t
#  (1≤|s|,|t|≤100
# ). Both strings consist of uppercase Latin letters.
#
# Output
# For each test case, print one integer — the minimum possible number of seconds you have to spend so that the first screen displays the sequence s
# , and the second screen displays the sequence t
# .
#
# Example
# InputCopy
# 3
# GARAGE
# GARAGEFORSALE
# ABCDE
# AABCD
# TRAINING
# DRAINING
# OutputCopy
# 14
# 10
# 16
# Note
# In the first test case, the following sequence of actions is possible:
#
# spend 6
#  seconds to write the sequence GARAGE on the first screen;
# copy the sequence from the first screen to the second screen;
# spend 7
#  seconds to complete the sequence on the second screen by writing FORSALE.
# In the second test case, the following sequence of actions is possible:
#
# spend 1
#  second to write the sequence A on the second screen;
# copy the sequence from the second screen to the first screen;
# spend 4
#  seconds to complete the sequence on the first screen by writing BCDE;
# spend 4
#  seconds to complete the sequence on the second screen by writing ABCD.
# In the third test case, the fastest way to display the sequences is to type both of them character by character without copying, and this requires 16
#  seconds.
# Solution
# C++ O(min(N, M)) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    std::string a, b;
    std::cin >> a >> b;
    if (a.size() < b.size()) std::swap(a, b);
    int i = 0;
    while (i < b.size() && a[i] == b[i]) ++i;
    std::cout << (i? 1 : 0) + (a.size() - i) + b.size() << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(min(N, M)) O(1) Greedy
import sys


def solution() -> None:
    a: str = sys.stdin.readline().rstrip()
    b: str = sys.stdin.readline().rstrip()
    i: int = 0
    if len(a) < len(b): a, b = b, a
    while i < len(b) and a[i] == b[i]: i += 1
    sys.stdout.write('{}\n'.format(len(a) - i + len(b) + bool(i)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()