# A. Jzzhu and Children
# time limit per test1 second
# memory limit per test256 megabytes
# There are n children in Jzzhu's school. Jzzhu is going to give some candies to them. Let's number all the children from 1 to n. The i-th child wants to get at least ai candies.
#
# Jzzhu asks children to line up. Initially, the i-th child stands at the i-th place of the line. Then Jzzhu start distribution of the candies. He follows the algorithm:
#
# Give m candies to the first child of the line.
# If this child still haven't got enough candies, then the child goes to the end of the line, else the child go home.
# Repeat the first two steps while the line is not empty.
# Consider all the children in the order they go home. Jzzhu wants to know, which child will be the last in this order?
#
# Input
# The first line contains two integers n, m (1 ≤ n ≤ 100; 1 ≤ m ≤ 100). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 100).
#
# Output
# Output a single integer, representing the number of the last child.
#
# Examples
# InputCopy
# 5 2
# 1 3 1 4 2
# OutputCopy
# 4
# InputCopy
# 6 4
# 1 1 2 2 3 3
# OutputCopy
# 6
# Note
# Let's consider the first sample.
#
# Firstly child 1 gets 2 candies and go home. Then child 2 gets 2 candies and go to the end of the line. Currently the line looks like [3, 4, 5, 2] (indices of the children in order of the line). Then child 3 gets 2 candies and go home, and then child 4 gets 2 candies and goes to the end of the line. Currently the line looks like [5, 2, 4]. Then child 5 gets 2 candies and goes home. Then child 2 gets two candies and goes home, and finally child 4 gets 2 candies and goes home.
#
# Child 4 is the last one who goes home.
# Solution
# C++ O(N) O(1) Math Greedy
#include <iostream>


void solution() {
    int n, m;
    std::scanf("%d %d", &n, &m);
    int prevReps = 0;
    int player = 0;
    for (int i = 0; i < n; ++i) {
        int desire;
        std::scanf("%d", &desire);
        int reps = desire / m + (int)(desire % m != 0);
        if (reps >= prevReps) {
            prevReps = reps;
            player = i + 1;
        }
    }
    std::printf("%d\n", player);
}


int main() {
    solution();
}

# Python O(N) O(1) Math Greedy
import sys


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    last: int = 0
    reps: int = 0
    players: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for player in range(1, n + 1):
        desire: int = next(players)
        rep: int = desire // m + int(desire % m != 0)
        if rep >= reps:
            reps = rep
            last = player
    sys.stdout.write('{}\n'.format(last))


if __name__ == '__main__':
    solution()