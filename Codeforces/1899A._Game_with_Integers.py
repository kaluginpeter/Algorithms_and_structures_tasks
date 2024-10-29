# A. Game with Integers
# time limit per test1 second
# memory limit per test256 megabytes
# Vanya and Vova are playing a game. Players are given an integer n
# . On their turn, the player can add 1
#  to the current integer or subtract 1
# . The players take turns; Vanya starts. If after Vanya's move the integer is divisible by 3
# , then he wins. If 10
#  moves have passed and Vanya has not won, then Vova wins.
#
# Write a program that, based on the integer n
# , determines who will win if both players play optimally.
#
# Input
# The first line contains the integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# The single line of each test case contains the integer n
#  (1≤n≤1000
# ).
#
# Output
# For each test case, print "First" without quotes if Vanya wins, and "Second" without quotes if Vova wins.
#
# Example
# InputCopy
# 6
# 1
# 3
# 5
# 100
# 999
# 1000
# OutputCopy
# First
# Second
# First
# First
# Second
# First
# Solution
# C++ O(1) O(1) Math
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::cout << (n % 3 == 0 ? "Second" : "First") << std::endl;
    }
}

# C++ O(1) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        sys.stdout.write(['First', 'Second'][n % 3 == 0] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
