# You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).
#
# Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.
#
# Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.
#
#
#
# Example 1:
#
# Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# Output: 3
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 2 (0 + 1 >= 1)
# - Assign worker 1 to task 1 (3 >= 2)
# - Assign worker 2 to task 0 (3 >= 3)
# Example 2:
#
# Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# Output: 1
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 0 (0 + 5 >= 5)
# Example 3:
#
# Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
# Output: 2
# Explanation:
# We can assign the magical pills and tasks as follows:
# - Give the magical pill to worker 0 and worker 1.
# - Assign worker 0 to task 0 (0 + 10 >= 10)
# - Assign worker 1 to task 1 (10 + 10 >= 15)
# The last pill is not given because it will not make any worker strong enough for the last task.
#
#
# Constraints:
#
# n == tasks.length
# m == workers.length
# 1 <= n, m <= 5 * 104
# 0 <= pills <= m
# 0 <= tasks[i], workers[j], strength <= 109
# Solution
# Python O(NlogN + MlogM + log(min(N, M))NlogM) O(N) BinarySearch BinarySearchTree
class Solution:
    def binary_search(self, stock: list[int], task: int) -> int:
        output: int = -1
        left: int = 0
        right: int = len(stock) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if stock[middle] >= task:
                output = stock[middle]
                right = middle - 1
            else: left = middle + 1
        return output

    def check(self, middle: int, pills: int, tasks: list[int], stock: list[int], strength: int) -> bool:
        for i in range(middle - 1, -1, -1):
            if stock[-1] >= tasks[i]:
                stock.remove(stock[-1])
            else:
                if not pills: return False
                weakest_possible: int = self.binary_search(stock, tasks[i] - strength)
                if weakest_possible == -1: return False
                stock.remove(weakest_possible)
                pills -= 1
        return True

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        output: int = 0
        left: int = 1
        n, m = len(tasks), len(workers)
        right: int = min(n, m)
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            stock: list[int] = SortedList()
            for i in range(m - middle, m): stock.add(workers[i])
            if self.check(middle, pills, tasks, stock, strength):
                output = middle
                left = middle + 1
            else: right = middle - 1
        return output

# C++ O(NlogN + MlogM + log(min(N, M))NlogM) O(N) BinarySearch BinarySearchTree
class Solution {
public:
    bool check(int middle, int pills, multiset<int> &stock, vector<int> &tasks, int &strength) {
        for (int i = middle - 1; i >= 0; --i) {
            if (auto worker = prev(stock.end()); *worker >= tasks[i]) {
                stock.erase(worker);
            } else {
                if (!pills) return false;
                auto weakestPossible = stock.lower_bound(tasks[i] - strength);
                if (weakestPossible == stock.end()) return false;
                stock.erase(weakestPossible);
                --pills;
            }
        }
        return true;
    }

    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        int n = tasks.size(), m = workers.size();
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());
        int left = 1, right = min(n, m), output = 0;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            multiset<int> stock;
            for (int i = m - middle;i < m; ++i) stock.insert(workers[i]);
            if (check(middle, pills, stock, tasks, strength)) {
                output = middle;
                left = middle + 1;
            } else right = middle - 1;
        }
        return output;
    }
};