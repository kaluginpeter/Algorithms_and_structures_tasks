# B. BerSU Ball
# time limit per test1 second
# memory limit per test256 megabytes
# The Berland State University is hosting a ballroom dance in celebration of its 100500-th anniversary! n boys and m girls are already busy rehearsing waltz, minuet, polonaise and quadrille moves.
#
# We know that several boy&girl pairs are going to be invited to the ball. However, the partners' dancing skill in each pair must differ by at most one.
#
# For each boy, we know his dancing skills. Similarly, for each girl we know her dancing skills. Write a code that can determine the largest possible number of pairs that can be formed from n boys and m girls.
#
# Input
# The first line contains an integer n (1 ≤ n ≤ 100) — the number of boys. The second line contains sequence a1, a2, ..., an (1 ≤ ai ≤ 100), where ai is the i-th boy's dancing skill.
#
# Similarly, the third line contains an integer m (1 ≤ m ≤ 100) — the number of girls. The fourth line contains sequence b1, b2, ..., bm (1 ≤ bj ≤ 100), where bj is the j-th girl's dancing skill.
#
# Output
# Print a single number — the required maximum possible number of pairs.
#
# Examples
# inputCopy
# 4
# 1 4 6 2
# 5
# 5 1 5 7 9
# outputCopy
# 3
# inputCopy
# 4
# 1 2 3 4
# 4
# 10 11 12 13
# outputCopy
# 0
# inputCopy
# 5
# 1 1 1 1 1
# 3
# 1 2 3
# outputCopy
# 2
# Solution
# Python O(NlogN) O(1) Two Pointers
import sys


def solution(boys: list, girls: list) -> str:
    boys.sort()
    girls.sort()
    left: int = 0
    right: int = 0
    pairs: int = 0
    while left < len(boys) and right < len(girls):
        if abs(boys[left] - girls[right]) <= 1:
            pairs += 1
            left += 1
            right += 1
        elif boys[left] < girls[right]:
            left += 1
        else:
            right += 1
    return str(pairs)


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    boys: list = list(map(int, sys.stdin.readline().rstrip().split()))
    m: int = int(sys.stdin.readline().rstrip())
    girls: list = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(solution(boys, girls))


# C++ O(NlogN) O(1) Two Pointers
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> boys;
    for (int i = 0; i < n; ++i) {
        int boy;
        std::cin >> boy;
        boys.push_back(boy);
    }
    int m;
    std::cin >> m;
    std::vector<int> girls;
    for (int i = 0; i < m; ++i) {
        int girl;
        std::cin >> girl;
        girls.push_back(girl);
    }
    std::sort(boys.begin(), boys.end());
    std::sort(girls.begin(), girls.end());
    int left = 0, right = 0;
    int pairs = 0;
    while (left < boys.size() && right < girls.size()) {
        if (std::abs(boys[left] - girls[right]) <= 1) {
            pairs += 1;
            left += 1;
            right += 1;
        } else if (boys[left] < girls[right]) {
            left += 1;
        } else {
            right += 1;
        }
    }
    std::cout << pairs << std::endl;
}
