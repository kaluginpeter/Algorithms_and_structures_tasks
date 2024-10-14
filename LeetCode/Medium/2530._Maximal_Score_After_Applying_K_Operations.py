# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
#
# In one operation:
#
# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.
#
# The ceiling function ceil(val) is the least integer greater than or equal to val.
#
#
#
# Example 1:
#
# Input: nums = [10,10,10,10,10], k = 5
# Output: 50
# Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
# Example 2:
#
# Input: nums = [1,10,3,3,3], k = 3
# Output: 17
# Explanation: You can do the following operations:
# Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
# Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
# Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
# The final score is 10 + 4 + 3 = 17.
#
#
# Constraints:
#
# 1 <= nums.length, k <= 105
# 1 <= nums[i] <= 109
# Solution
# Python O(NlogN + KlogN) O(N) Heap Priority Queue Greedy
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap: list[int] = []
        for num in nums:
            heapq.heappush(heap, -num)
        score: int = 0
        for _ in range(k):
            current_move: int = -heapq.heappop(heap)
            score += current_move
            heapq.heappush(heap, -math.ceil(current_move / 3))
        return score

# C++ O(NlogN + KlogN) O(N) Heap Greedy Priority Queue
class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        std::priority_queue<int, std::vector<int>> max_heap;
        for (int num : nums) {
            max_heap.push(num);
        }
        long long score = 0;
        for (int move = 0; move < k; ++move) {
            int current_num = max_heap.top();
            max_heap.pop();
            score += current_num;
            max_heap.push((current_num % 3 == 0 ? current_num / 3 : current_num / 3 + 1));
        }
        return score;
    }
};