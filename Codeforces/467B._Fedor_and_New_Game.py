# B. Fedor and New Game
# time limit per test1 second
# memory limit per test256 megabytes
# After you had helped George and Alex to move in the dorm, they went to help their friend Fedor play a new computer game «Call of Soldiers 3».
#
# The game has (m + 1) players and n types of soldiers in total. Players «Call of Soldiers 3» are numbered form 1 to (m + 1). Types of soldiers are numbered from 0 to n - 1. Each player has an army. Army of the i-th player can be described by non-negative integer xi. Consider binary representation of xi: if the j-th bit of number xi equal to one, then the army of the i-th player has soldiers of the j-th type.
#
# Fedor is the (m + 1)-th player of the game. He assume that two players can become friends if their armies differ in at most k types of soldiers (in other words, binary representations of the corresponding numbers differ in at most k bits). Help Fedor and count how many players can become his friends.
#
# Input
# The first line contains three integers n, m, k (1 ≤ k ≤ n ≤ 20; 1 ≤ m ≤ 1000).
#
# The i-th of the next (m + 1) lines contains a single integer xi (1 ≤ xi ≤ 2n - 1), that describes the i-th player's army. We remind you that Fedor is the (m + 1)-th player.
#
# Output
# Print a single integer — the number of Fedor's potential friends.
#
# Examples
# InputCopy
# 7 3 1
# 8
# 5
# 111
# 17
# OutputCopy
# 0
# InputCopy
# 3 3 3
# 1
# 2
# 3
# 4
# OutputCopy
# 3
# Solution
# C++ O(N) O(N) BitMask
#include <bits/stdc++.h>

using namespace std;


void solution() {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    vector<bitset<64>> players;
    for (int i = 0; i < m + 1; ++i) {
        long long player;
        scanf("%d", &player);
        bitset<64> y(player);
        players.push_back(y);
    }
    int friends = 0;
    for (int i = 0; i < m; ++i) {
        if ((players[m] ^ players[i]).count() <= k) ++friends;
    }
    printf("%d\n", friends);
}


int main() {
    solution();
}

# Python O(N) O(N) BitSet
import sys


def solution() -> None:
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    players: list[int] = []
    for _ in range(m + 1):
        player: int = int(sys.stdin.readline().rstrip())
        players.append(player)
    friends: int = 0
    for i in range(m):
        if (players[m] ^ players[i]).bit_count() <= k: friends += 1
    sys.stdout.write(f'{friends}\n')


if __name__ == '__main__':
    solution()