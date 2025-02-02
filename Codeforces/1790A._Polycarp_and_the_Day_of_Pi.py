# A. Polycarp and the Day of Pi
# time limit per test1 second
# memory limit per test256 megabytes
# On March 14, the day of the number π
#  is celebrated all over the world. This is a very important mathematical constant equal to the ratio of the circumference of a circle to its diameter.
#
# Polycarp was told at school that the number π
#  is irrational, therefore it has an infinite number of digits in decimal notation. He wanted to prepare for the Day of the number π
#  by memorizing this number as accurately as possible.
#
# Polycarp wrote out all the digits that he managed to remember. For example, if Polycarp remembered π
#  as 3.1415
# , he wrote out 31415.
#
# Polycarp was in a hurry and could have made a mistake, so you decided to check how many first digits of the number π
#  Polycarp actually remembers correctly.
#
# Input
# The first line of the input data contains the single integer t
#  (1≤t≤103
# ) — the number of test cases in the test.
#
# Each test case is described by a single string of digits n
# , which was written out by Polycarp.
#
# The string n
#  contains up to 30
#  digits.
#
# Output
# Output t
#  integers, each of which is the answer to the corresponding test case, that is how many first digits of the number π
#  Polycarp remembers correctly.
#
# Example
# InputCopy
# 9
# 000
# 3
# 4141592653
# 141592653589793238462643383279
# 31420
# 31415
# 314159265358
# 27182
# 314159265358979323846264338327
# OutputCopy
# 0
# 1
# 0
# 0
# 3
# 5
# 12
# 0
# 30
# Solution
# C++ O(N) O(1) String
#include <bits/stdc++.h>


void solution() {
    std::string pi = "314159265358979323846264338327";
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::string digits;
        std::cin >> digits;
        int idx = 0;
        while (idx < std::min(30, (int)digits.size()) && pi[idx] == digits[idx]) {
            ++idx;
        }
        std::cout << idx << "\n";
    }
}


int main() {
    solution();
}

# Python O(N) O(1) String
import sys


def solution() -> None:
    pi: str = '314159265358979323846264338327'
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        stock: str = sys.stdin.readline().rstrip()
        idx: int = 0
        while idx < min(30, len(stock)) and pi[idx] == stock[idx]: idx += 1
        sys.stdout.write(f'{idx}\n')


if __name__ == '__main__':
    solution()