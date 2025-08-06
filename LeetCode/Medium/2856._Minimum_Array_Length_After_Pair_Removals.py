# Given an integer array num sorted in non-decreasing order.
#
# You can perform the following operation any number of times:
#
# Choose two indices, i and j, where nums[i] < nums[j].
# Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
# Return the minimum length of nums after applying the operation zero or more times.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
#
# Output: 0
#
# Explanation:
#
#
#
# Example 2:
#
# Input: nums = [1,1,2,2,3,3]
#
# Output: 0
#
# Explanation:
#
#
#
# Example 3:
#
# Input: nums = [1000000000,1000000000]
#
# Output: 2
#
# Explanation:
#
# Since both numbers are equal, they cannot be removed.
#
# Example 4:
#
# Input: nums = [2,3,4,4,4]
#
# Output: 1
#
# Explanation:
#
#
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# nums is sorted in non-decreasing order.
# Solution
# Python O(NlogN) O(N) PriorityQueue HashMap
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        hashmap: dict[int, int] = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        min_heap: list[tuple[int, int]] = []
        for num, freq in hashmap.items():
            heapq.heappush(min_heap, (-freq, num))
        output: int = len(nums)
        for left in nums:
            if not hashmap[left]: continue
            while min_heap and min_heap[0][1] <= left: heapq.heappop(min_heap)
            if not min_heap: break
            freq, right = heapq.heappop(min_heap)
            if freq + 1: heapq.heappush(min_heap, (freq + 1, right))
            output -= 2
            hashmap[left] -= 1
            hashmap[right] -= 1
        return output

# C++ O(NlogN) O(N) PriorityQueue HashMap
class Solution {
public:
    int minLengthAfterRemovals(vector<int>& nums) {
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
        std::unordered_map<int, int> hashmap;
        for (const int &num : nums) ++hashmap[num];
        for (const auto &p : hashmap) {
            minHeap.push({-p.second, p.first});
        }
        int output = nums.size();
        for (const int &left : nums) {
            if (!hashmap[left]) continue;
            while (!minHeap.empty() && minHeap.top().second <= left) minHeap.pop();
            if (minHeap.empty()) break;
            int freq = -minHeap.top().first, right = minHeap.top().second;
            minHeap.pop();
            if (freq - 1) minHeap.push({-(--freq), right});
            --hashmap[left];
            --hashmap[right];
            output -= 2;
        }
        return output;

    }
};

# Python O(N) O(1) TwoPointers
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        take: int = 0
        left: int = 0
        n: int = len(nums)
        right: int = n // 2
        while left < n // 2 and right < n:
            if nums[left] < nums[right]:
                left += 1
                take += 2
            right += 1
        return n - take

# C++ O(N) O(1) TwoPointers
class Solution {
public:
    int minLengthAfterRemovals(vector<int>& nums) {
        int take = 0, n = nums.size();
        int left = 0, middle = n / 2, right = middle;
        while (left < middle && right < n) {
            if (nums[left] < nums[right]) {
                ++left;
                take += 2;
            }
            ++right;
        }
        return n - take;
    }
};