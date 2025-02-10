# B. Random Teams
# time limit per test1 second
# memory limit per test256 megabytes
# n participants of the competition were split into m teams in some manner so that each team has at least one participant. After the competition each pair of participants from the same team became friends.
#
# Your task is to write a program that will find the minimum and the maximum number of pairs of friends that could have formed by the end of the competition.
#
# Input
# The only line of input contains two integers n and m, separated by a single space (1 ≤ m ≤ n ≤ 109) — the number of participants and the number of teams respectively.
#
# Output
# The only line of the output should contain two integers kmin and kmax — the minimum possible number of pairs of friends and the maximum possible number of pairs of friends respectively.
#
# Examples
# InputCopy
# 5 1
# OutputCopy
# 10 10
# InputCopy
# 3 2
# OutputCopy
# 1 1
# InputCopy
# 6 3
# OutputCopy
# 3 6
# Note
# In the first sample all the participants get into one team, so there will be exactly ten pairs of friends.
#
# In the second sample at any possible arrangement one team will always have two participants and the other team will always have one participant. Thus, the number of pairs of friends will always be equal to one.
#
# In the third sample minimum number of newly formed friendships can be achieved if participants were split on teams consisting of 2 people, maximum number can be achieved if participants were split on teams of 1, 1 and 4 people.
# Solution
# C++ O(1) O(1) Math
#include <bits/stdc++.h>


void solution() {
    long long n, m;
    std::cin >> n >> m;
    long long mx = (n - m + 1) * (n - m) / 2;
    long long mn = 0;
    if (n % m == 0) mn = (n / m) * (n / m - 1) / 2 * m;
    else {
        long long mean = n / m;
        mn = mean * (mean - 1) / 2 * (m - n % m) + (mean + 1) * (mean) / 2 * (n % m);
    }
    std::cout << mn << " " << mx << "\n";
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys

def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    mx: int = (n - m + 1) * (n - m) // 2
    mn: int = 0
    if n % m == 0: mn = (n // m) * (n // m - 1) // 2 * m
    else:
        mean: int = n // m
        mn = mean * (mean - 1) // 2 * (m - n % m) + (mean + 1) * mean // 2 * (n % m)
    sys.stdout.write(f'{mn} {mx}\n')



if __name__ == '__main__':
    solution()