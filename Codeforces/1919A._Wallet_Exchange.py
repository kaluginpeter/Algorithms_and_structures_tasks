# A. Wallet Exchange
# time limit per test1 second
# memory limit per test256 megabytes
# Alice and Bob are bored, so they decide to play a game with their wallets. Alice has a
#  coins in her wallet, while Bob has b
#  coins in his wallet.
#
# Both players take turns playing, with Alice making the first move. In each turn, the player will perform the following steps in order:
#
# Choose to exchange wallets with their opponent, or to keep their current wallets.
# Remove 1
#  coin from the player's current wallet. The current wallet cannot have 0
#  coins before performing this step.
# The player who cannot make a valid move on their turn loses. If both Alice and Bob play optimally, determine who will win the game.
#
# Input
# Each test contains multiple test cases. The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases. The description of the test cases follows.
#
# The first and only line of each test case contains two integers a
#  and b
#  (1≤a,b≤109
# ) — the number of coins in Alice's and Bob's wallets, respectively.
#
# Output
# For each test case, output "Alice" if Alice will win the game, and "Bob" if Bob will win the game.
#
# Example
# InputCopy
# 10
# 1 1
# 1 4
# 5 3
# 4 5
# 11 9
# 83 91
# 1032 9307
# 839204 7281
# 1000000000 1000000000
# 53110 2024
# OutputCopy
# Bob
# Alice
# Bob
# Alice
# Bob
# Bob
# Alice
# Alice
# Bob
# Bob
# Note
# In the first test case, an example of the game is shown below:
#
# Alice chooses to not swap wallets with Bob in step 1 of her move. Now, a=0
#  and b=1
# .
# Since Alice's wallet is empty, Bob must choose to not swap their wallets in step 1 of his move. Now, a=0
#  and b=0
# .
# Since both Alice's and Bob's wallets are empty, Alice is unable to make a move. Hence, Bob wins.
# In the second test case, an example of the game is shown below:
#
# Alice chooses to swap wallets with Bob in step 1 of her move. Now, a=3
#  and b=1
# .
# Bob chooses to swap wallets with Alice in step 1 of his move. Now, a=1
#  and b=2
# .
# Alice chooses to not swap wallets with Bob in step 1 of her move. Now, a=0
#  and b=2
# .
# Since Alice's wallet is empty, Bob can only choose to not swap wallets with Alice in step 1 of his move. Now, a=0
#  and b=1
# .
# Since Alice's wallet is empty, Alice can only choose to swap wallets with Bob in step 1 of her move. Now, a=0
#  and b=0
# .
# Since both Alice's wallet and Bob's wallet are empty, Bob is unable to make a move. Hence, Alice wins.
# Solution
# C++ O(1) O(1) Math Greedy
#include <iostream>



void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int x, y;
        std::scanf("%d %d", &x, &y);
        std::cout << ((static_cast<long long>(x) + y) & 1? "Alice" : "Bob") << std::endl;
    }
}

int main() {
    solution();
}

# Python O(1) O(1) Math Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write('{}\n'.format(['Bob', 'Alice'][(x + y) & 1]))


if __name__ == '__main__':
    solution()