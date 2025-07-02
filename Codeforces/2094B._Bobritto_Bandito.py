# B. Bobritto Bandito
# time limit per test1 second
# memory limit per test256 megabytes
# In Bobritto Bandito's home town of residence, there are an infinite number of houses on an infinite number line, with houses at …,−2,−1,0,1,2,…
# . On day 0
# , he started a plague by giving an infection to the unfortunate residents of house 0
# . Each succeeding day, the plague spreads to exactly one healthy household that is next to an infected household. It can be shown that each day the infected houses form a continuous segment.
#
# Let the segment starting at the l
# -th house and ending at the r
# -th house be denoted as [l,r]
# . You know that after n
#  days, the segment [l,r]
#  became infected. Find any such segment [l′,r′]
#  that could have been infected on the m
# -th day (m≤n
# ).
#
# Input
# The first line contains an integer t
#  (1≤t≤100
# ) – the number of independent test cases.
#
# The only line of each test case contains four integers n
# , m
# , l
# , and r
#  (1≤m≤n≤2000,−n≤l≤0≤r≤n,r−l=n
# ).
#
# Output
# For each test case, output two integers l′
#  and r′
#  on a new line. If there are multiple solutions, output any.
#
# Example
# InputCopy
# 4
# 4 2 -2 2
# 4 1 0 4
# 3 3 -1 2
# 9 8 -6 3
# OutputCopy
# -1 1
# 0 1
# -1 2
# -5 3
# Note
# In the first test case, it is possible that on the 1
# -st, 2
# -nd, and 3
# -rd days the interval of houses affected is [−1,0]
# , [−1,1]
# , [−2,1]
# . Therefore, [−1,1]
#  is a valid output.
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, m, l, r;
        std::cin >> n >> m >> l >> r;
        if (r < 0) {
            std::swap(l, r);
            r = -r;
            l = -l;
        }
        int extra = std::max(0, m - r);
        int left = 0 - extra;
        std::printf("%d %d\n", left, std::min(m, r));
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m, l, r = map(int, sys.stdin.readline().rstrip().split())
        if r < 0: l, r = -r, -l
        extra: int = max(0, m - r)
        left: int = 0 - extra
        sys.stdout.write('{} {}\n'.format(left, min(m, r)))


if __name__ == '__main__':
    solution()