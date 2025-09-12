# A. Special Characters
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an integer n
# .
#
# Your task is to build a string of uppercase Latin letters. There must be exactly n
#  special characters in this string. Let's call a character special if it is equal to exactly one of its neighbors.
#
# For example, there are 6
#  special characters in the AAABAACC string (at positions: 1
# , 3
# , 5
# , 6
# , 7
#  and 8
# ).
#
# Print any suitable string or report that there is no such string.
#
# Input
# The first line contains a single integer t
#  (1≤t≤50
# ) — the number of test cases.
#
# The only line of each test case contains a single integer n
#  (1≤n≤50
# ).
#
# Output
# For each test case, print the answer as follows:
#
# if there is no suitable string, print one line containing the string NO;
# otherwise, print two lines. The first line should contain the string YES; on the second line print a string of length at most 200
#  — the answer itself (it can be shown that if some answers exist, then there is an answer of length at most 200
# ). If there are several solutions, print any of them.
# Example
# InputCopy
# 3
# 6
# 1
# 2
# OutputCopy
# YES
# AAABAACC
# NO
# YES
# MM
# Solution
# C++ O(N) O(1) String
#include <iostream>


void solution() {
    int n;
    std::cin >> n;
    if (n & 1) {
        std::cout << "NO\n";
        return;
    }
    std::cout << "YES\n";
    char prev = 'A';
    while (n > 1) {
        std::cout << prev << prev;
        prev = ((prev - 'A') + 1) % 26 + 'A';
        n -= 2;
    }
    std::cout << std::endl;
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
    if n & 1:
        sys.stdout.write('NO\n')
        return
    sys.stdout.write('YES\n')
    prev: str = 'A'
    while n > 1:
        n -= 2
        sys.stdout.write('{}'.format(prev * 2))
        prev = chr((ord(prev) - 65 + 1) % 26 + 65)
    sys.stdout.write('\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()