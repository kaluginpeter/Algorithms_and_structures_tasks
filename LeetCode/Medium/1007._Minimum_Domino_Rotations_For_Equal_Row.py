# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
#
# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
#
# If it cannot be done, return -1.
#
#
#
# Example 1:
#
#
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:
#
# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
#
#
# Constraints:
#
# 2 <= tops.length <= 2 * 104
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6
# Solution
# Python O(N) O(1) Greedy
class Solution:
    def check(self, target: int, tops: list[int], bottoms: list[int]) -> int:
        moves: int = 0
        for domino in range(len(tops)):
            if tops[domino] != target:
                if bottoms[domino] != target: return float('inf')
                moves += 1
        return moves

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        output: int = float('inf')
        for i in range(1, 6 + 1):
            output = min(output, self.check(i, tops, bottoms), self.check(i, bottoms, tops))
        return output if output != float('inf') else -1

# C++ O(N) O(1) Greedy
class Solution {
public:
    int check(int target, vector<int> &tops, vector<int> &bottoms) {
        int moves = 0;
        for (int domino = 0; domino < tops.size(); ++domino) {
            if (tops[domino] != target) {
                if (bottoms[domino] != target) return INT32_MAX;
                else ++moves;
            }
        }
        return moves;
    }

    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int output = INT32_MAX;
        for (int i = 1; i <= 6; ++i) {
            output = std::min(output, check(i, tops, bottoms));
            output = std::min(output, check(i, bottoms, tops));
        }
        return (output == INT32_MAX ? -1 : output);
    }
};