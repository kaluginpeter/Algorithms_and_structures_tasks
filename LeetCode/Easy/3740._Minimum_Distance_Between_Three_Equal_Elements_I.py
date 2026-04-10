# You are given an integer array nums.
#
# A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
#
# The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
#
# Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1,1,3]
#
# Output: 6
#
# Explanation:
#
# The minimum distance is achieved by the good tuple (0, 2, 3).
#
# (0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.
#
# Example 2:
#
# Input: nums = [1,1,2,3,2,1,2]
#
# Output: 8
#
# Explanation:
#
# The minimum distance is achieved by the good tuple (2, 4, 6).
#
# (2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.
#
# Example 3:
#
# Input: nums = [1]
#
# Output: -1
#
# Explanation:
#
# There are no good tuples. Therefore, the answer is -1.
#
#
#
# Constraints:
#
# 1 <= n == nums.length <= 100
# 1 <= nums[i] <= n
#
# Solution
# Python O(N) O(D) Hashing
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        seen: list[list[int]] = [[] for _ in range(101)]
        diff: int = float('inf')
        for i in range(len(nums)):
            if len(seen[nums[i]]) > 1:
                tmpdiff: int = (i - seen[nums[i]][-1]) + (i - seen[nums[i]][-2]) + (seen[nums[i]][-1] - seen[nums[i]][-2])
                if tmpdiff < diff: diff = tmpdiff
            seen[nums[i]].append(i)
        return diff if diff != float('inf') else -1

# C++ O(N) O(D) Hashing
class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        std::array<std::vector<size_t>, 101> seen{};
        size_t n = nums.size();
        int dist = 301;
        for (size_t i = 0; i < n; ++i) {
            if (seen[nums[i]].size() > 1) {
                size_t prev = seen[nums[i]].back();
                size_t prevPrev = *----(seen[nums[i]].end());
                int tmpDist = i - prev + (prev - prevPrev) + (i - prevPrev);
                if (tmpDist < dist) dist = tmpDist;
            }
            seen[nums[i]].push_back(i);
        }
        return (dist == 301 ? -1 : dist);
    }
};