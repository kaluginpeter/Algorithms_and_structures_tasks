# There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).
#
# The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.
#
# For example, if the row consists of players 1, 2, 4, 6, 7
# Player 1 competes against player 7.
# Player 2 competes against player 6.
# Player 4 automatically advances to the next round.
# After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).
#
# The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.
#
# Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.
#
#
#
# Example 1:
#
# Input: n = 11, firstPlayer = 2, secondPlayer = 4
# Output: [3,4]
# Explanation:
# One possible scenario which leads to the earliest round number:
# First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Second round: 2, 3, 4, 5, 6, 11
# Third round: 2, 3, 4
# One possible scenario which leads to the latest round number:
# First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Second round: 1, 2, 3, 4, 5, 6
# Third round: 1, 2, 4
# Fourth round: 2, 4
# Example 2:
#
# Input: n = 5, firstPlayer = 1, secondPlayer = 5
# Output: [1,1]
# Explanation: The players numbered 1 and 5 compete in the first round.
# There is no way to make them compete in any other round.
#
#
# Constraints:
#
# 2 <= n <= 28
# 1 <= firstPlayer < secondPlayer <= n
# Python O((2^N)NlogN) O(N) BitMask Recursion
class Solution:
    early: int = 0
    later: int = 0

    def backtracking(self, players: list[int], x: int, y: int, steps: int) -> None:
        for i in range(len(players) // 2):
            if (players[i] == x and players[len(players) - 1 - i] == y) or (players[i] == y and players[len(players) - 1 - i] == x):
                self.early = min(self.early, steps)
                self.later = max(self.later, steps)
                return
        m: int = len(players) // 2
        if not (len(players) & 1): m -= 2
        else:
            if players[len(players) // 2] in (x, y): m -= 1
            else: m -= 2
        for mask in range(1 << m):
            mask_pointer: int = mask
            winners: list[int] = []
            for i in range(len(players) // 2):
                if players[i] in (x, y):
                    winners.append(players[i])
                    continue
                elif players[len(players) - 1 - i] in (x, y):
                    winners.append(players[len(players) - 1 - i])
                    continue
                if mask_pointer & 1: winners.append(players[i])
                else: winners.append(players[len(players) - 1 - i])
                mask_pointer >>= 1
            if len(players) & 1: winners.append(players[len(players) // 2])
            winners.sort()
            self.backtracking(winners, x, y, steps + 1)

    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        self.early = n
        self.later = 0
        self.backtracking(list(range(n)), firstPlayer - 1, secondPlayer - 1, 1)
        return [self.early, self.later]

# C++ O((2^N)NlogN) O(N) Bitmasking Recursion
class Solution {
public:
    int early = 0, later = 0;
    void backtrack(std::vector<int> &players, const int &x, const int &y, int steps) {
        for (int i = 0; i < players.size() / 2; ++i) {
            if ((players[i] == x && players[players.size() - 1 - i] == y) || (players[i] == y && players[players.size() - 1 - i] == x)) {
                early = std::min(early, steps);
                later = std::max(later, steps);
                return;
            }
        }
        int nextN = players.size() / 2;
        if (!(players.size() & 1)) nextN -= 2;
        else {
            if (players[players.size() / 2] == x || players[players.size() / 2] == y) --nextN;
            else nextN -= 2;
        }
        for (int mask = 0; mask < (1 << nextN); ++mask) {
            std::vector<int> winners;
            int pointerMask = mask;
            for (int i = 0; i < players.size() / 2; ++i) {
                if (players[i] == x || players[i] == y) {
                    winners.push_back(players[i]);
                    continue;
                } else if (players[players.size() - 1 - i] == x || players[players.size() - 1 - i] == y) {
                    winners.push_back(players[players.size() - 1 - i]);
                    continue;
                }
                if (pointerMask & 1) winners.push_back(players[i]);
                else winners.push_back(players[players.size() - 1 - i]);
                pointerMask >>= 1;
            }
            if (players.size() & 1) winners.push_back(players[players.size() / 2]);
            std::sort(winners.begin(), winners.end());
            backtrack(winners, x, y, steps + 1);
        }
    }

    vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        early = n;
        later = 0;
        std::vector<int> players;
        for (int i = 1; i <= n; ++i) players.push_back(i);
        backtrack(players, firstPlayer, secondPlayer, 1);
        return {early, later};
    }
};