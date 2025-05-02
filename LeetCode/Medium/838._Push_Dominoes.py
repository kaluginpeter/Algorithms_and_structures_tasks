# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
#
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
#
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
#
# You are given a string dominoes representing the initial state where:
#
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.
#
#
#
# Example 1:
#
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
# Example 2:
#
#
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
#
#
# Constraints:
#
# n == dominoes.length
# 1 <= n <= 105
# dominoes[i] is either 'L', 'R', or '.'.
# Solution
# Python O(N) O(N*) SlidingWindow
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        output: list[str] = list(dominoes)
        prev_right: int = -1
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                if prev_right == -1:
                    prev_right = i
                    continue
                for j in range(prev_right + 1, i): output[j] = 'R'
                prev_right = i
            elif dominoes[i] == 'L':
                if prev_right == -1:
                    j: int = i - 1
                    while j >= 0 and dominoes[j] == '.':
                        output[j] = 'L'
                        j -= 1
                    continue
                left: int = prev_right + 1
                right: int = i - 1
                while left < right:
                    output[left] = 'R'
                    output[right] = 'L'
                    left += 1
                    right -= 1
                prev_right = -1
        if prev_right != -1:
            for i in range(prev_right, len(dominoes)): output[i] = 'R'
        return ''.join(output)

# C++ O(N) O(1) SlidingWindow
class Solution {
public:
    string pushDominoes(string dominoes) {
        int prevRight = -1, n = dominoes.size();
        for (int i = 0; i < n; ++i) {
            if (dominoes[i] == 'R') {
                if (prevRight == -1) {
                    prevRight = i;
                    continue;
                }
                for (int j = prevRight; j < i; ++j) {
                    dominoes[j] = 'R';
                }
                prevRight = i;
            } else if (dominoes[i] == 'L') {
                if (prevRight == -1) {
                    int j = i - 1;
                    while (j >= 0 && dominoes[j] == '.') {
                        dominoes[j] = 'L';
                        --j;
                    }
                } else {
                    int left = prevRight + 1;
                    int right = i - 1;
                    while (left < right) {
                        dominoes[left] = 'R';
                        dominoes[right] = 'L';
                        ++left;
                        --right;
                    }
                    prevRight = -1;
                }
            }
        }
        if (prevRight != -1) {
            for (int i = prevRight; i < n; ++i) dominoes[i] = 'R';
        }
        return dominoes;
    }
};