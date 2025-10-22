# You are given an integer array nums and two integers k and numOperations.
#
# You must perform an operation numOperations times on nums, where in each operation you:
#
# Select an index i that was not selected in any previous operations.
# Add an integer in the range [-k, k] to nums[i].
# Return the maximum possible frequency of any element in nums after performing the operations.
#
#
#
# Example 1:
#
# Input: nums = [1,4,5], k = 1, numOperations = 2
#
# Output: 2
#
# Explanation:
#
# We can achieve a maximum frequency of two by:
#
# Adding 0 to nums[1], after which nums becomes [1, 4, 5].
# Adding -1 to nums[2], after which nums becomes [1, 4, 4].
# Example 2:
#
# Input: nums = [5,11,20,20], k = 5, numOperations = 1
#
# Output: 2
#
# Explanation:
#
# We can achieve a maximum frequency of two by:
#
# Adding 0 to nums[1].
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k <= 109
# 0 <= numOperations <= nums.length
# Solution
# C++ O(NlogN) O(N) Sorting BinarySearch
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        std::sort(nums.begin(), nums.end());
        std::unordered_map<int, int> numCount;
        std::set<int> modes;
        auto addMode = [&](int value) {
            modes.insert(value);
            if (value - k >= nums.front()) modes.insert(value - k);
            if (value + k <= nums.back()) modes.insert(value + k);
        };

        int output = 0, lastNumIndex = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != nums[lastNumIndex]) {
                numCount[nums[lastNumIndex]] = i - lastNumIndex;
                output = std::max(output, i - lastNumIndex);
                addMode(nums[lastNumIndex]);
                lastNumIndex = i;
            }
        }
        numCount[nums[lastNumIndex]] = nums.size() - lastNumIndex;
        output = std::max(output, static_cast<int>(nums.size()) - lastNumIndex);
        addMode(nums[lastNumIndex]);
        auto leftBound = [&](int value) {
            int left = 0, right = nums.size() - 1;
            while (left < right) {
                int mid = (left + right) / 2;
                if (nums[mid] < value) left = mid + 1;
                else right = mid;
            }
            return left;
        };
        auto rightBound = [&](int value) {
            int left = 0, right = nums.size() - 1;
            while (left < right) {
                int mid = (left + right + 1) / 2;
                if (nums[mid] > value) right = mid - 1;
                else left = mid;
            }
            return left;
        };

        for (int mode : modes) {
            int l = leftBound(mode - k);
            int r = rightBound(mode + k);
            int tmp = 0;
            if (numCount.count(mode)) tmp = std::min(r - l + 1, numCount[mode] + numOperations);
            else tmp = std::min(r - l + 1, numOperations);
            output = std::max(output, tmp);
        }
        return output;
    }
};