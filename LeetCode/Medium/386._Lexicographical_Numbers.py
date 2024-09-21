# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
#
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.
#
#
#
# Example 1:
#
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:
#
# Input: n = 2
# Output: [1,2]
#
#
# Constraints:
#
# 1 <= n <= 5 * 104
# Solution
# Python O(N) O(logN) Depth-First-Search
class Solution:
    def dfs(self, current: int, target: int, result: list[int]) -> None:
        if current > target:
            return
        if current > 0:
            result.append(current)
        for acc in range(10):
            if (current == 0 and acc == 0) or current * 10 + acc > target:
                continue
            self.dfs(current * 10 + acc, target, result)

    def lexicalOrder(self, n: int) -> List[int]:
        output: list[int] = []
        self.dfs(0, n, output)
        return output

# C++ O(N) O(logN) Depth-First-Search
class Solution {
public:
    void dfs(int current, int target, std::vector<int>& result) {
        if (current > target) {
            return;
        }
        if (current > 0) {
            result.push_back(current);
        }
        for (int acc = 0; acc < 10; ++acc) {
            if (
                (current == 0 && acc == 0) ||
                (current * 10 + acc > target)
            ) {
                continue;
            }
            dfs(current * 10 + acc, target, result);
        }
    }

    vector<int> lexicalOrder(int n) {
        std::vector<int> output = {};
        dfs(0, n, output);
        return output;
    }
};