# A. Square String?
# time limit per test1 second
# memory limit per test256 megabytes
# A string is called square if it is some string written twice in a row. For example, the strings "aa", "abcabc", "abab" and "baabaa" are square. But the strings "aaa", "abaaab" and "abcdabc" are not square.
#
# For a given string s
#  determine if it is square.
#
# Input
# The first line of input data contains an integer t
#  (1≤t≤100
# ) —the number of test cases.
#
# This is followed by t
#  lines, each containing a description of one test case. The given strings consist only of lowercase Latin letters and have lengths between 1
#  and 100
#  inclusive.
#
# Output
# For each test case, output on a separate line:
#
# YES if the string in the corresponding test case is square,
# NO otherwise.
# You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as a positive response).
#
# Example
# inputCopy
# 10
# a
# aa
# aaa
# aaaa
# abab
# abcabc
# abacaba
# xxyy
# xyyx
# xyxy
# outputCopy
# NO
# YES
# NO
# YES
# YES
# YES
# NO
# NO
# NO
# YES
# Solution
# Python O(N) O(1) Math String
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: str = sys.stdin.readline().rstrip()
        if len(n) & 1: sys.stdout.write('NO' + '\n')
        else: sys.stdout.write(['NO', 'YES'][n[:len(n) // 2] == n[len(n) // 2:]] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(N) O(1) String Math
#include <iostream>
#include <string>

int main() {
    size_t t;
    std::cin >> t;
    for (size_t time = 0; time < t; ++time) {
        std::string n;
        std::cin >> n;
        if (n.size() % 2 != 0) {
            std::cout << "NO" << std::endl;
            continue;
        }
        std::cout << (n.substr(0, n.size() / 2) == n.substr(n.size() / 2, n.size())? "YES" : "NO") << std::endl;
    }
}