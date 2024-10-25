# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
#
# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation:
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7        3
#  1  3  -1  -3 [5  3  6] 7        5
#  1  3  -1  -3  5 [3  6  7]       6
# Example 2:
#
# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# Solution
# Python O(NlogK) O(N) SortedList(AVL-Tree)
from sortedcontainers import SortedList
class Solution:
    def find_median(self, storage: list[int]) -> float:
        n: int = len(storage)
        if n & 1:
            return storage[n // 2]
        return (storage[n // 2] + storage[n // 2 - 1]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        storage: list[int] = SortedList()
        for idx in range(k):
            storage.add(nums[idx])
        output: list[int] = []
        output.append(self.find_median(storage))
        for right in range(k, len(nums)):
            storage.discard(nums[right - k])
            storage.add(nums[right])
            output.append(self.find_median(storage))
        return output

# Python O(NlogK) O(N) Min & Max Heaps
class Solution:
    def find_median(self, small: list[tuple[int, int]], large: list[tuple[int, int]], k: int) -> float:
        if k & 1:
            return large[0][0]
        return (-1 * small[0][0] + large[0][0]) / 2

    def move(self, from_heap: list[tuple[int, int]], to_heap: list[tuple[int, int]]) -> None:
        pair: tuple[int, int] = heapq.heappop(from_heap)
        heapq.heappush(to_heap, (-pair[0], pair[1]))

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small: list[tuple[int, int]] = []
        large: list[tuple[int, int]] = []
        for idx in range(k):
            heapq.heappush(small, (-nums[idx], idx))
        for idx in range(k - (k >> 1)):
            self.move(small, large)
        output: list[int] = []
        output.append(self.find_median(small, large, k))
        for right in range(k, len(nums)):
            outgoing_idx: int = right - k
            if nums[right] >= large[0][0]:
                heapq.heappush(large, (nums[right], right))
                if nums[outgoing_idx] <= large[0][0]:
                    self.move(large, small)
            else:
                heapq.heappush(small, (-nums[right], right))
                if nums[outgoing_idx] >= large[0][0]:
                    self.move(small, large)

            while large and large[0][1] <= outgoing_idx:
                heapq.heappop(large)
            while small and small[0][1] <= outgoing_idx:
                heapq.heappop(small)
            output.append(self.find_median(small, large, k))
        return output