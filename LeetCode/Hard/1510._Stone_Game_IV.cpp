
/*
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.



Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).


Constraints:

1 <= n <= 105
*/
// Solution
// C++ O(10^5) O(10^5) DynamicProgramming
static constexpr int MAX = 100000;
class Solution {
public:
    inline static std::bitset<MAX + 1> dp;
    inline static bool init = []() {
        for (int i = 0; i <= MAX; ++i) {
            if (dp.test(i)) continue;
            for (int j = 1; j * j <= MAX - i; ++j) dp.set(i + j * j);
        }
        return false;
    }();

    bool winnerSquareGame(int n) {
        return dp.test(n);
    }
};