# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left
# and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
#
# Example 1:
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
#
# Constraints:
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.
# Solution
class NumArray:
    def __init__(self, nums: List[int]):
        self.s = list(accumulate(nums, initial=0))
    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]

# Python O(N) O(N) Prefix Sum
class NumArray:

    def __init__(self, nums: List[int]) -> None:
        self.prefix_sum: list[int] = []
        current_sum: int = 0
        for num in nums:
            current_sum += num
            self.prefix_sum.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        left_sum: int = self.prefix_sum[left - 1] if left > 0 else 0
        right_sum: int = self.prefix_sum[right]
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# C++ O(N) O(N) Prefix Sum
class NumArray {
public:
    NumArray(vector<int>& nums) {
        int currentSum = 0;
        for (int num : nums) {
            currentSum += num;
            prefixSum.push_back(currentSum);
        }
    }

    int sumRange(int left, int right) {
        int leftSum = (left > 0 ? prefixSum[left - 1] : 0);
        int rightSum = prefixSum[right];
        return rightSum - leftSum;
    }
private:
    std::vector<int> prefixSum;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */