/*
You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

 

Example 1:

Input: nums = [1,2,3]

Output: 12

Explanation:

A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = 22 - 12 + 32 = 4 - 1 + 9 = 12

Example 2:

Input: nums = [1,-1,2,-2,3,-3]

Output: 16

Explanation:

A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16

 

Constraints:

1 <= nums.length <= 105
-4 * 104 <= nums[i] <= 4 * 104
*/
// Solution
// C++ O(NlogN) O(1) Greedy TwoPointers
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        for (int& num : nums) num *= (num <= 0 ? -1 : 1);
        std::sort(nums.begin(), nums.end());
        long long output = 0;
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            output += std::pow(static_cast<long long>(nums[right]), 2LL);
            if (left == right) break;
            output -= std::pow(static_cast<long long>(nums[left]), 2LL);
            ++left;
            --right;
        }
        return output;
    }
};

// Go O(NlogN) O(1) TwoPointers Greedy
import "slices"
func maxAlternatingSum(nums []int) int64 {
    for i := 0; i < len(nums); i++ {
        if nums[i] < 0 { nums[i] *= -1 }
    }
    slices.Sort(nums)
    var left, right int = 0, len(nums) - 1
    var output int64 = 0
    for left < right {
        output += int64(nums[right] * nums[right]) - int64(nums[left] * nums[left])
        left++
        right--
    }
    if len(nums) & 1 == 1 { output += int64(nums[right] * nums[right]) }
    return output
}