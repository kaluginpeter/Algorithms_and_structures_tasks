# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
#
# Return any such subsequence as an integer array of length k.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: nums = [2,1,3,3], k = 2
# Output: [3,3]
# Explanation:
# The subsequence has the largest sum of 3 + 3 = 6.
# Example 2:
#
# Input: nums = [-1,-2,3,4], k = 3
# Output: [-1,3,4]
# Explanation:
# The subsequence has the largest sum of -1 + 3 + 4 = 6.
# Example 3:
#
# Input: nums = [3,4,3,3], k = 2
# Output: [3,4]
# Explanation:
# The subsequence has the largest sum of 3 + 4 = 7.
# Another possible subsequence is [4, 3].
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# -105 <= nums[i] <= 105
# 1 <= k <= nums.length
# Solution
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = sorted(enumerate(nums), key=lambda x: x[1])[-k:]
        return [v for k, v in sorted(ans)]


# Python O(N + KlogK + K) O(K) PriorityQueue
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap: list[tuple[int, int]] = []
        for i in range(len(nums)):
            if len(min_heap) < k or min_heap[0][0] < nums[i]:
                if len(min_heap) == k: heapq.heappop(min_heap)
                heapq.heappush(min_heap, (nums[i], i))
        min_heap.sort(key=lambda pair: pair[1])
        return [pair[0] for pair in min_heap]

# C++ O(N + KlogK + K) O(K) PriorityQueue
class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
        for (int i = 0; i < nums.size(); ++i) {
            if (minHeap.size() < k || minHeap.top().first < nums[i]) {
                if (minHeap.size() == k) minHeap.pop();
                minHeap.push({nums[i], i});
            }
        }
        std::vector<std::pair<int, int>> candidates;
        for (int i = 0; i < k; ++i) {
            candidates.push_back(minHeap.top());
            minHeap.pop();
        }
        std::sort(candidates.begin(), candidates.end(), [](const std::pair<int, int> &x, const std::pair<int, int> &y){
            return x.second < y.second;
        });
        std::vector<int> output;
        for (int i = 0; i < k; ++i) output.push_back(candidates[i].first);
        return output;
    }
};