# A. Homework
# time limit per test1 second
# memory limit per test256 megabytes
# Vlad and Dima have been assigned a task in school for their English class. They were given two strings a
#  and b
#  and asked to append all characters from b
#  to string a
#  in any order. The guys decided to divide the work between themselves and, after lengthy negotiations, determined who would add each character from string b
#  to a
# .
#
# Due to his peculiarities, Vlad can only add characters to the beginning of the word, while Dima can only add them to the end. They add characters in the order they appear in string b
# . Your task is to determine what string Vlad and Dima will end up with.
#
# Input
# Each test consists of several test cases. The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases. The description of the test cases follows.
#
# The first line contains an integer n
#  (1≤n≤10
# ) — the length of the string a
# .
#
# The second line contains the string a
# , consisting of lowercase letters of the English alphabet.
#
# The third line contains an integer m
#  (1≤m≤10
# ) — the length of the strings b
#  and c
# .
#
# The fourth line contains the string b
# , consisting of lowercase letters of the English alphabet.
#
# The fifth line contains the string c
# , consisting of the characters 'V' and 'D' — the distribution of the characters of string b
#  between Dima and Vlad. If ci
#  = 'V', then the i
# -th letter is added by Vlad; otherwise, it is added by Dima.
#
# Output
# For each test case, output the string that will result from Dima and Vlad's work.
#
# Example
# InputCopy
# 4
# 2
# ot
# 2
# ad
# DV
# 3
# efo
# 7
# rdcoecs
# DVDVDVD
# 3
# aca
# 4
# bbaa
# DVDV
# 3
# biz
# 4
# abon
# VVDD
# OutputCopy
# dota
# codeforces
# abacaba
# babizon
# Note
# In the first test case, there is initially a string ot
# . Then Dima appends the character a
#  to the end of the string, resulting in ota
# , and Vlad appends the last character, resulting in dota
# .
#
# In the second test case, the string will change as follows: efo→efor→defor→deforc→odeforc→odeforce→codeforce→codeforces
#
# In the third test case: aca→acab→bacab→bacaba→abacaba
#
# In the fourth test case: biz→abiz→babiz→babizo→babizon
# Solution
# C++ O(N + M) O(M) String
#include <iostream>
#include <string>
#include <algorithm>


void solution() {
    size_t n, m;
    std::string N, M, path;
    std::cin >> n >> N >> m >> M >> path;
    std::string prefix = "";
    for (size_t i = 0; i < path.size(); ++i) {
        if (path[i] == 'V') prefix.push_back(M[i]);
        else N.push_back(M[i]);
    }
    std::reverse(prefix.begin(), prefix.end());
    std::cout << prefix << N << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N + M) O(M) String
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    N: list[str] = list(sys.stdin.readline().rstrip())
    m: int = int(sys.stdin.readline().rstrip())
    M: str = sys.stdin.readline().rstrip()
    path: str = sys.stdin.readline().rstrip()
    prefix: list[str] = []
    for i in range(m):
        if path[i] == 'V': prefix.append(M[i])
        else: N.append(M[i])
    sys.stdout.write('{}{}\n'.format(''.join(reversed(prefix)), ''.join(N)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()