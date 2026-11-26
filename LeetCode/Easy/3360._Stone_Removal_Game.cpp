/*
Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.

Alice starts by removing exactly 10 stones on her first turn.
For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
The player who cannot make a move loses the game.

Given a positive integer n, return true if Alice wins the game and false otherwise.

 

Example 1:

Input: n = 12

Output: true

Explanation:

Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
Bob cannot remove 9 stones, so Alice wins.
Example 2:

Input: n = 1

Output: false

Explanation:

Alice cannot remove 10 stones, so Alice loses.
 

Constraints:

1 <= n <= 50
*/
// Solution
// C++ O(1) O(1) Math
class Solution {
public:
    bool canAliceWin(int n) {
        int k = (21 - std::sqrt(441.0 - 8 * n)) / 2;
        // floating point error at exact boundaries
        while ((k + 1) <= 10 && (k + 1) * (21 - (k + 1)) / 2 <= n) ++k;
        while (k > 0 && k * (21 - k) / 2 > n) --k;
        return k & 1;
    }
};
// 10 8 6 4 2 = 30
//  9 7 5 3 1 = 25
// Let's observe the sequence of moves: 10 -> 9 -> 8 -> ... -> 2 -> 1
// Obviously it's a arithmetic sequence, so let's try to formalize it
// Image the i'th move? How much stones are will be taken?
// For first move when i = 1 the answer is 10
// For the second i = 2 answer is 9
// So for i'th move the answer will be 11 - i
// Then using arithmetic sequence formula (firstTerm + lastTerm) * numberOfTerm / 2
// we can write something like this: (10 + (11 - k)) * k / 2
// Let's simplify the expression:
// (10 + 11 - k) * k / 2 -> (21 - k) * k / 2 -> (-k^2 + 21k) / 2
// We have a quadratic equation, let's build an inquality such that
// the root of euqation is less than or equal to n, since we need to fit all stones into pile
// (-k^2 + 21k) / 2 <= n | * 2
// -k^2 + 21k <= 2n
// -k^2 + 21k - 2n <= 0 | * -1
// k^2 - 21k + 2n >= 0
// Use a discriminant formula ot find a roots:
// x1 = (21 + sqrt((-21)^2 - 4 * 1 * 2n)) / 2 -> (21 + sqrt(441 - 8n)) / 2
// s2 = (21 - sqrt((-21)^2 - 4 * 1 * 2n)) / 2 -> (21 - sqrt(441 - 8n)) / 2

// k^2 - 21k + 2n >= 0 holds when k <= x1 or k >= x2
// at most 10 moves exist (10, 9, ..., 1), so k <= 10 < x2 -> k <= x1
// largest valid k = rounded down (21 - sqrt(441 - 8n)) / 2
// moves alternate Alice, Bob, Alice, ... -> Alice wins iff k is odd