# B. Lecture
# time limit per test1 second
# memory limit per test256 megabytes
# You have a new professor of graph theory and he speaks very quickly. You come up with the following plan to keep up with his lecture and make notes.
#
# You know two languages, and the professor is giving the lecture in the first one. The words in both languages consist of lowercase English characters, each language consists of several words. For each language, all words are distinct, i.e. they are spelled differently. Moreover, the words of these languages have a one-to-one correspondence, that is, for each word in each language, there exists exactly one word in the other language having has the same meaning.
#
# You can write down every word the professor says in either the first language or the second language. Of course, during the lecture you write down each word in the language in which the word is shorter. In case of equal lengths of the corresponding words you prefer the word of the first language.
#
# You are given the text of the lecture the professor is going to read. Find out how the lecture will be recorded in your notes.
#
# Input
# The first line contains two integers, n and m (1 ≤ n ≤ 3000, 1 ≤ m ≤ 3000) — the number of words in the professor's lecture and the number of words in each of these languages.
#
# The following m lines contain the words. The i-th line contains two strings ai, bi meaning that the word ai belongs to the first language, the word bi belongs to the second language, and these two words have the same meaning. It is guaranteed that no word occurs in both languages, and each word occurs in its language exactly once.
#
# The next line contains n space-separated strings c1, c2, ..., cn — the text of the lecture. It is guaranteed that each of the strings ci belongs to the set of strings {a1, a2, ... am}.
#
# All the strings in the input are non-empty, each consisting of no more than 10 lowercase English letters.
#
# Output
# Output exactly n words: how you will record the lecture in your notebook. Output the words of the lecture in the same order as in the input.
#
# Examples
# InputCopy
# 4 3
# codeforces codesecrof
# contest round
# letter message
# codeforces contest letter contest
# OutputCopy
# codeforces round letter round
# InputCopy
# 5 3
# joll wuqrd
# euzf un
# hbnyiyc rsoqqveh
# hbnyiyc joll joll euzf joll
# OutputCopy
# hbnyiyc joll joll un joll
# Solution
# C++ O(N) O(N) HashMap
#include <iostream>
#include <string>
#include <unordered_map>


void solution() {
    int n, m;
    std::cin >> n >> m;
    std::unordered_map<std::string, std::string> hashmap;
    for (int i = 0; i < m; ++i) {
        std::string x, y;
        std::cin >> x >> y;
        hashmap[x] = y;
    }
    for (int i = 0; i < n; ++i) {
        std::string c;
        std::cin >> c;
        std::string output = hashmap[c];
        if (c.size() <= hashmap[c].size()) {
            output = c;
        }
        if (i) {
            std::cout << " ";
        }
        std::cout << output;
    }
}


int main() {
    solution();
}

# Python O(N) O(N) HashMap
from __future__ import annotations
import sys


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    hashmap: dict[str, str] = dict()
    for _ in range(m):
        x, y = sys.stdin.readline().rstrip().split()
        hashmap[x] = y
    words: list[str] = sys.stdin.readline().rstrip().split()
    for i in range(n):
        output: str = words[i]
        if len(hashmap[words[i]]) < len(output):
            output = hashmap[words[i]]
        if i:
            sys.stdout.write(' ')
        sys.stdout.write(output)
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()