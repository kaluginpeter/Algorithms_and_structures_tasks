# A. Elections
# time limit per test1 second
# memory limit per test256 megabytes
# The elections in which three candidates participated have recently ended. The first candidate received a
#  votes, the second one received b
#  votes, the third one received c
#  votes. For each candidate, solve the following problem: how many votes should be added to this candidate so that he wins the election (i.e. the number of votes for this candidate was strictly greater than the number of votes for any other candidate)?
#
# Please note that for each candidate it is necessary to solve this problem independently, i.e. the added votes for any candidate do not affect the calculations when getting the answer for the other two candidates.
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases. Then t
#  test cases follow.
#
# Each test case consists of one line containing three integers a
# , b
# , and c
#  (0≤a,b,c≤109
# ).
#
# Output
# For each test case, output in a separate line three integers A
# , B
# , and C
#  (A,B,C≥0
# ) separated by spaces — the answers to the problem for the first, second, and third candidate, respectively.
#
# Example
# InputCopy
# 5
# 0 0 0
# 10 75 15
# 13 13 17
# 1000 0 0
# 0 1000000000 0
# OutputCopy
# 1 1 1
# 66 0 61
# 5 5 0
# 0 1001 1001
# 1000000001 0 1000000001
# Solution
# C++ O(1) O(1) Math Greedy
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int a, b, c;
        std::cin >> a >> b >> c;
        if (a > std::max(b, c)) std::cout << "0 ";
        else std::cout << std::max(b, c) - a + 1<< " ";
        if (b > std::max(a, c)) std::cout << "0 ";
        else std::cout << std::max(a, c) - b + 1 << " ";
        if (c > std::max(a, b)) std::cout << "0\n";
        else std::cout << std::max(a, b) - c + 1 << "\n";
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        if a > max(b, c): sys.stdout.write('0 ')
        else: sys.stdout.write(f'{max(b, c) - a + 1} ')
        if b > max(a, c): sys.stdout.write('0 ')
        else: sys.stdout.write(f'{max(a, c) - b + 1} ')
        if c > max(a, b): sys.stdout.write('0\n')
        else: sys.stdout.write(f'{max(a, b) - c + 1}\n')


if __name__ == '__main__':
    solution()
