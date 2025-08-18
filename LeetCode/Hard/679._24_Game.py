# You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.
#
# You are restricted with the following rules:
#
# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.
#
#
#
# Example 1:
#
# Input: cards = [4,1,8,7]
# Output: true
# Explanation: (8-4) * (7-1) = 24
# Example 2:
#
# Input: cards = [1,2,1,2]
# Output: false
#
#
# Constraints:
#
# cards.length == 4
# 1 <= cards[i] <= 9
# Solution
# Python O(4^N * N^2) O(1) Backtracking Math
class Solution:
    def backtrack(self, nums: list[float]) -> bool:
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6
        n: int = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                next_: list[float] = []
                for k in range(n):
                    if k != i and k != j: next_.append(nums[k])
                a: float = nums[i]
                b: float = nums[j]
                ops: list[float] = [a + b, a - b, b - a, a * b]
                if abs(a) > 1e-6: ops.append(b / a)
                if abs(b) > 1e-6: ops.append(a / b)
                for op in ops:
                    next_.append(op)
                    if self.backtrack(next_): return True
                    next_.pop()
        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        return self.backtrack(cards)

# C++ O(4^N * N^2) O(1) Backtracking Math
class Solution {
public:
    bool backtrack(std::vector<double>& nums) {
        if (nums.size() == 1) return std::fabs(nums[0] - 24.0) < 1e-6;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                std::vector<double> next;
                for (int k = 0; k < n; ++k) {
                    if (k != i && k != j) next.push_back(nums[k]);
                }
                double a = nums[i], b = nums[j];
                std::vector<double> ops = {a + b, a - b, b - a, a * b};
                if (std::fabs(b) > 1e-6) ops.push_back(a / b);
                if (std::fabs(a) > 1e-6) ops.push_back(b / a);
                for (double op : ops) {
                    next.push_back(op); // take
                    if (backtrack(next)) return true;
                    next.pop_back(); // not take
                }
            }
        }
        return false;
    }

    bool judgePoint24(std::vector<int>& cards) {
        std::vector<double> nums(cards.begin(), cards.end());
        return backtrack(nums);
    }
};