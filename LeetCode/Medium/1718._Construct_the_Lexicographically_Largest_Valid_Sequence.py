# Given an integer n, find a sequence that satisfies all of the following:
#
# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.
#
# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.
#
# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
# Example 2:
#
# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]
#
#
# Constraints:
#
# 1 <= n <= 20
# Solution
# Python O(N!) O(N) Backtracking
class Solution:
    def backtrack(
        self, start: int, used: list[bool], output: list[int], n: int
    ) -> bool:
        if start == len(output): return True
        if output[start]: return self.backtrack(start + 1, used, output, n)
        for num in range(n, 0, -1):
            if used[num]: continue
            used[num] = True
            output[start] = num
            if num == 1:
                if self.backtrack(start + 1, used, output, n): return True
            elif start + num < len(output) and not output[start + num]:
                output[start + num] = num
                if self.backtrack(start + 1, used, output, n): return True
                output[start + num] = 0
            output[start] = 0
            used[num] = False
        return False

    def constructDistancedSequence(self, n: int) -> List[int]:
        bound: int = n * 2 - 1
        output: list[int] = [0] * bound
        used: list[bool] = [False] * (n + 1)
        length: int = 0
        self.backtrack(length, used, output, n)
        return output

# C++ O(!N) O(N) Backtracking
class Solution {
public:
    bool backtrack(int start, std::vector<int>& output, std::vector<bool>& used, int& n) {
        if (start == output.size()) return true;
        if (output[start]) return backtrack(start + 1, output, used, n);
        for (int num = n; num > 0; --num) {
            if (used[num]) continue;
            used[num] = true;
            output[start] = num;
            if (num == 1) {
                if (backtrack(start + 1, output, used, n)) return true;
            }
            else if ((start + num < output.size()) && (!output[start + num])) {
                output[start + num] = num;
                if (backtrack(start + 1, output, used, n)) return true;
                output[start + num] = 0;
            }
            output[start] = 0;
            used[num] = false;
        }
        return false;
    }

    vector<int> constructDistancedSequence(int n) {
        int bound = n * 2 - 1;
        std::vector<int> output (bound, 0);
        std::vector<bool> used (n + 1, false);
        int start = 0;
        backtrack(start, output, used, n);
        return output;
    }
};