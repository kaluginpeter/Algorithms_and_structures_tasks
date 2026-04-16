# You are given a circular array nums and an array queries.
#
# For each query i, you have to find the following:
#
# The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
# Return an array answer of the same size as queries, where answer[i] represents the result for query i.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]
#
# Output: [2,-1,3]
#
# Explanation:
#
# Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
# Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
# Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).
# Example 2:
#
# Input: nums = [1,2,3,4], queries = [0,1,2,3]
#
# Output: [-1,-1,-1,-1]
#
# Explanation:
#
# Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries.
#
#
#
# Constraints:
#
# 1 <= queries.length <= nums.length <= 105
# 1 <= nums[i] <= 106
# 0 <= queries[i] < nums.length
# Solution
# Python O(N + KlogN) O(N + K) HashMap BinarySearch
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        hashmap: dict[int, list[int]] = dict()
        n: int = len(nums)
        for i in range(n):
            if nums[i] not in hashmap: hashmap[nums[i]] = []
            hashmap[nums[i]].append(i)
        output: list[int] = [-1] * len(queries)
        for i in range(len(queries)):
            target: int = nums[queries[i]]
            if len(hashmap[target]) == 1: continue
            y: int = queries[i]
            idx: int = 0
            left: int = 0
            right: int = len(hashmap[target]) - 1

            while left <= right:
                middle: int = left + ((right - left) >> 1)
                if hashmap[target][middle] > y:
                    right = middle - 1
                elif hashmap[target][middle] < y:
                    left = middle + 1
                else:
                    idx = middle
                    break

            answer: int = float('inf')
            left_neighbor: int = idx - 1
            if left_neighbor < 0: left_neighbor = len(hashmap[target]) - 1
            right_neighbor: int = (idx + 1) % len(hashmap[target])

            if left_neighbor < idx:
                answer = min(answer, y - hashmap[target][left_neighbor])
                answer = min(answer, n - y + hashmap[target][left_neighbor])
            else:
                answer = min(answer, hashmap[target][left_neighbor] - y)
                answer = min(answer, n - hashmap[target][left_neighbor] + y)

            if right_neighbor < idx:
                answer = min(answer, y - hashmap[target][right_neighbor])
                answer = min(answer, n - y + hashmap[target][right_neighbor])
            else:
                answer = min(answer, hashmap[target][right_neighbor] - y)
                answer = min(answer, n - hashmap[target][right_neighbor] + y)

            output[i] = answer
        return output

# C++ O(N + KlogN) O(N + K) HashMap BinarySearch
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        unordered_map<int, vector<int>> hashmap;
        for (int i = 0; i < n; ++i) {
            hashmap[nums[i]].push_back(i);
        }
        vector<int> output (queries.size(), -1);
        for (int i = 0; i < queries.size(); ++i) {
            int target = queries[i];
            if (hashmap[nums[target]].size() == 1) continue;
            int left = 0;
            int right = hashmap[nums[target]].size() - 1;
            int idx = 0;
            while (left <= right) {
                int middle = left + ((right - left) >> 1);
                if (hashmap[nums[target]][middle] > target) right = middle - 1;
                else if (hashmap[nums[target]][middle] < target) left = middle + 1;
                else {
                    idx = middle;
                    break;
                }
            }
            int leftNeighbor = idx - 1;
            if (leftNeighbor < 0) leftNeighbor = hashmap[nums[target]].size() - 1;
            int rightNeighbor = (idx + 1) % hashmap[nums[target]].size();
            int answer = n;

            if (leftNeighbor < idx) {
                answer = min(answer, n - target + hashmap[nums[target]][leftNeighbor]);
                answer = min(answer, target - hashmap[nums[target]][leftNeighbor]);
            } else {
                answer = min(answer, n - hashmap[nums[target]][leftNeighbor] + target);
                answer = min(answer, hashmap[nums[target]][leftNeighbor] - target);
            }
            if (rightNeighbor < idx) {
                answer = min(answer, n - target + hashmap[nums[target]][rightNeighbor]);
                answer = min(answer, target - hashmap[nums[target]][rightNeighbor]);
            } else {
                answer = min(answer, n - hashmap[nums[target]][rightNeighbor] + target);
                answer = min(answer, hashmap[nums[target]][rightNeighbor] - target);
            }
            output[i] = answer;
        }
        return output;
    }
};


# Python O(N + M + MlogN) O(N + M) BinarySearch HashMap
class Solution:
    def get_index(self, series: list[int], target: int) -> int:
        left: int = 0
        right: int = len(series) - 1
        while left < right:
            middle: int = left + ((right - left) >> 1)
            if series[middle] == target: return middle
            elif series[middle] < target: left = middle + 1
            else: right = middle - 1
        return left

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n: int = len(nums)
        m: int = len(queries)
        seen: dict[int, list[int]] = defaultdict(list)
        for i in range(n): seen[nums[i]].append(i)
        output: list[int] = [-1] * m
        for j in range(m):
            i: int = queries[j]
            if i >= n or len(seen[nums[i]]) == 1: continue
            k: int = self.get_index(seen[nums[i]], i)
            left_dist: int = (i - seen[nums[i]][k - 1]) if k else (i + (n - seen[nums[i]][-1]))
            right_dist: int = (seen[nums[i]][k + 1] - i) if k + 1 != len(seen[nums[i]]) else ((n - i) + seen[nums[i]][0])
            output[j] = min(left_dist, right_dist)
        return output

# C++ O(N + M + MlogN) O(N + M) HashMap BinarySearch
class Solution {
public:
    size_t getIndex(std::vector<size_t>& series, size_t& target) {
        size_t left = 0, right = series.size() - 1;
        while (left < right) {
            size_t middle = left + ((right - left) >> 1);
            if (series[middle] == target) return middle;
            else if (series[middle] < target) left = middle + 1;
            else right = middle - 1;
        }
        return left;
    }
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        size_t n = nums.size(), m = queries.size();
        std::unordered_map<int, std::vector<size_t>> seen;
        for (size_t i = 0; i < n; ++i) seen[nums[i]].push_back(i);
        std::vector<int> output(m, -1);
        for (size_t j = 0; j < m; ++j) {
            size_t i = queries[j];
            if (j >= n || seen[nums[i]].size() == 1) continue;
            size_t k = getIndex(seen[nums[i]], i);
            int leftDist = (
                k ?
                i - seen[nums[i]][k - 1]
                : i + (n - seen[nums[i]].back())
            );
            int rightDist = (
                k + 1 != seen[nums[i]].size() ?
                seen[nums[i]][k + 1] - i
                : (n - i) + seen[nums[i]][0]
            );
            output[j] = std::min(leftDist, rightDist);
        }
        return output;
    }
};