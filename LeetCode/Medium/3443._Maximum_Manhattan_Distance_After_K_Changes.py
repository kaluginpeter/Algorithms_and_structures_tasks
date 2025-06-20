# You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:
#
# 'N' : Move north by 1 unit.
# 'S' : Move south by 1 unit.
# 'E' : Move east by 1 unit.
# 'W' : Move west by 1 unit.
# Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.
#
# Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.
#
# The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
#
#
# Example 1:
#
# Input: s = "NWSE", k = 1
#
# Output: 3
#
# Explanation:
#
# Change s[2] from 'S' to 'N'. The string s becomes "NWNE".
#
# Movement	Position (x, y)	Manhattan Distance	Maximum
# s[0] == 'N'	(0, 1)	0 + 1 = 1	1
# s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
# s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
# s[3] == 'E'	(0, 2)	0 + 2 = 2	3
# The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.
#
# Example 2:
#
# Input: s = "NSWWEW", k = 3
#
# Output: 6
#
# Explanation:
#
# Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".
#
# The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# 0 <= k <= s.length
# s consists of only 'N', 'S', 'E', and 'W'.
# Solution
# Python O(N) O(1) Simulation Greedy
class Solution:
    output: int = 0
    def simulate_process(self, support_y: str, enemy_y: str, support_x: str, k: int, s: str) -> None:
        x: int = 0
        y: int = 0
        for move in s:
            if move == support_y: y += 1
            elif move == enemy_y:
                if k:
                    y += 1
                    k -= 1
                else: y -= 1
            elif move == support_x: x += 1
            else:
                if k:
                    x += 1
                    k -= 1
                else: x -= 1
            self.output = max(self.output, abs(x) + abs(y))

    def maxDistance(self, s: str, k: int) -> int:
        self.output = 0
        # common NE NW SE SW
        self.simulate_process('N', 'S', 'E', k, s)
        self.simulate_process('N', 'S', 'W', k, s)
        self.simulate_process('S', 'N', 'E', k, s)
        self.simulate_process('S', 'N', 'W', k, s)
        return self.output

# C++ O(N) O(1) Simulation Greedy
class Solution {
public:
    void simulateProcess(char supportY, char enemyY, char supportX, int &output, int &k, std::string &s) {
        int x = 0, y = 0, skipped = k;
        for (char &move : s) {
            if (move == supportY) ++y;
            else if (move == enemyY) {
                if (skipped) {
                    --skipped;
                    ++y;
                } else --y;
            }
            else if (move == supportX) ++x;
            else {
                if (skipped) {
                    --skipped;
                    ++x;
                } else --x;
            }
            output = std::max(output, std::abs(x) + std::abs(y));
        }
    }
    int maxDistance(string s, int k) {
        // common NE NW SE SW
        int output = 0;
        simulateProcess('N', 'S', 'E', output, k, s);
        simulateProcess('N', 'S', 'W', output, k, s);
        simulateProcess('S', 'N', 'E', output, k, s);
        simulateProcess('S', 'N', 'W', output, k, s);
        return output;
    }
};