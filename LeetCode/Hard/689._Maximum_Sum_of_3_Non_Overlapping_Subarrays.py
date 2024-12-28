# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.
#
# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Example 2:
#
# Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
# Output: [0,2,4]
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] < 216
# 1 <= k <= floor(nums.length / 3)
# Solution
# Python O(NM) O(NM) Dynamic Programming
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        k_sums: list[int] = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] - nums[i - k] + nums[i])
        dp: dict[tuple[int, int]] = dict()

        def get_max_sum(i: int, count: int) -> int:
            if i > len(nums) - k or count == 3:
                return 0
            if (i, count) in dp:
                return dp[(i, count)]
            include: int = k_sums[i] + get_max_sum(i + k, count + 1)
            skip: int = get_max_sum(i + 1, count)
            dp[(i, count)] = max(include, skip)
            return dp[(i, count)]

        def get_indices() -> list[int]:
            i: int = 0
            indices: list[int] = []
            while i <= len(nums) - k and len(indices) < 3:
                include: int = k_sums[i] + get_max_sum(i + k, len(indices) + 1)
                skip: int = get_max_sum(i + 1, len(indices))
                if include >= skip:
                    indices.append(i)
                    i += k
                else:
                    i += 1
            return indices

        return get_indices()

# C++ O(NM) O(NM) Dynamic Programming
struct TupleHash {
    template <typename T1, typename T2>
    std::size_t operator()(const std::tuple<T1, T2>& t) const {
        auto hash1 = std::hash<T1>{}(std::get<0>(t));
        auto hash2 = std::hash<T2>{}(std::get<1>(t));
        return hash1 ^ (hash2 << 1);
    }
};
class Solution {
public:
    int getMaxSum(int i, int count, std::vector<int>& nums, std::vector<int>& kSums, int& k, std::unordered_map<std::tuple<int, int>, int, TupleHash>& dp) {
        if ((i > nums.size() - k) || (count == 3)) {
            return 0;
        }
        if (dp.count({i, count})) {
            return dp[{i, count}];
        }
        int include = kSums[i] + getMaxSum(i + k, count + 1, nums, kSums, k, dp);
        int skip = getMaxSum(i + 1, count, nums, kSums, k, dp);
        dp[{i, count}] = std::max(include, skip);
        return dp[{i, count}];
    }
    std::vector<int> getIndices (std::vector<int>& nums, std::vector<int>& kSums, int& k, std::unordered_map<std::tuple<int, int>, int, TupleHash>& dp) {
        int i = 0;
        std::vector<int> indices;
        while ((i <= nums.size() - k) && (indices.size() < 3)) {
            int include = kSums[i] + getMaxSum(i + k, indices.size() + 1, nums, kSums, k, dp);
            int skip = getMaxSum(i + 1, indices.size(), nums, kSums, k, dp);
            if (include >= skip) {
                indices.push_back(i);
                i += k;
            } else {
                i += 1;
            }
        }
        return indices;
    }
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        std::vector<int> kSums;
        int curSum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (i < k) {
                curSum += nums[i];
                if (i == k - 1) {
                    kSums.push_back(curSum);
                }
            } else {
                kSums.push_back(kSums[kSums.size() - 1] - nums[i - k] + nums[i]);
            }
        }
        std::unordered_map<std::tuple<int, int>, int, TupleHash> dp;
        return getIndices(nums, kSums, k, dp);
    }
};