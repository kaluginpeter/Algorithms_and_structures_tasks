# A. Vacations
# time limit per test1 second
# memory limit per test256 megabytes
# Vasya has n days of vacations! So he decided to improve his IT skills and do sport. Vasya knows the following information about each of this n days: whether that gym opened and whether a contest was carried out in the Internet on that day. For the i-th day there are four options:
#
# on this day the gym is closed and the contest is not carried out;
# on this day the gym is closed and the contest is carried out;
# on this day the gym is open and the contest is not carried out;
# on this day the gym is open and the contest is carried out.
# On each of days Vasya can either have a rest or write the contest (if it is carried out on this day), or do sport (if the gym is open on this day).
#
# Find the minimum number of days on which Vasya will have a rest (it means, he will not do sport and write the contest at the same time). The only limitation that Vasya has — he does not want to do the same activity on two consecutive days: it means, he will not do sport on two consecutive days, and write the contest on two consecutive days.
#
# Input
# The first line contains a positive integer n (1 ≤ n ≤ 100) — the number of days of Vasya's vacations.
#
# The second line contains the sequence of integers a1, a2, ..., an (0 ≤ ai ≤ 3) separated by space, where:
#
# ai equals 0, if on the i-th day of vacations the gym is closed and the contest is not carried out;
# ai equals 1, if on the i-th day of vacations the gym is closed, but the contest is carried out;
# ai equals 2, if on the i-th day of vacations the gym is open and the contest is not carried out;
# ai equals 3, if on the i-th day of vacations the gym is open and the contest is carried out.
# Output
# Print the minimum possible number of days on which Vasya will have a rest. Remember that Vasya refuses:
#
# to do sport on any two consecutive days,
# to write the contest on any two consecutive days.
# Examples
# InputCopy
# 4
# 1 3 2 0
# OutputCopy
# 2
# InputCopy
# 7
# 1 3 3 2 1 2 3
# OutputCopy
# 0
# InputCopy
# 2
# 2 2
# OutputCopy
# 1
# Note
# In the first test Vasya can write the contest on the day number 1 and do sport on the day number 3. Thus, he will have a rest for only 2 days.
#
# In the second test Vasya should write contests on days number 1, 3, 5 and 7, in other days do sport. Thus, he will not have a rest for a single day.
#
# In the third test Vasya can do sport either on a day number 1 or number 2. He can not do sport in two days, because it will be contrary to the his limitation. Thus, he will have a rest for only one day.
# Solution
# Python O(N) O(N) DynamicProgramming
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    a: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    dp: list[list[int]] = [[float('inf')] * 3 for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        current: int = a[i - 1]
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + 1
        if current == 1 or current == 3: dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
        if current == 2 or current == 3: dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
    sys.stdout.write('{}\n'.format(min(dp[n][0], dp[n][1], dp[n][2])))


if __name__ == '__main__':
    solution()

# C++ O(N) O(N) DynamicProgramming
#include <iostream>
#include <vector>
#include <algorithm>

constexpr int INF = 1e9;

void solution() {
    int n;
    std::scanf("%d", &n);
    std::vector<int> a(n, 0);
    for (int i = 0; i < n; ++i) std::scanf("%d", &a[i]);
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(3, INF));
    dp[0][0] = 0;
    for (int i = 1; i <= n; ++i) {
        int current = a[i - 1];
        dp[i][0] = std::min({dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]}) + 1;
        if (current == 1 || current == 3) dp[i][1] = std::min(dp[i - 1][0], dp[i - 1][2]);
        if (current == 2 || current == 3) dp[i][2] = std::min(dp[i - 1][0], dp[i - 1][1]);
    }

    std::printf("%d\n", std::min({dp[n][0], dp[n][1], dp[n][2]}));
}


int main() {
    solution();
}