# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
#
# Return the length of the shortest subarray to remove.
#
# A subarray is a contiguous subsequence of the array.
#
#
#
# Example 1:
#
# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
# Example 2:
#
# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
# Example 3:
#
# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any elements.
#
#
# Constraints:
#
# 1 <= arr.length <= 105
# 0 <= arr[i] <= 109
# Solution C++ O(N) O(1) Two Pointers
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size();
        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) {
            --right;
        }
        int minSubLength = right;
        int left = 0;
        while (left < right && (left == 0 || arr[left - 1] <= arr[left])) {
            while (right < n && arr[left] > arr[right]) {
                ++right;
            }
            minSubLength = std::min(minSubLength, right - left - 1);
            ++left;
        }
        return minSubLength;
    }
};

# Python O(N) O(1) Two Pointers
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n: int = len(arr)
        right: int = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        min_sub_length: int = right
        left: int = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < n and arr[left] > arr[right]:
                right += 1
            min_sub_length = min(min_sub_length, right - left - 1)
            left += 1
        return min_sub_length