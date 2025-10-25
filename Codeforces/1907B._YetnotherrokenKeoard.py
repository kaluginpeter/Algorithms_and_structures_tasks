# B. YetnotherrokenKeoard
# time limit per test1 second
# memory limit per test256 megabytes
# Polycarp has a problem — his laptop keyboard is broken.
#
# Now, when he presses the 'b' key, it acts like an unusual backspace: it deletes the last (rightmost) lowercase letter in the typed string. If there are no lowercase letters in the typed string, then the press is completely ignored.
#
# Similarly, when he presses the 'B' key, it deletes the last (rightmost) uppercase letter in the typed string. If there are no uppercase letters in the typed string, then the press is completely ignored.
#
# In both cases, the letters 'b' and 'B' are not added to the typed string when these keys are pressed.
#
# Consider an example where the sequence of key presses was "ARaBbbitBaby". In this case, the typed string will change as follows: "" →A
#  "A" →R
#  "AR" →a
#  "ARa" →B
#  "Aa" →b
#  "A" →b
#  "A" →i
#  "Ai" →t
#  "Ait" →B
#  "it" →a
#  "ita" →b
#  "it" →y
#  "ity".
#
# Given a sequence of pressed keys, output the typed string after processing all key presses.
#
# Input
# The first line of the input data contains an integer t
#  (1≤t≤1000
# ), the number of test cases in the test.
#
# The following contains t
#  non-empty lines, which consist of lowercase and uppercase letters of the Latin alphabet.
#
# It is guaranteed that each line contains at least one letter and the sum of the lengths of the lines does not exceed 106
# .
#
# Output
# For each test case, output the result of processing the key presses on a separate line. If the typed string is empty, then output an empty line.
#
# Example
# InputCopy
# 12
# ARaBbbitBaby
# YetAnotherBrokenKeyboard
# Bubble
# Improbable
# abbreviable
# BbBB
# BusyasaBeeinaBedofBloomingBlossoms
# CoDEBARbIES
# codeforces
# bobebobbes
# b
# TheBBlackbboard
# OutputCopy
# ity
# YetnotherrokenKeoard
# le
# Imprle
# revile
#
# usyasaeeinaedofloominglossoms
# CDARIES
# codeforces
# es
#
# helaoard
# Solution
# C++ O(N) O(N) String
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>


void solution() {
    std::string moves;
    std::cin >> moves;
    std::unordered_set<int> hashset;
    std::vector<std::pair<char, int>> lower, upper;
    for (int i = 0; i < moves.size(); ++i) {
        if (moves[i] == 'b') {
            hashset.insert(i);
            if (!lower.empty()) {
                hashset.insert(lower.back().second);
                lower.pop_back();
            }
        } else if (moves[i] == 'B') {
            hashset.insert(i);
            if (!upper.empty()) {
                hashset.insert(upper.back().second);
                upper.pop_back();
            }
        } else {
            if (std::isupper(moves[i])) upper.push_back({moves[i], i});
            else lower.push_back({moves[i], i});
        }
    }
    std::string output = "";
    for (int i = 0; i < moves.size(); ++i) {
        if (!hashset.count(i)) output.push_back(moves[i]);
    }
    std::cout << output << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(N) String
import sys


def solution() -> None:
    moves: str = sys.stdin.readline().rstrip()
    upper: list[i] = []
    lower: list[int] = []
    hashset: set[int] = set()
    for i in range(len(moves)):
        if moves[i] in 'bB':
            hashset.add(i)
            if moves[i].isupper():
                if upper: hashset.add(upper.pop())
            if moves[i].islower():
                if lower: hashset.add(lower.pop())
        elif moves[i].isupper(): upper.append(i)
        else: lower.append(i)
    output: list[str] = []
    for i in range(len(moves)):
        if i not in hashset:
            output.append(moves[i])
    sys.stdout.write('{}\n'.format(''.join(output)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()