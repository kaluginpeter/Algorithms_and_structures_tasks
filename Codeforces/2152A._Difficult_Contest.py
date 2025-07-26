# A. Difficult Contest
# time limit per test2 seconds
# memory limit per test256 megabytes
# It is known that a contest can be represented by a string s
# , consisting of uppercase Latin letters that denote problems. It is also known that a contest is difficult if it contains "FFT" or "NTT" as a contiguous substring.
#
# Your task is to rearrange the problem in contest s
#  in such a way that this contest is not difficult. If the initial contest is not difficult, you may leave it as it is.
#
# Input
# Each test consists of several test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The only line of each test case contains s
#  (1≤|s|≤2⋅105
# ).
#
# Additional constraints on the input data:
#
# the total length of strings across all test cases does not exceed 2⋅105
# .
# Output
# For each test case, output a string — a non-difficult contest that was obtained from s
#  by rearranging the letters.
#
# If there are multiple correct answers, you may output any. It can be shown that at least one correct answer always exists.
#
# Example
# InputCopy
# 5
# FFT
# ABFBANTTA
# FFTNTT
# FFTFFTFFTNNTNNT
# AFFTBFFNTTFTTZ
# OutputCopy
# FTF
# ABFBANATT
# NTFTFT
# TFFFFFFNTNTNTNT
# AFTFBTTFFNFTTZ
# Solution
# C++ O(N) O(1) TwoPointers
#include <iostream>
#include <string>


void solution() {
    std::string contest;
    std::cin >> contest;
    int left = 0, i = 0;
    while (i < contest.size()) {
        if (contest[i - 2] == 'F' && contest[i - 1] == 'F' && contest[i] == 'T') {
            std::swap(contest[left], contest[i]);
            ++left;
        } else if (contest[i - 2] == 'N' && contest[i - 1] == 'T' && contest[i] == 'T') {
            std::swap(contest[left], contest[i]);
            ++left;
        } else ++i;
    }
    std::cout << contest << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) TwoPointers
import sys


def solution() -> None:
    contest: list[str] = list(sys.stdin.readline().rstrip())
    left: int = 0
    i: int = 2
    while i < len(contest):
        if contest[i - 2] + contest[i - 1] + contest[i] in {"FFT", "NTT"}:
            contest[left], contest[i] = contest[i], contest[left]
            left += 1
        else: i += 1
    sys.stdout.write('{}\n'.format(''.join(contest)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()