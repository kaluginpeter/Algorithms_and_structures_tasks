# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
#
# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.
# Return nums after the rearrangement.
#
#
#
# Example 1:
#
# Input: nums = [9,12,5,10,14,3,10], pivot = 10
# Output: [9,5,3,10,10,12,14]
# Explanation:
# The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
# The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
# The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
# Example 2:
#
# Input: nums = [-3,4,3,2], pivot = 2
# Output: [-3,2,4,3]
# Explanation:
# The element -3 is less than the pivot so it is on the left side of the array.
# The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
# The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -106 <= nums[i] <= 106
# pivot equals to an element of nums.
# Solution Partition O(N) O(N)
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot: list[int] = []
        equals_to_pivot: list[int] = []
        more_than_pivot: list[int] = []
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num > pivot:
                more_than_pivot.append(num)
            else:
                equals_to_pivot.append(num)
        return less_than_pivot + equals_to_pivot + more_than_pivot

# Python O(N) O(D + K) Two Pointers
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n: int = len(nums)
        less_than: list[int] = []
        greater_than: list[int] = []
        for num in nums:
            if num < pivot: less_than.append(num)
            elif num > pivot: greater_than.append(num)
        nums_idx: int = 0
        for i in range(len(less_than)):
            nums[nums_idx] = less_than[i]
            nums_idx += 1
        for i in range(n - len(less_than) - len(greater_than)):
            nums[nums_idx] = pivot
            nums_idx += 1
        for i in range(len(greater_than)):
            nums[nums_idx] = greater_than[i]
            nums_idx += 1
        return nums

# C++ O(N) O(D + K) Two Pointers
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size();
        vector<int> lessThan;
        vector<int> greaterThan;
        for (int i = 0; i < n; ++i) {
            if (nums[i] < pivot) {
                lessThan.push_back(nums[i]);
            } else if (nums[i] > pivot) {
                greaterThan.push_back(nums[i]);
            }
        }
        int numsIdx = 0;
        for (int i = 0; i < lessThan.size(); ++i) {
            nums[numsIdx] = lessThan[i];
            ++numsIdx;
        }
        for (int i = 0; i < n - greaterThan.size() - lessThan.size(); ++i) {
            nums[numsIdx] = pivot;
            ++numsIdx;
        }
        for (int i = 0; i < greaterThan.size(); ++i) {
            nums[numsIdx] = greaterThan[i];
            ++numsIdx;
        }
        return nums;
    }
};