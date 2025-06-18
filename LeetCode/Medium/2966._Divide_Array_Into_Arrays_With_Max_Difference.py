# You are given an integer array nums of size n and a positive integer k.
#
# Divide the array into one or more arrays of size 3 satisfying the following conditions:
#
# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.
#
#
#
# Example 1:
#
# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
# The difference between any two elements in each array is less than or equal to 2.
# Note that the order of elements is not important.
# Example 2:
#
# Input: nums = [1,3,3,2,7,3], k = 3
# Output: []
# Explanation: It is not possible to divide the array satisfying all the conditions.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 105
# n is a multiple of 3.
# 1 <= nums[i] <= 105
# 1 <= k <= 105
# Solution O(N log N) O(N)
class Solution(object):
    def divideArray(self, nums, k):
        if len(nums) < 3:
            return []
        nums.sort()
        l = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            else:
                l.append(nums[i:i+3])
        return l


# Python O(N * 1e5) O(1e5) CountingSort
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        hashmap: list[int] = [0] * 100001
        for num in nums: hashmap[num] += 1
        output: list[list[int]] = []
        chunk: list[int] = []
        num: int = 1
        while num < len(hashmap):
            if not hashmap[num]:
                num += 1
                continue
            if len(chunk) > 1 and num - chunk[0] > k:
                output.clear()
                return output
            chunk.append(num)
            if len(chunk) == 3:
                output.append(chunk)
                chunk = []
            hashmap[num] -= 1
        return output

# C++ O(N * 1e5) O(1e5) CountingSort
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        std::vector<int> hashmap(1e5 + 1, 0);
        for (int &num : nums) ++hashmap[num];
        std::vector<std::vector<int>> output;
        std::vector<int> chunk;
        int num = 1;
        while (num < hashmap.size()) {
            if (!hashmap[num]) {
                ++num;
                continue;
            };
            if (chunk.size() > 1 && num - chunk[0] > k) {
                output.clear();
                return output;
            }
            --hashmap[num];
            chunk.push_back(num);
            if (chunk.size() == 3) {
                output.push_back(chunk);
                chunk.clear();
            }
        }
        return output;
    }
};