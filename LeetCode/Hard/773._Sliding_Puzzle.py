# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
#
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
#
# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
#
#
#
# Example 1:
#
#
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Example 2:
#
#
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Example 3:
#
#
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
#
#
# Constraints:
#
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# Each value board[i][j] is unique.
# Solution
# Python O(MN * (MN)!) O((MN)!) Breadth-First-Search Matrix
class Solution:
    directions: list[list[int]] = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [3, 5, 1],
        [4, 2],
    ]

    def _swap(self, s: str, i: int, j: int) -> str:
        s: list[str] = list(s)
        s[i], s[j] = s[j], s[i]
        return ''.join(s)

    def slidingPuzzle(self, board: List[List[int]]) -> int:

        target: str = '123450'
        start_state: str = ''.join(str(num) for row in board for num in row)
        seen: set[str] = set()
        queue: list[str] = deque([start_state])
        seen.add(start_state)
        steps: int = 0
        while queue:
            for _ in range(len(queue)):
                current_state: str = queue.popleft()
                if current_state == target:
                    return steps
                zero_index: int = current_state.index('0')
                for next_index in self.directions[zero_index]:
                    next_state: str = self._swap(current_state, zero_index, next_index)
                    if next_state in seen:
                        continue
                    seen.add(next_state)
                    queue.append(next_state)
            steps += 1
        return -1

# C++ O(MN * (MN)!) O((MN)!) Breadth-First-Search Matrix
class Solution {
public:
    void swap(std::string& state, int before, int after) {
        char temp = state[before];
        state[before] = state[after];
        state[after] = temp;
    }
    int slidingPuzzle(vector<vector<int>>& board) {
        std::vector<std::vector<int>> directions = {
            {1, 3},
            {0, 2, 4},
            {1, 5},
            {0, 4},
            {3, 5, 1},
            {4, 2},
        };
        std::string target = "123450";
        std::string startState = "";
        for (int row = 0; row < 2; ++row) {
            for (int col = 0; col < 3; ++col) {
                startState += std::to_string(board[row][col]);
            }
        }
        std::unordered_set<std::string> seen;
        seen.insert(startState);
        std::deque<std::string> queue;
        queue.push_back(startState);
        int moves = 0;
        while (queue.size()) {
            int n = queue.size();
            for (int rep = 0; rep < n; ++rep) {
                std::string currentState = queue.front();
                queue.pop_front();
                if (currentState == target) {
                    return moves;
                }
                int zeroIndex = static_cast<int>(currentState.find('0'));
                for (int nextIndex : directions[zeroIndex]) {
                    std::string nextState = currentState;
                    swap(nextState, zeroIndex, nextIndex);
                    if (seen.count(nextState)) {
                        continue;
                    }
                    seen.insert(nextState);
                    queue.push_back(nextState);
                }
            }
            ++moves;
        }
        return -1;
    }
};