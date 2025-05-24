# A. Line Breaks
# time limit per test1 second
# memory limit per test256 megabytes
# Kostya has a text s
#  consisting of n
#  words made up of Latin alphabet letters. He also has two strips on which he must write the text. The first strip can hold m
#  characters, while the second can hold as many as needed.
#
# Kostya must choose a number x
#  and write the first x
#  words from s
#  on the first strip, while all the remaining words are written on the second strip. To save space, the words are written without gaps, but each word must be entirely on one strip.
#
# Since space on the second strip is very valuable, Kostya asks you to choose the maximum possible number x
#  such that all words s1,s2,…,sx
#  fit on the first strip of length m
# .
#
# Input
# The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and m
#  (1≤n≤50
# ; 1≤m≤500
# ) — the number of words in the list and the maximum number of characters that can be on the first strip.
#
# The next n
#  lines contain one word si
#  of lowercase Latin letters, where the length of si
#  does not exceed 10
# .
#
# Output
# For each test case, output the maximum number of words x
#  such that the first x
#  words have a total length of no more than m
# .
#
# Example
# InputCopy
# 5
# 3 1
# a
# b
# c
# 2 9
# alpha
# beta
# 4 12
# hello
# world
# and
# codeforces
# 3 2
# ab
# c
# d
# 3 2
# abc
# ab
# a
# OutputCopy
# 1
# 2
# 2
# 1
# 0
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, m;
        std::scanf("%d %d", &n, &m);
        int words = 0, totalLength = 0;
        for (int j = 0; j < n; ++j) {
            std::string word;
            std::cin >> word;
            totalLength += word.size();
            if (totalLength <= m) ++words;
        }
        std::printf("%d\n", words);
    }
}


int main() {
    solution();
}
# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        total_length: int = 0
        valid: int = 0
        for i in range(n):
            word: str = sys.stdin.readline().rstrip()
            total_length  += len(word)
            if total_length <= m: valid += 1
        sys.stdout.write('{}\n'.format(valid))


if __name__ == '__main__':
    solution()