# A. Spell Check
# time limit per test1 second
# memory limit per test256 megabytes
# Timur likes his name. As a spelling of his name, he allows any permutation of the letters of the name. For example, the following strings are valid spellings of his name: Timur, miurT, Trumi, mriTu. Note that the correct spelling must have uppercased T and lowercased other letters.
#
# Today he wrote string s
#  of length n
#  consisting only of uppercase or lowercase Latin letters. He asks you to check if s
#  is the correct spelling of his name.
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤103
# ) — the number of test cases.
#
# The first line of each test case contains an integer n
#  (1≤n≤10)
#  — the length of string s
# .
#
# The second line of each test case contains a string s
#  consisting of only uppercase or lowercase Latin characters.
#
# Output
# For each test case, output "YES" (without quotes) if s
#  satisfies the condition, and "NO" (without quotes) otherwise.
#
# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
#
# Example
# inputCopy
# 10
# 5
# Timur
# 5
# miurT
# 5
# Trumi
# 5
# mriTu
# 5
# timur
# 4
# Timr
# 6
# Timuur
# 10
# codeforces
# 10
# TimurTimur
# 5
# TIMUR
# outputCopy
# YES
# YES
# YES
# YES
# NO
# NO
# NO
# NO
# NO
# NO
# Solution
# Python O(NlogN) O(N)
import sys


def solution(t: int) -> None:
    valid: list = sorted('Timur')
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        word: str = sys.stdin.readline().rstrip()
        sys.stdout.write(['NO', 'YES'][valid == sorted(word)] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(NlogN) O(1)
#include <iostream>
#include <string>
#include <algorithm>

int main() {
    size_t t;
    std::cin >> t;
    std::string valid = "Timur";
    std::sort(valid.begin(), valid.end());
    for (size_t rep = 0; rep < t; ++rep) {
        int n;
        std::cin >> n;
        std::string name;
        std::cin >> name;
        std::sort(name.begin(), name.end());
        std::cout << (valid == name? "YES" : "NO") << std::endl;
    }
}