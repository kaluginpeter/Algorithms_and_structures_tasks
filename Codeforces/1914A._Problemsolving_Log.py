# A. Problemsolving Log
# time limit per test2 seconds
# memory limit per test256 megabytes
# Monocarp is participating in a programming contest, which features 26
#  problems, named from 'A' to 'Z'. The problems are sorted by difficulty. Moreover, it's known that Monocarp can solve problem 'A' in 1
#  minute, problem 'B' in 2
#  minutes, ..., problem 'Z' in 26
#  minutes.
#
# After the contest, you discovered his contest log — a string, consisting of uppercase Latin letters, such that the i
# -th letter tells which problem Monocarp was solving during the i
# -th minute of the contest. If Monocarp had spent enough time in total on a problem to solve it, he solved it. Note that Monocarp could have been thinking about a problem after solving it.
#
# Given Monocarp's contest log, calculate the number of problems he solved during the contest.
#
# Input
# The first line contains a single integer t
#  (1≤t≤100
# ) — the number of testcases.
#
# The first line of each testcase contains a single integer n
#  (1≤n≤500
# ) — the duration of the contest, in minutes.
#
# The second line contains a string of length exactly n
# , consisting only of uppercase Latin letters, — Monocarp's contest log.
#
# Output
# For each testcase, print a single integer — the number of problems Monocarp solved during the contest.
#
# Example
# InputCopy
# 3
# 6
# ACBCBC
# 7
# AAAAFPC
# 22
# FEADBBDFFEDFFFDHHHADCC
# OutputCopy
# 3
# 1
# 4
# Solution
# C++ O(N) O(D) HashMap
#include <iostream>
#include <string>
#include <vector>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::string contest;
        std::cin >> contest;
        std::vector<int> count(26, 0);
        for (char c : contest) ++count[c - 'A'];
        int solved = 0;
        for (int i = 0; i < 26; ++i) {
            if (count[i] >= (i + 1)) ++solved;
        }
        std::printf("%d\n", solved);
    }
}


int main() {
    solution();
}

# Python O(N) O(D) HashMap
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        contest: str = sys.stdin.readline().rstrip()
        hashmap: list[int] = [0] * 26
        for problem in contest: hashmap[ord(problem) - 65] += 1
        solved: int = 0
        for problem in range(26):
            if hashmap[problem] >= (problem + 1): solved += 1
        sys.stdout.write('{}\n'.format(solved))


if __name__ == '__main__':
    solution()