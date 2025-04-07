# A. Cipher Shifer
# time limit per test1 second
# memory limit per test256 megabytes
# There is a string a
#  (unknown to you), consisting of lowercase Latin letters, encrypted according to the following rule into string s
# :
#
# after each character of string a
# , an arbitrary (possibly zero) number of any lowercase Latin letters, different from the character itself, is added;
# after each such addition, the character that we supplemented is added.
# You are given string s
# , and you need to output the initial string a
# . In other words, you need to decrypt string s
# .
#
# Note that each string encrypted in this way is decrypted uniquely.
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The descriptions of the test cases follow.
#
# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the length of the encrypted message.
#
# The second line of each test case contains a string s
#  of length n
#  — the encrypted message obtained from some string a
# .
#
# Output
# For each test case, output the decrypted message a
#  on a separate line.
#
# Example
# InputCopy
# 3
# 8
# abacabac
# 5
# qzxcq
# 20
# ccooddeeffoorrcceess
# OutputCopy
# ac
# q
# codeforces
# Note
# In the first encrypted message, the letter a
#  is encrypted as aba
# , and the letter c
#  is encrypted as cabac
# .
#
# In the second encrypted message, only one letter q
#  is encrypted as qzxcq
# .
#
# In the third encrypted message, zero characters are added to each letter.
# Solution
# C++ O(N) O(1) String Greedy TwoPointers
#include <iostream>
#include <string>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::string sequence;
        std::cin >> sequence;
        std::string output = "";
        int left = 0, right = left + 1;
        while (right < n) {
            while (right < n && sequence[left] != sequence[right]) ++right;
            output.push_back(sequence[left]);
            ++right;
            left = right;
            ++right;
        }
        std::cout << output << "\n";
    }
}


int main() {
    solution();
}

# Python O(N) O(1) String Greedy TwoPointers
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        sequence: str = sys.stdin.readline().rstrip()
        output: list[str] = []
        left: int = 0
        right: int = left + 1
        while right < n:
            while right < n and sequence[left] != sequence[right]: right += 1
            output.append(sequence[left])
            left, right = right + 1, right + 2
        sys.stdout.write('{}\n'.format(''.join(output)))


if __name__ == '__main__':
    solution()