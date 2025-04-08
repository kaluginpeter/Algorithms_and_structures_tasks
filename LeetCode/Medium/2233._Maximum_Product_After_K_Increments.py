# You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.
#
# Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo.
#
#
#
# Example 1:
#
# Input: nums = [0,4], k = 5
# Output: 20
# Explanation: Increment the first number 5 times.
# Now nums = [5, 4], with a product of 5 * 4 = 20.
# It can be shown that 20 is maximum product possible, so we return 20.
# Note that there may be other ways to increment nums to have the maximum product.
# Example 2:
#
# Input: nums = [6,3,3,2], k = 2
# Output: 216
# Explanation: Increment the second number 1 time and increment the fourth number 1 time.
# Now nums = [6, 4, 3, 3], with a product of 6 * 4 * 3 * 3 = 216.
# It can be shown that 216 is maximum product possible, so we return 216.
# Note that there may be other ways to increment nums to have the maximum product.
#
#
# Constraints:
#
# 1 <= nums.length, k <= 105
# 0 <= nums[i] <= 106
# Solution
# Python O(NlogN) O(N) PriorityQueue Greedy
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        min_heap: list[int] = []
        for num in nums: heapq.heappush(min_heap, num)
        for _ in range(k):
            num: int = heapq.heappop(min_heap)
            heapq.heappush(min_heap, num + 1)
        output: int = 1
        MOD: int = 1000000007
        while min_heap:
            output = output * heapq.heappop(min_heap) % MOD
        return output

# C++ O(NlogN) O(N) PriorityQueue Greedy
class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap (nums.begin(), nums.end());
        for (int i = 0; i < k; ++i) {
            int num = minHeap.top();
            minHeap.pop();
            ++num;
            minHeap.push(num);
        }
        long long MOD = 1000000007;
        long long output = 1;
        while (!minHeap.empty()) {
            output = output * static_cast<long long>(minHeap.top()) % MOD;
            minHeap.pop();
        }
        return static_cast<int>(output);
    }
};