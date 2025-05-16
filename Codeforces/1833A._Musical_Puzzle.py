# A. Musical Puzzle
# time limit per test1 second
# memory limit per test256 megabytes
# Vlad decided to compose a melody on his guitar. Let's represent the melody as a sequence of notes corresponding to the characters 'a', 'b', 'c', 'd', 'e', 'f', and 'g'.
#
# However, Vlad is not very experienced in playing the guitar and can only record exactly two notes at a time. Vlad wants to obtain the melody s
# , and to do this, he can merge the recorded melodies together. In this case, the last sound of the first melody must match the first sound of the second melody.
#
# For example, if Vlad recorded the melodies "ab" and "ba", he can merge them together and obtain the melody "aba", and then merge the result with "ab" to get "abab".
#
# Help Vlad determine the minimum number of melodies consisting of two notes that he needs to record in order to obtain the melody s
# .
#
# Input
# The first line of input contains an integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Following that are the descriptions of the test cases.
#
# The first line of each test case contains an integer n
#  (2≤n≤50
# ) — the length of the melody s
# .
#
# The second line of each test case contains a string s
#  of length n
# , consisting of characters 'a', 'b', 'c', 'd', 'e', 'f', 'g'.
#
# Output
# Output t
#  integers, each representing the answer for the corresponding test case. As the answer output minimum number of melodies consisting of two notes that Vlad needs to record.
#
# Example
# InputCopy
# 5
# 4
# abab
# 7
# abacaba
# 6
# aaaaaa
# 7
# abcdefg
# 5
# babdd
# OutputCopy
# 2
# 4
# 1
# 6
# 4
# Note
# In the first sample, you need to record the melodies "ab" and "ba", as described in the problem statement.
#
# In the second sample, you need to record the melodies "ab", "ba", "ac", and "ca".
#
# In the third sample, the only necessary melody is "aa".
# Solution
# C++ O(N) O(N) String HashSet
#include <iostream>
#include <string>
#include <unordered_set>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::string notes;
        std::cin >> notes;
        std::unordered_set<std::string> seen;
        seen.insert(notes.substr(0, 2));
        int differ = 1;
        int idx = 1;
        while (idx + 1 < n) {
            if (seen.count(notes.substr(idx, 2))) ++idx;
            else {
                seen.insert(notes.substr(idx, 2));
                ++differ;
                ++idx;
            }
        }
        std::printf("%d\n", differ);
    }
}


int main() {
    solution();
}

# Python O(N) O(N) HashSet String
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        notes: str = sys.stdin.readline().rstrip()
        seen: set[str] = set()
        seen.add(notes[:2])
        differ: int = 1
        idx: int = 1
        while idx + 1 < n:
            if notes[idx:idx + 2] in seen: idx += 1
            else:
                differ += 1
                seen.add(notes[idx:idx + 2])
                idx += 1
        sys.stdout.write('{}\n'.format(differ))


if __name__ == '__main__':
    solution()