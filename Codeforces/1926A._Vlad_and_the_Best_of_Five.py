# A. Vlad and the Best of Five
# time limit per test1 second
# memory limit per test256 megabytes
# Vladislav has a string of length 5
# , whose characters are each either A
#  or B
# .
#
# Which letter appears most frequently: A
#  or B
# ?
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤32
# ) — the number of test cases.
#
# The only line of each test case contains a string of length 5
#  consisting of letters A
#  and B
# .
#
# All t
#  strings in a test are different (distinct).
#
# Output
# For each test case, output one letter (A
#  or B
# ) denoting the character that appears most frequently in the string.
#
# Example
# inputCopy
# 8
# ABABB
# ABABA
# BBBAB
# AAAAA
# BBBBB
# BABAA
# AAAAB
# BAAAA
# outputCopy
# B
# A
# B
# A
# B
# A
# A
# A
# Solution
# C++ O(N) O(1) String
#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string n;
        std::cin >> n;
        int A = 0;
        int B = 0;
        for (char letter : n) {
            if (letter == 'A') {
                ++A;
            } else {
                ++B;
            }
        }
        std::cout << (A > B ? "A" : "B") << std::endl;
    }
}

# Python O(N) O(1) String
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: str = sys.stdin.readline().rstrip()
        sys.stdout.write(['B', 'A'][n.count('A') > n.count('B')] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
