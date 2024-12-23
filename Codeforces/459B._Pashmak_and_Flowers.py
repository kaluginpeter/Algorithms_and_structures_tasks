# B. Pashmak and Flowers
# time limit per test1 second
# memory limit per test256 megabytes
# Pashmak decided to give Parmida a pair of flowers from the garden. There are n flowers in the garden and the i-th of them has a beauty number bi. Parmida is a very strange girl so she doesn't want to have the two most beautiful flowers necessarily. She wants to have those pairs of flowers that their beauty difference is maximal possible!
#
# Your task is to write a program which calculates two things:
#
# The maximum beauty difference of flowers that Pashmak can give to Parmida.
# The number of ways that Pashmak can pick the flowers. Two ways are considered different if and only if there is at least one flower that is chosen in the first way and not chosen in the second way.
# Input
# The first line of the input contains n (2 ≤ n ≤ 2·105). In the next line there are n space-separated integers b1, b2, ..., bn (1 ≤ bi ≤ 109).
#
# Output
# The only line of output should contain two integers. The maximum beauty difference and the number of ways this may happen, respectively.
#
# Examples
# InputCopy
# 2
# 1 2
# OutputCopy
# 1 1
# InputCopy
# 3
# 1 4 5
# OutputCopy
# 4 1
# InputCopy
# 5
# 3 1 2 3 1
# OutputCopy
# 2 4
# Note
# In the third sample the maximum beauty difference is 2 and there are 4 ways to do this:
#
# choosing the first and the second flowers;
# choosing the first and the fifth flowers;
# choosing the fourth and the second flowers;
# choosing the fourth and the fifth flowers.
# Solution
# C++ O(NlogN) O(1) Sorting
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> scores;
    for (int i = 0; i < n; ++i) {
        int score;
        std::cin >> score;
        scores.push_back(score);
    }
    std::sort(scores.begin(), scores.end());
    long long x = 1;
    long long y = 1;
    int idx = 0;
    while (idx + 1 < n && scores[idx] == scores[idx + 1]) {
        ++x;
        ++idx;
    }
    idx = n - 1;
    while (idx >= 0 && scores[idx] == scores[idx - 1]) {
        ++y;
        --idx;
    }
    long long t = x * y;
    if (scores[0] == scores[n - 1]) {
        t = x * (x + 1) / 2 - x;
    }
    std::cout << scores[n - 1] - scores[0] << " " << t << "\n";
}


int main() {
    solution();
}

# Python O(NlogN) O(1) Sorting
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    scores: list = list(map(int, sys.stdin.readline().rstrip().split()))
    scores.sort()
    x = y = 1
    idx: int = 0
    while idx + 1 < n and scores[idx] == scores[idx + 1]:
        idx += 1
        x += 1
    idx = n - 1
    while idx - 1 >= 0 and scores[idx] == scores[idx - 1]:
        y += 1
        idx -= 1
    t: int = x * y
    if scores[-1] == scores[0]:
        t = x * (x + 1) // 2 - x
    sys.stdout.write(f'{scores[-1] - scores[0]} {t}\n')


if __name__ == '__main__':
    solution()
