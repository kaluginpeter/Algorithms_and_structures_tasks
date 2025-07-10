# D. Binary String Battle
# time limit per test2 seconds
# memory limit per test256 megabytes
# Alice and Bob are given a binary string s
#  of length n
# , and an integer k
#  (1≤k<n
# ).
#
# Alice wins if she is able to transform all characters of s
#  into zeroes. If Alice is unable to win in a finite number of moves, then Bob wins.
#
# Alice and Bob take turns, with Alice going first.
#
# On Alice's turn, she may choose any subsequence∗
#  of length k
#  in s
# , then set all characters in that subsequence to zero.
# On Bob's turn, he may choose any substring†
#  of length k
#  in s
# , then set all characters in that substring to one.
# Note that Alice wins if the string consists of all zeros at any point during the game, including in between Alice's and Bob's turns.
#
# Determine who wins with optimal play.
#
# ∗
# A subsequence of a string s
#  is a set of characters in s
# . Note that these characters do not have to be adjacent.
#
# †
# A substring of a string s
#  is a contiguous group of characters in s
# . Note that these characters must be adjacent.
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# )  — the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (2≤n≤2⋅105
# , 1≤k<n
# ).
#
# The second line of each test case contains a binary string s
#  of length n
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output on a single line "Alice" if Alice wins with optimal play, and "Bob" if Bob wins with optimal play.
#
# You can output the answer in any case (upper or lower). For example, the strings "aLiCe", "alice", "ALICE", and "alICE" will be recognized as "Alice".
#
# Example
# InputCopy
# 6
# 5 2
# 11011
# 7 4
# 1011011
# 6 1
# 010000
# 4 1
# 1111
# 8 3
# 10110110
# 6 4
# 111111
# OutputCopy
# Bob
# Alice
# Alice
# Bob
# Bob
# Alice
# Note
# In the third sample, Alice can choose the subsequence consisting of s2
# , turning s
#  into 000000
# . Then she wins immediately.
#
# In the fourth sample, it can be shown that there is no way for Alice to guarantee that she can turn s
#  into 0000
#  within a finite number of moves.
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    int n, k;
    std::cin >> n >> k;
    std::string sequence = "";
    std::cin >> sequence;
    // 1st case, when ones count <= k
    int ones = 0;
    for (char &character : sequence) {
        if (character == '1') ++ones;
    }
    if (ones <= k) {
        std::cout << "Alice\n";
        return;
    }
    std::cout << (k * 2 > n ? "Alice" : "Bob") << std::endl;
    return;

}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    sequence: str = sys.stdin.readline().rstrip()
    ones: int = sequence.count('1')
    if ones <= k:
        sys.stdout.write('Alice\n')
        return
    sys.stdout.write('{}\n'.format(['Bob', 'Alice'][k * 2 > n]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()