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