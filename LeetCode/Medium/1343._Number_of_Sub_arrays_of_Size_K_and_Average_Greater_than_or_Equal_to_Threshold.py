# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
#
#
#
# Example 1:
#
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Example 2:
#
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
#
#
# Constraints:
#
# 1 <= arr.length <= 105
# 1 <= arr[i] <= 104
# 1 <= k <= arr.length
# 0 <= threshold <= 104
# Solution
# Python O(N) O(1) Sliding Window
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        answer: int = 0
        left: int = 0
        current_sum: int = 0
        for right in range(len(arr)):
            if right - left + 1 > k:
                current_sum -= arr[left]
                left += 1
            current_sum += arr[right]
            if right - left + 1 == k:
                answer += current_sum / k >= threshold
        return answer
# C++ O(N) O(1) Sliding Window
class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int answer = 0;
        size_t left = 0;
        int current_sum = 0;
        for (size_t right = 0; right < arr.size(); ++right) {
            if (right - left + 1 > k) {
                current_sum -= arr[left];
                left += 1;
            }
            current_sum += arr[right];
            if (right - left + 1 == k) {
                answer += current_sum / k >= threshold;
            }
        }
        return answer;
    }
};