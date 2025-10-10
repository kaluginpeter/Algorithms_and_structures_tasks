# B. Deck of Cards
# time limit per test2 seconds
# memory limit per test256 megabytes
# Monocarp has a deck of cards numbered from 1
#  to n
# . Initially, the cards are arranged from smallest to largest, with 1
#  on top and n
#  at the bottom.
#
# Monocarp performed k
#  actions on the deck. Each action was one of three types:
#
# remove the top card;
# remove the bottom card;
# remove either the top or bottom card.
# Your task is to determine the fate of each card: whether it remains in the deck, has been removed, or might be both.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤k≤n≤2⋅105
# ).
#
# The second line contains a string s
#  of length k
# , consisting of characters 0, 1, and/or {2}. This string describes Monocarp's actions. If the i
# -th character is 0, Monocarp removes the top card on the i
# -th action. If it's 1, he removes the bottom card. If it's 2, either the top or bottom card can be removed.
#
# Additional constraint on the input: the sum of n
#  over all test cases doesn't exceed 2⋅105
# .
#
# Output
# For each test case, print a string consisting of n
#  characters. The i
# -th character should be + (plus sign) if the i
# -th card is still in the deck, - (minus sign) if it has been removed, or ? (question mark) if its state is unknown.
#
# Example
# InputCopy
# 4
# 4 2
# 01
# 3 2
# 22
# 1 1
# 2
# 7 5
# 01201
# OutputCopy
# -++-
# ???
# -
# --?+?--
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    size_t n, k;
    std::cin >> n >> k;
    std::string moves = "";
    std::cin >> moves;
    int left = 1, right = n, extra = 0;
    for (char& ch : moves) {
        if (ch == '0') ++left;
        else if (ch == '1') --right;
        else ++extra;
    }
    for (size_t i = 1; i <= n; ++i) {
        if (i < left) std::cout << '-';
        else if (i > right) std::cout << '-';
        else if (left + extra > right) std::cout << '-';
        else if (left + extra > i || right - extra < i) std::cout << '?';
        else std::cout << '+';
    }
    std::cout << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    moves: str = sys.stdin.readline().rstrip()
    left: int = 1
    right: int = n
    extra: int = 0
    for m in moves:
        if m == '0': left += 1
        elif m == '1': right -= 1
        else: extra += 1
    for i in range(1, n + 1):
        if i < left or right < i or left + extra > right:
            sys.stdout.write('-')
        elif left + extra > i or right - extra < i:
            sys.stdout.write('?')
        else: sys.stdout.write('+')
    sys.stdout.write('\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()