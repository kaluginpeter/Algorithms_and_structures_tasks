# A. Two Substrings
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given string s. Your task is to determine if the given string s contains two non-overlapping substrings "AB" and "BA" (the substrings can go in any order).
#
# Input
# The only line of input contains a string s of length between 1 and 105 consisting of uppercase Latin letters.
#
# Output
# Print "YES" (without the quotes), if string s contains two non-overlapping substrings "AB" and "BA", and "NO" otherwise.
#
# Examples
# InputCopy
# ABA
# OutputCopy
# NO
# InputCopy
# BACFAB
# OutputCopy
# YES
# InputCopy
# AXBYBXA
# OutputCopy
# NO
# Note
# In the first sample test, despite the fact that there are substrings "AB" and "BA", their occurrences overlap, so the answer is "NO".
#
# In the second sample test there are the following occurrences of the substrings: BACFAB.
#
# In the third sample test there is no substring "AB" nor substring "BA".
# Solution
# C++ O(N) O(1) String
#include <bits/stdc++.h>


void solution() {
    std::string pattern;
    std::cin >> pattern;
    std::string x = "AB";
    std::string y = "BA";
    std::cout << (
        (
            (pattern.find(x) != std::string::npos && pattern.find(y, pattern.find(x) + 2) != std::string::npos)
            || (pattern.find(y) != std::string::npos && pattern.find(x, pattern.find(y) + 2) != std::string::npos)
        )? "YES" : "NO"
    ) << "\n";
}


int main() {
    solution();
}

# Python O(N) O(1) String
import sys

def solution() -> None:
    pattern: str = sys.stdin.readline().rstrip()
    x: str = 'AB'
    y: str = 'BA'
    sys.stdout.write(['NO', 'YES'][
        (x in pattern and y in pattern[pattern.index(x) + 2:])
        or (y in pattern and x in pattern[pattern.index(y) + 2:])
    ] + '\n')

if __name__ == '__main__':
    solution()