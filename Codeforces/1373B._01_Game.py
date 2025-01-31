# B. 01 Game
# time limit per test1 second
# memory limit per test256 megabytes
# Alica and Bob are playing a game.
#
# Initially they have a binary string s
#  consisting of only characters 0 and 1.
#
# Alice and Bob make alternating moves: Alice makes the first move, Bob makes the second move, Alice makes the third one, and so on. During each move, the current player must choose two different adjacent characters of string s
#  and delete them. For example, if s=1011001
#  then the following moves are possible:
#
# delete s1
#  and s2
# : 1011001→11001
# ;
# delete s2
#  and s3
# : 1011001→11001
# ;
# delete s4
#  and s5
# : 1011001→10101
# ;
# delete s6
#  and s7
# : 1011001→10110
# .
# If a player can't make any move, they lose. Both players play optimally. You have to determine if Alice can win.
#
# Input
# First line contains one integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Only line of each test case contains one string s
#  (1≤|s|≤100
# ), consisting of only characters 0 and 1.
#
# Output
# For each test case print answer in the single line.
#
# If Alice can win print DA (YES in Russian) in any register. Otherwise print NET (NO in Russian) in any register.
#
# Example
# InputCopy
# 3
# 01
# 1111
# 0011
# OutputCopy
# DA
# NET
# NET
# Note
# In the first test case after Alice's move string s
#  become empty and Bob can not make any move.
#
# In the second test case Alice can not make any move initially.
#
# In the third test case after Alice's move string s
#  turn into 01
# . Then, after Bob's move string s
#  become empty and Alice can not make any move.
# Solution
# C++ O(N) O(N) Stack String Greedy
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string moves;
        std::cin >> moves;
        std::stack<char> store;
        bool isAliceWin = false;
        for (char& ch : moves) {
            if (!store.size() || store.top() == ch) {
                store.push(ch);
            } else {
                store.pop();
                isAliceWin = !isAliceWin;
            }
        }
        std::cout << (isAliceWin? "DA" : "NET") << "\n";
    }
}


int main() {
    solution();
}

# Python O(N) O(N) Stack String Greedy
from __future__ import annotations
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        moves: str = sys.stdin.readline().rstrip()
        stack: list[str] = []
        is_alice_win: bool = False
        for ch in moves:
            if not stack or stack[-1] == ch: stack.append(ch)
            else:
                stack.pop()
                is_alice_win = not is_alice_win
        sys.stdout.write('{}\n'.format('DA' if is_alice_win else 'NET'))


if __name__ == '__main__':
    solution()
