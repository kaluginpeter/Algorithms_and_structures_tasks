# You are given a 0-indexed integer array nums consisting of 3 * n elements.
#
# You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:
#
# The first n elements belonging to the first part and their sum is sumfirst.
# The next n elements belonging to the second part and their sum is sumsecond.
# The difference in sums of the two parts is denoted as sumfirst - sumsecond.
#
# For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
# Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
# Return the minimum difference possible between the sums of the two parts after the removal of n elements.
#
#
#
# Example 1:
#
# Input: nums = [3,1,2]
# Output: -1
# Explanation: Here, nums has 3 elements, so n = 1.
# Thus we have to remove 1 element from nums and divide the array into two equal parts.
# - If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
# - If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
# - If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
# The minimum difference between sums of the two parts is min(-1,1,2) = -1.
# Example 2:
#
# Input: nums = [7,9,5,8,1,3]
# Output: 1
# Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
# If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
# To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
# It can be shown that it is not possible to obtain a difference smaller than 1.
#
#
# Constraints:
#
# nums.length == 3 * n
# 1 <= n <= 105
# 1 <= nums[i] <= 105
# Solution
# Python O(NlogN + N) O(N) PriorityQueue Prefix and Suffix Array
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n: int = len(nums) // 3
        prefix: list[int] = [float('inf')] * (n * 3)
        suffix: list[int] = [0] * (n * 3)
        cur_sum: int = 0
        min_heap: list[int] = []
        for i in range(n * 2):
            if len(min_heap) < n or -min_heap[0] > nums[i]:
                if len(min_heap) == n: cur_sum -= -heapq.heappop(min_heap)
                cur_sum += nums[i]
                heapq.heappush(min_heap, -nums[i])
            prefix[i] = cur_sum
        min_heap = []
        cur_sum = 0
        for i in range(n * 3 - 1, n - 1, -1):
            if len(min_heap) < n or min_heap[0] < nums[i]:
                if len(min_heap) == n: cur_sum -= heapq.heappop(min_heap)
                cur_sum += nums[i]
                heapq.heappush(min_heap, nums[i])
            suffix[i] = cur_sum
        output: int = float('inf')
        for i in range(n - 1, 2 * n + 1):
            if i - 1 > n - 1: output = min(output, prefix[i - 1] - suffix[i])
            if i + 1 < 2 * n: output = min(output, prefix[i] - suffix[i + 1])
        return output

# C++ O(NlogN + N) O(N) PriorityQueue Prefix and Suffix Array
class Solution {
public:
    long long minimumDifference(vector<int>& nums) {
        int n = nums.size() / 3;
        std::vector<long long> prefix(n * 3, INT64_MAX), suffix(n * 3, 0);
        std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
        long long curSum = 0;
        for (int i = 0; i < 2 * n; ++i) {
            if (minHeap.size() < n || -minHeap.top() > nums[i]) {
                if (minHeap.size() == n) {
                    curSum -= -minHeap.top();
                    minHeap.pop();
                }
                curSum += nums[i];
                minHeap.push(-nums[i]);
            }
            prefix[i] = curSum;
        }
        while (!minHeap.empty()) minHeap.pop();
        curSum = 0;
        for (int i = 3 * n - 1; i >= n; --i) {
            if (minHeap.size() < n || minHeap.top() < nums[i]) {
                if (minHeap.size() == n) {
                    curSum -= minHeap.top();
                    minHeap.pop();
                }
                curSum += nums[i];
                minHeap.push(nums[i]);
            }
            suffix[i] = curSum;
        }
        long long output = INT64_MAX;
        for (int i = n - 1; i <= n * 2; ++i) {
            if (i - 1 > n - 1) output = std::min(output, prefix[i - 1] - suffix[i]);
            if (i + 1 < n * 2) output = std::min(output, prefix[i] - suffix[i + 1]);
        }
        return output;
    }
};