/*
You are given an integer array nums and an integer target.

Return the number of subarrays of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.



Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

nums[1..1] = [2]
nums[2..2] = [2]
nums[1..2] = [2,2]
nums[0..2] = [1,2,2]
nums[1..3] = [2,2,3]
So there are 5 such subarrays.

Example 2:

Input: nums = [1,1,1,1], target = 1

Output: 10

Explanation:

​​​​​​​All 10 subarrays have 1 as the majority element.

Example 3:

Input: nums = [1,2,3], target = 4

Output: 0

Explanation:

target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.



Constraints:

1 <= nums.length <= 10​​​​​​​5
1 <= nums[i] <= 10​​​​​​​9
1 <= target <= 109
*/
// Solution
// C++ O(NlogN) O(N) FenwickTree
class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        size_t n = nums.size();
        std::vector<int> prefix(n + 1, 0);
        for (size_t i = 0; i < n; ++i) prefix[i + 1] = prefix[i] + (nums[i] == target ? 1 : -1);
        std::vector<int> sPrefix = prefix;
        std::sort(sPrefix.begin(), sPrefix.end());
        sPrefix.erase(std::unique(sPrefix.begin(), sPrefix.end()), sPrefix.end());
        auto get_ = [&](int x) {
            return std::lower_bound(sPrefix.begin(), sPrefix.end(), x) - sPrefix.begin() + 1;
        };
        size_t m = sPrefix.size();
        std::vector<long long> FIT(m + 1, 0);
        auto upd = [&](size_t i) {
            while (i <= m) {
                ++FIT[i];
                i += i & -i;
            }
        };
        auto q = [&](size_t i) {
            long long out = 0;
            while (i > 0) {
                out += FIT[i];
                i -= i & -i;
            }
            return out;
        };
        long long output = 0;
        upd(get_(prefix[0]));
        for (size_t i = 1; i <= n; ++i) {
            size_t j = get_(prefix[i]);
            output += q(j - 1);
            upd(j);
        }
        return output;
    }
};