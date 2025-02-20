# A. Problem Generator
# time limit per test1 second
# memory limit per test256 megabytes
# Vlad is planning to hold m
#  rounds next month. Each round should contain one problem of difficulty levels 'A', 'B', 'C', 'D', 'E', 'F', and 'G'.
#
# Vlad already has a bank of n
#  problems, where the i
# -th problem has a difficulty level of ai
# . There may not be enough of these problems, so he may have to come up with a few more problems.
#
# Vlad wants to come up with as few problems as possible, so he asks you to find the minimum number of problems he needs to come up with in order to hold m
#  rounds.
#
# For example, if m=1
# , n=10
# , a=
#  'BGECDCBDED', then he needs to come up with two problems: one of difficulty level 'A' and one of difficulty level 'F'.
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and m
#  (1≤n≤50
# , 1≤m≤5
# ) — the number of problems in the bank and the number of upcoming rounds, respectively.
#
# The second line of each test case contains a string a
#  of n
#  characters from 'A' to 'G' — the difficulties of the problems in the bank.
#
# Output
# For each test case, output a single integer — the minimum number of problems that need to come up with to hold m
#  rounds.
#
# Example
# InputCopy
# 3
# 10 1
# BGECDCBDED
# 10 2
# BGECDCBDED
# 9 1
# BBCDEFFGG
# OutputCopy
# 2
# 5
# 1
# Solution
# C++ O(N) O(1) Counting
#include <iostream>
#include <vector>
#include <string>


void solution(int& t) {
    for (int i = 0; i < t; ++i) {
        int n, m;
        std::cin >> n >> m;
        std::string problems;
        std::cin >> problems;
        int totalFreq = 7 * m;
        std::vector<int> chunks(7, 0);
        for (char& ch : problems) {
            ++chunks[ch - 'A'];
        }
        for (int& freq : chunks) {
            totalFreq -= std::min(m, freq);
        }
        std::cout << totalFreq << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(N) O(1) Counting
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        problems: str = sys.stdin.readline().rstrip()
        total_freq: int = 7 * m
        chunks: list = [0] * 7
        for ch in problems:
            chunks[ord(ch) - 65] += 1
        for freq in chunks:
            total_freq -= min(freq, m)
        sys.stdout.write(str(total_freq) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)