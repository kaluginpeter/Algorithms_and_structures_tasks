# A. Fair Playoff
# time limit per test2 seconds
# memory limit per test256 megabytes
# Four players participate in the playoff tournament. The tournament is held according to the following scheme: the first player will play with the second, and the third player with the fourth, then the winners of the pairs will play in the finals of the tournament.
#
# It is known that in a match between two players, the one whose skill is greater will win. The skill of the i
# -th player is equal to si
#  and all skill levels are pairwise different (i. e. there are no two identical values in the array s
# ).
#
# The tournament is called fair if the two players with the highest skills meet in the finals.
#
# Determine whether the given tournament is fair.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# A single line of test case contains four integers s1,s2,s3,s4
#  (1≤si≤100
# ) — skill of the players. It is guaranteed that all the numbers in the array are different.
#
# Output
# For each testcase, output YES if the tournament is fair, or NO otherwise.
#
# Example
# inputCopy
# 4
# 3 7 9 5
# 4 5 6 9
# 5 3 8 1
# 6 5 3 2
# outputCopy
# YES
# NO
# YES
# NO
# Note
# Consider the example:
#
# in the first test case, players 2
#  and 3
#  with skills 7
#  and 9
#  advance to the finals;
# in the second test case, players 2
#  and 4
#  with skills 5
#  and 9
#  advance to the finals. The player with skill 6
#  does not advance, but the player with skill 5
#  advances to the finals, so the tournament is not fair;
# in the third test case, players 1
#  and 3
#  with skills 5
#  and 8
#  advance to the finals;
# in the fourth test case, players 1
#  and 3
#  with skills 6
#  and 3
#  advance to the finals. The player with skill 5
#  does not advance, but the player with skill 3
#  advances to the finals, so the tournament is not fair.
# Solution
# Python O(1) O(1) Math Greedy
import sys


def solution(t: int) -> None:
    for _ in range(t):
        a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
        f_p_mn: int = min(a, b)
        f_p_mx: int = max(a, b)
        s_p_mn: int = min(c, d)
        s_p_mx: int = max(c, d)
        sys.stdout.write(['NO', 'YES'][f_p_mx > s_p_mn and s_p_mx > f_p_mn] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(1) O(1) Math Greedy
#include <iostream>

int main() {
    int t;
    std::cin >> t;
    for (int rep = 0; rep < t; ++rep) {
        int a, b, c, d;
        std::cin >> a >> b >> c >> d;
        int f_p_mn = std::min(a, b);
        int f_p_mx = std::max(a, b);
        int s_p_mn = std::min(c, d);
        int s_p_mx = std::max(c, d);
        std::cout << (f_p_mx > s_p_mn && s_p_mx > f_p_mn ? "YES" : "NO") << std::endl;
    }
}