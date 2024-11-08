# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#
#
# Constraints:
#
# 1 <= n <= 20
# 1 <= k <= n
# Solution O(k * 2**N) O(k * 2**N)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, current_comb):
            if len(current_comb) == k:
                all_comb.append(list(current_comb))
                return
            for i in range(start, n + 1):
                current_comb.append(i)
                backtrack(i+1, current_comb)
                current_comb.pop()
        all_comb = []
        backtrack(1, [])
        return all_comb

# Python O(k * 2**N) O(k * 2**N) Backtracking
class Solution:
    def helper(self, num: int, n: int, k: int, init: list[int], output: list[list[int]]) -> None:
        if len(init) == k:
            output.append(init.copy())
            return
        if num > n:
            return
        init.append(num)
        self.helper(num + 1, n, k, init, output)
        init.pop()
        self.helper(num + 1, n, k, init, output)

    def combine(self, n: int, k: int) -> List[List[int]]:
        output: list[list[int]] = []
        init: list[int] = []
        self.helper(1, n, k, init, output)
        return output

# C++ O(k * 2**N) O(k * 2**N) Backtracking
class Solution {
public:
    void helper(int num, int n, std::vector<int>& init, std::vector<std::vector<int>>& output, int k) {
        if (init.size() == k) {
            output.push_back(init);
            return;
        }
        if (num > n) {
            return;
        }
        init.push_back(num);
        helper(num + 1, n, init, output, k);
        init.pop_back();
        helper(num + 1, n, init, output, k);
    }
    vector<vector<int>> combine(int n, int k) {
        std::vector<std::vector<int>> output;
        std::vector<int> init;
        helper(1, n, init, output, k);
        return output;
    }
};

# Python O(k * C(n, k)) O(k * C(n, k)) Backtracking
class Solution:
    def helper(self, num: int, n: int, k: int, init: list[int], output: list[list[int]]) -> None:
        if len(init) == k:
            output.append(init.copy())
            return
        if num > n:
            return
        for next_num in range(num, n + 1):
            init.append(next_num)
            self.helper(next_num + 1, n, k, init, output)
            init.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        output: list[list[int]] = []
        init: list[int] = []
        self.helper(1, n, k, init, output)
        return output
# C++ O(k * C(n, k)) O(k * C(n, k)) Backtracking
class Solution {
public:
    void helper(int nextNum, int n, std::vector<int>& init, std::vector<std::vector<int>>& output, int k) {
        if (init.size() == k) {
            output.push_back(init);
            return;
        }
        if (nextNum > n) {
            return;
        }
        for (int num = nextNum; num < n + 1; ++num) {
            init.push_back(num);
            helper(num + 1, n, init, output, k);
            init.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        std::vector<std::vector<int>> output;
        std::vector<int> init;
        helper(1, n, init, output, k);
        return output;
    }
};