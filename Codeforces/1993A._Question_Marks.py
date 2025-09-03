# A. Question Marks
# time limit per test1 second
# memory limit per test256 megabytes
# Tim is doing a test consisting of 4n
#  questions; each question has 4
#  options: 'A', 'B', 'C', and 'D'. For each option, there are exactly n
#  correct answers corresponding to that option — meaning there are n
#  questions with the answer 'A', n
#  questions with the answer 'B', n
#  questions with the answer 'C', and n
#  questions with the answer 'D'.
#
# For each question, Tim wrote his answer on the answer sheet. If he could not figure out the answer, he would leave a question mark '?' for that question.
#
# You are given his answer sheet of 4n
#  characters. What is the maximum number of correct answers Tim can get?
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains an integer n
#  (1≤n≤100
# ).
#
# The second line of each test case contains a string s
#  of 4n
#  characters (si∈{A,B,C,D,?}
# ) — Tim's answers for the questions.
#
# Output
# For each test case, print a single integer — the maximum score that Tim can achieve.
#
# Example
# InputCopy
# 6
# 1
# ABCD
# 2
# AAAAAAAA
# 2
# AAAABBBB
# 2
# ????????
# 3
# ABCABCABCABC
# 5
# ACADC??ACAC?DCAABC?C
# OutputCopy
# 4
# 2
# 4
# 0
# 9
# 13
# Note
# In the first test case, there is exactly one question with each answer 'A', 'B', 'C', and 'D'; so it's possible that Tim gets all his answers correct.
#
# In the second test case, there are only two correct answers 'A' which makes him get exactly 2
#  points in any case.
#
# In the third test case, Tim can get at most 2
#  correct answers with option 'A' and 2
#  correct answers with option 'B'. For example, he would get 4
#  points if the answers were 'AACCBBDD'.
#
# In the fourth test case, he refuses to answer any question at all, which makes him get 0
#  points.
# Solution
# C++ O(N) O(1) String
#include <iostream>
#include <string>


void solution() {
    int n;
    std::cin >> n;
    std::string pattern;
    std::cin >> pattern;
    int a = 0, b = 0, c = 0, d = 0;
    for (const char &ch : pattern) {
        if (ch == '?') continue;
        else if (ch == 'A') ++a;
        else if (ch == 'B') ++b;
        else if (ch == 'C') ++c;
        else ++d;
    }
    std::cout << (std::min(a, n) + std::min(b, n) + std::min(c, n) + std::min(d, n)) << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) String
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    pattern: str = sys.stdin.readline().rstrip()
    a: int = 0
    b: int = 0
    c_: int = 0
    d: int = 0
    for c in pattern:
        if c == '?': continue
        elif c == 'A': a += 1
        elif c == 'B': b += 1
        elif c == 'C': c_ += 1
        else: d += 1
    sys.stdout.write('{}\n'.format(min(a, n) + min(b, n) + min(c_, n) + min(d, n)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()