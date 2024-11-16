# B. Atilla's Favorite Problem
# time limit per test1 second
# memory limit per test256 megabytes
# In order to write a string, Atilla needs to first learn all letters that are contained in the string.
#
# Atilla needs to write a message which can be represented as a string s
# . He asks you what is the minimum alphabet size required so that one can write this message.
#
# The alphabet of size x
#  (1≤x≤26
# ) contains only the first x
#  Latin letters. For example an alphabet of size 4
#  contains only the characters a
# , b
# , c
#  and d
# .
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤100
# ) — the length of the string.
#
# The second line of each test case contains a string s
#  of length n
# , consisting of lowercase Latin letters.
#
# Output
# For each test case, output a single integer — the minimum alphabet size required to so that Atilla can write his message s
# .
#
# Example
# InputCopy
# 5
# 1
# a
# 4
# down
# 10
# codeforces
# 3
# bcf
# 5
# zzzzz
# OutputCopy
# 1
# 23
# 19
# 6
# 26
# Note
# For the first test case, Atilla needs to know only the character a
# , so the alphabet of size 1
#  which only contains a
#  is enough.
#
# For the second test case, Atilla needs to know the characters d
# , o
# , w
# , n
# . The smallest alphabet size that contains all of them is 23
#  (such alphabet can be represented as the string abcdefghijklmnopqrstuvw
# ).
# Solution
# C++ O(N) O(1) String
#include <iostream>
#include <string>


int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::string letters;
        std::cin >> letters;
        int maxChar = 0;
        for (char letter : letters) {
            if (letter - 'a' > maxChar) {
                maxChar = letter - 'a';
            }
        }
        std::cout << maxChar + 1 << "\n";
    }
}

# Python O(N) O(1) String
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        letters: str = sys.stdin.readline().rstrip()
        max_char: int = 0
        for letter in letters:
            max_char = max(max_char, ord(letter) - 96)
        sys.stdout.write(str(max_char) + '\n')

if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
