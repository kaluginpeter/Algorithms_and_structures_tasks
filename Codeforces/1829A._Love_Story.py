# A. Love Story
# time limit per test1 second
# memory limit per test256 megabytes
# Timur loves codeforces. That's why he has a string s
#  having length 10
#  made containing only lowercase Latin letters. Timur wants to know how many indices string s
#  differs from the string "codeforces".
#
# For example string s=
#  "coolforsez" differs from "codeforces" in 4
#  indices, shown in bold.
#
# Help Timur by finding the number of indices where string s
#  differs from "codeforces".
#
# Note that you can't reorder the characters in the string s
# .
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case is one line and contains the string s
# , consisting of exactly 10
#  lowercase Latin characters.
#
# Output
# For each test case, output a single integer — the number of indices where string s
#  differs.
#
# Example
# inputCopy
# 5
# coolforsez
# cadafurcie
# codeforces
# paiuforces
# forcescode
# outputCopy
# 4
# 5
# 0
# 4
# 9
# Solution
# C++ O(1) O(1) String
#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    std::string valid = "codeforces";
    for (int rep = 0; rep < t; ++rep) {
        std::string n;
        std::cin >> n;
        int count = 0;
        for (size_t index = 0; index < valid.size(); ++index) {
            if (valid[index] != n[index]) {
                count++;
            }
        };
        std::cout << count << std::endl;
    }
}

# Python O(1) O(1) String
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: str = sys.stdin.readline().rstrip()
        sys.stdout.write(str(sum(n[idx] != 'codeforces'[idx] for idx in range(10))) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
