# D. This Is the Last Time
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given n
#  casinos, numbered from 1
#  to n
# . Each casino is described by three integers: li
# , ri
# , and reali
#  (li≤reali≤ri
# ). You initially have k
#  coins.
#
# You can play at casino i
#  only if the current number of coins x
#  satisfies li≤x≤ri
# . After playing, your number of coins becomes reali
# .
#
# You can visit the casinos in any order and are not required to visit all of them. Each casino can be visited no more than once.
#
# Your task is to find the maximum final number of coins you can obtain.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤n≤105
# , 0≤k≤109
# ) — the number of casinos and the initial number of coins.
#
# This is followed by n
#  lines. In the i
# -th line, there are three integers li
# , ri
# , reali
#  (0≤li≤reali≤ri≤109
# ) — the parameters of the i
# -th casino.
#
# It is guaranteed that the sum of all n
#  across all test cases does not exceed 105
# .
#
# Output
# For each test case, output a single integer — the maximum number of coins you can obtain after optimally choosing the order of visiting the casinos.
#
# Example
# InputCopy
# 5
# 3 1
# 2 3 3
# 1 2 2
# 3 10 10
# 1 0
# 1 2 2
# 1 2
# 1 2 2
# 2 2
# 1 3 2
# 2 4 4
# 2 5
# 1 10 5
# 3 6 5
# OutputCopy
# 10
# 0
# 2
# 4
# 5
# Note
# In the first test case, you can first play at the 2
# -nd casino. After that, you will have 2
#  coins. Then you can play at the 1
# -st casino, and the number of coins will increase to 3
# . Finally, after playing at the 3
# -rd casino, you will have 10
#  coins — this is the maximum possible amount.
#
# In the second test case, you have no money, so you cannot earn more.
#
# In the fourth test case, it is beneficial to play at the 2
# -nd casino right away and earn 4
#  coins.
# Solution
# C++ O(NlogN) O(N) PriorityQueue
#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <set>

struct Casino {
    int l, r, real;
};

bool compareCasinos(const Casino& a, const Casino& b) {
    return a.l < b.l;
}

void solution() {
    int n;
    long long k;
    std::cin >> n >> k;
    std::vector<Casino> casinos(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> casinos[i].l >> casinos[i].r >> casinos[i].real;
    }
    std::sort(casinos.begin(), casinos.end(), compareCasinos);
    std::multiset<std::pair<int, int>> available_casinos;
    int casino_idx = 0;

    while (true) {
        while (casino_idx < n && casinos[casino_idx].l <= k) {
            available_casinos.insert({casinos[casino_idx].real, casinos[casino_idx].r});
            ++casino_idx;
        }
        while (!available_casinos.empty() && available_casinos.rbegin()->second < k) {
            available_casinos.erase(std::prev(available_casinos.end()));
        }
        if (available_casinos.empty() || available_casinos.rbegin()->first <= k) break;
        k = available_casinos.rbegin()->first;
        available_casinos.erase(std::prev(available_casinos.end()));
    }
    std::cout << k << "\n";
}

int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN) PriorityQueue
import heapq
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().split())

    casinos: list[tuple[int, int, int]] = []
    for _ in range(n):
        l, r, real = map(int, sys.stdin.readline().split())
        casinos.append((l, r, real))
    casinos.sort()
    available_casinos_heap: list[tuple[int, int]] = []
    casino_idx: int = 0
    while True:
        while casino_idx < n and casinos[casino_idx][0] <= k:
            l, r, real = casinos[casino_idx]
            heapq.heappush(available_casinos_heap, (-real, r))
            casino_idx += 1
        while available_casinos_heap and available_casinos_heap[0][1] < k:
            heapq.heappop(available_casinos_heap)
        if not available_casinos_heap or -available_casinos_heap[0][0] <= k:
            break
        best_payout, _ = heapq.heappop(available_casinos_heap)
        k = -best_payout

    sys.stdout.write('{}\n'.format(k))


if __name__ == "__main__":
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()
