# A. Trippi Troppi
# time limit per test1 second
# memory limit per test256 megabytes
# Trippi Troppi resides in a strange world. The ancient name of each country consists of three strings. The first letter of each string is concatenated to form the country's modern name.
#
# Given the country's ancient name, please output the modern name.
#
# Input
# The first line contains an integer t
#  – the number of independent test cases (1≤t≤100
# ).
#
# The following t
#  lines each contain three space-separated strings. Each string has a length of no more than 10
# , and contains only lowercase Latin characters.
#
# Output
# For each test case, output the string formed by concatenating the first letter of each word.
#
# Example
# InputCopy
# 7
# united states america
# oh my god
# i cant lie
# binary indexed tree
# believe in yourself
# skibidi slay sigma
# god bless america
# OutputCopy
# usa
# omg
# icl
# bit
# biy
# sss
# gba
# Solution
# C++ O(N) O(1) String
#include <iostream>
#include <string>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        std::string word;
        std::cin >> word;
        std::cout << word[0];
        std::cin >> word;
        std::cout << word[0];
        std::cin >> word;
        std::cout << word[0] << "\n";
    }
}


int main() {
    solution();
}
# Python O(N) O(1) String
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        a, b, c = sys.stdin.readline().rstrip().split()
        sys.stdout.write('{}{}{}\n'.format(a[0], b[0], c[0]))


if __name__ == '__main__':
    solution()