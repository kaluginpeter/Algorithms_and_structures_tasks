# You are given two integer arrays, nums1 and nums2, both of length n, along with a positive integer k.
#
# For each index i from 0 to n - 1, perform the following:
#
# Find all indices j where nums1[j] is less than nums1[i].
# Choose at most k values of nums2[j] at these indices to maximize the total sum.
# Return an array answer of size n, where answer[i] represents the result for the corresponding index i.
#
#
#
# Example 1:
#
# Input: nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2
#
# Output: [80,30,0,80,50]
#
# Explanation:
#
# For i = 0: Select the 2 largest values from nums2 at indices [1, 2, 4] where nums1[j] < nums1[0], resulting in 50 + 30 = 80.
# For i = 1: Select the 2 largest values from nums2 at index [2] where nums1[j] < nums1[1], resulting in 30.
# For i = 2: No indices satisfy nums1[j] < nums1[2], resulting in 0.
# For i = 3: Select the 2 largest values from nums2 at indices [0, 1, 2, 4] where nums1[j] < nums1[3], resulting in 50 + 30 = 80.
# For i = 4: Select the 2 largest values from nums2 at indices [1, 2] where nums1[j] < nums1[4], resulting in 30 + 20 = 50.
# Example 2:
#
# Input: nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1
#
# Output: [0,0,0,0]
#
# Explanation:
#
# Since all elements in nums1 are equal, no indices satisfy the condition nums1[j] < nums1[i] for any i, resulting in 0 for all positions.
#
#
#
# Constraints:
#
# n == nums1.length == nums2.length
# 1 <= n <= 105
# 1 <= nums1[i], nums2[i] <= 106
# 1 <= k <= n
# Solution
# Python O(NlogN) O(N) Priority Queue Sorting
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n: int = len(nums1)
        orders: list[int] = sorted(range(n), key=lambda idx: (nums1[idx], nums2[idx]))
        min_heap: list[int] = []
        cur_sum: int = 0
        output: list[int] = [0] * n
        for i in range(n):
            idx: int = orders[i]
            if i and nums1[orders[i - 1]] == nums1[idx]:
                output[idx] = output[orders[i - 1]]
            else: output[idx] = cur_sum
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums2[idx])
                cur_sum += nums2[idx]
            elif min_heap[0] < nums2[idx]:
                cur_sum -= heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums2[idx])
                cur_sum += nums2[idx]
        return output

# C++ O(NlogN) O(N) PriorityQueue Sorting
vector<int> sortedIndices(const vector<int>& nums1, const vector<int>& nums2) {
    int n = nums1.size();
    vector<int> indices(n);
    for (int i = 0; i < n; ++i) {
        indices[i] = i;
    }
    sort(indices.begin(), indices.end(), [&](int a, int b) {
        if (nums1[a] != nums1[b]) {
            return nums1[a] < nums1[b];
        }
        return nums2[a] < nums2[b];
    });
    return indices;
}

class Solution {
public:
    vector<long long> findMaxSum(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<int> orders = sortedIndices(nums1, nums2);
        vector<long long> output (n, 0);
        priority_queue<int, vector<int>, greater<int>> minHeap;
        long long curSum = 0;
        for (int i = 0; i < n; ++i) {
            int idx = orders[i];
            if (i && nums1[orders[i - 1]] == nums1[idx]) {
                output[idx] = output[orders[i - 1]];
            } else output[idx] = curSum;
            if (minHeap.size() < k) {
                minHeap.push(nums2[idx]);
                curSum += (long long)nums2[idx];
            } else if (minHeap.top() < nums2[idx]) {
                curSum -= (long long)minHeap.top();
                minHeap.pop();
                minHeap.push(nums2[idx]);
                curSum += (long long)nums2[idx];
            }
        }
        return output;
    }
};