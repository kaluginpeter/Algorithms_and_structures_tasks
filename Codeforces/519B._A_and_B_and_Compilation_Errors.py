# B. A and B and Compilation Errors
# time limit per test2 seconds
# memory limit per test256 megabytes
# A and B are preparing themselves for programming contests.
#
# B loves to debug his code. But before he runs the solution and starts debugging, he has to first compile the code.
#
# Initially, the compiler displayed n compilation errors, each of them is represented as a positive integer. After some effort, B managed to fix some mistake and then another one mistake.
#
# However, despite the fact that B is sure that he corrected the two errors, he can not understand exactly what compilation errors disappeared — the compiler of the language which B uses shows errors in the new order every time! B is sure that unlike many other programming languages, compilation errors for his programming language do not depend on each other, that is, if you correct one error, the set of other error does not change.
#
# Can you help B find out exactly what two errors he corrected?
#
# Input
# The first line of the input contains integer n (3 ≤ n ≤ 105) — the initial number of compilation errors.
#
# The second line contains n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109) — the errors the compiler displayed for the first time.
#
# The third line contains n - 1 space-separated integers b1, b2, ..., bn - 1 — the errors displayed at the second compilation. It is guaranteed that the sequence in the third line contains all numbers of the second string except for exactly one.
#
# The fourth line contains n - 2 space-separated integers с1, с2, ..., сn - 2 — the errors displayed at the third compilation. It is guaranteed that the sequence in the fourth line contains all numbers of the third line except for exactly one.
#
# Output
# Print two numbers on a single line: the numbers of the compilation errors that disappeared after B made the first and the second correction, respectively.
#
# Examples
# InputCopy
# 5
# 1 5 8 123 7
# 123 7 5 1
# 5 1 7
# OutputCopy
# 8
# 123
# InputCopy
# 6
# 1 4 3 3 5 7
# 3 7 5 4 3
# 4 3 7 5
# OutputCopy
# 1
# 3
# Note
# In the first test sample B first corrects the error number 8, then the error number 123.
#
# In the second test sample B first corrects the error number 1, then the error number 3. Note that if there are multiple errors with the same number, B can correct only one of them in one step.
# Solution
# Python O(NlogN) O(1) Sorting Greedy
from __future__ import annotations
import sys


def solution(n: int, first: list[int], second: list[int], third: list[int]) -> None:
    i: int = 0
    while i < len(second) and first[i] == second[i]:
        i += 1
    sys.stdout.write(f'{first[i]}\n')
    j: int = 0
    while j < len(third) and second[j] == third[j]:
        j += 1
    sys.stdout.write(f'{second[j]}\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    first: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    second: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    third: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, first, second, third)

# C++ O(NlogN) O(1) Sorting Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> first(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> first[i];
    }
    std::vector<int> second(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        std::cin >> second[i];
    }
    std::vector<int> third(n - 2);
    for (int i = 0; i < n - 2; ++i) {
        std::cin >> third[i];
    }
    std::sort(first.begin(), first.end());
    std::sort(second.begin(), second.end());
    std::sort(third.begin(), third.end());
    int i = 0;
    while (i < n - 1 && first[i] == second[i]) {
        ++i;
    }
    std::cout << first[i] << "\n";
    int j = 0;
    while (j < n - 2 && second[j] == third[j]) {
        ++j;
    }
    std::cout << second[j] << "\n";
}


int main() {
    solution();
}