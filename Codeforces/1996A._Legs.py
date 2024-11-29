# A. Legs
# time limit per test2 seconds
# memory limit per test256 megabytes
# It's another beautiful day on Farmer John's farm.
#
# After Farmer John arrived at his farm, he counted n
#  legs. It is known only chickens and cows live on the farm, and a chicken has 2
#  legs while a cow has 4
# .
#
# What is the minimum number of animals Farmer John can have on his farm assuming he counted the legs of all animals?
#
# Input
# The first line contains single integer t
#  (1≤t≤103
# ) — the number of test cases.
#
# Each test case contains an integer n
#  (2≤n≤2⋅103
# , n
#  is even).
#
# Output
# For each test case, output an integer, the minimum number of animals Farmer John can have on his farm.
#
# Example
# InputCopy
# 3
# 2
# 6
# 8
# OutputCopy
# 1
# 2
# 2
# Solution
# C++ O(1) O(1) Math
#include <iostream>

void solution(int t) {
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::cout << (n / 4 + n % 4 / 2) << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}
# Python O(1) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        sys.stdout.write(str(n // 4 + n % 4 // 2) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
