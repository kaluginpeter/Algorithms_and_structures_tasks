/*
You are given an integer array nums.

The low score of nums is the minimum absolute difference between any two integers.
The high score of nums is the maximum absolute difference between any two integers.
The score of nums is the sum of the high and low scores.
Return the minimum score after changing two elements of nums.

 

Example 1:

Input: nums = [1,4,7,8,5]

Output: 3

Explanation:

Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
The low score is the minimum absolute difference: |6 - 6| = 0.
The high score is the maximum absolute difference: |8 - 5| = 3.
The sum of high and low score is 3.
Example 2:

Input: nums = [1,4,3]

Output: 0

Explanation:

Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
The sum of maximum absolute difference and minimum absolute difference is 0.
 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 109
*/
// Solution
// C++ O(NlogN) O(1) Sorting Greedy
class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        size_t n = nums.size();
        // First case: transform two biggest
        // Since both biggest integers will be transformed equally
        // the minimal difference will be zero
        int output = nums[n - 3] - nums[0];
        // Second case: transform two smallest
        output = std::min(output, nums[n - 1] - nums[2]);
        // Third case: transfrom one biggest and one smallest
        output = std::min(output, nums[n - 2] - nums[1]);
        return output;
    }
};

// We need to find a solution faster than or equal to O(NlogN)
// We can consider to try all possible "optimal" choices:
// Transfrom either: two biggest, two smallest, one biggest and one smallest
// And amongs all results choose the smallest one
// Go O(NlogN) O(1) Sorting Greedy
import "slices"
func minimizeSum(nums []int) int {
    slices.Sort(nums)
    var n int = len(nums)
    return min(nums[n - 3] - nums[0], nums[n - 1] - nums[2], nums[n - 2] - nums[1])
}