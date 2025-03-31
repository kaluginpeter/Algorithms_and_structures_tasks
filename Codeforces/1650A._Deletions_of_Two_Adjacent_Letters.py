# A. Deletions of Two Adjacent Letters
# time limit per test2 seconds
# memory limit per test256 megabytes
# The string s
#  is given, the string length is odd number. The string consists of lowercase letters of the Latin alphabet.
#
# As long as the string length is greater than 1
# , the following operation can be performed on it: select any two adjacent letters in the string s
#  and delete them from the string. For example, from the string "lemma" in one operation, you can get any of the four strings: "mma", "lma", "lea" or "lem" In particular, in one operation, the length of the string reduces by 2
# .
#
# Formally, let the string s
#  have the form s=s1s2…sn
#  (n>1
# ). During one operation, you choose an arbitrary index i
#  (1≤i<n
# ) and replace s=s1s2…si−1si+2…sn
# .
#
# For the given string s
#  and the letter c
# , determine whether it is possible to make such a sequence of operations that in the end the equality s=c
#  will be true? In other words, is there such a sequence of operations that the process will end with a string of length 1
# , which consists of the letter c
# ?
#
# Input
# The first line of input data contains an integer t
#  (1≤t≤103
# ) — the number of input test cases.
#
# The descriptions of the t
#  cases follow. Each test case is represented by two lines:
#
# string s
# , which has an odd length from 1
#  to 49
#  inclusive and consists of lowercase letters of the Latin alphabet;
# is a string containing one letter c
# , where c
#  is a lowercase letter of the Latin alphabet.
# Output
# For each test case in a separate line output:
#
# YES, if the string s
#  can be converted so that s=c
#  is true;
# NO otherwise.
# You can output YES and NO in any case (for example, the strings yEs, yes, Yes and YES will be recognized as a positive response).
#
# Example
# InputCopy
# 5
# abcde
# c
# abcde
# b
# x
# y
# aaaaaaaaaaaaaaa
# a
# contest
# t
# OutputCopy
# YES
# NO
# NO
# YES
# YES
# Note
# In the first test case, s
# ="abcde". You need to get s
# ="c". For the first operation, delete the first two letters, we get s
# ="cde". In the second operation, we delete the last two letters, so we get the expected value of s
# ="c".
#
# In the third test case, s
# ="x", it is required to get s
# ="y". Obviously, this cannot be done.
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        std::string sequence;
        char target;
        std::cin >> sequence >> target;
        int n = sequence.size();
        bool isValid = false;
        for (int pos = 0; pos < n; ++pos) {
            if (sequence[pos] == target) {
                if (pos % 2 == 0 && (n - pos - 1) % 2 == 0) {
                    isValid = true;
                    break;
                }
            }
        }
        std::cout << (isValid? "YES" : "NO") << "\n";
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
        sequence: str = sys.stdin.readline().rstrip()
        target: str = sys.stdin.readline().rstrip()
        n: int = len(sequence)
        is_valid: bool = False
        for pos in range(n):
            if sequence[pos] == target:
                if not (pos & 1) and not ((n - pos - 1) & 1):
                    is_valid = True
                    break
        sys.stdout.write('{}\n'.format(['NO', 'YES'][is_valid]))


if __name__ == '__main__':
    solution()