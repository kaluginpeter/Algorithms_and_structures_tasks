# You are given an integer array nums.
#
# A mirror pair is a pair of indices (i, j) such that:
#
# 0 <= i < j < nums.length, and
# reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
# Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).
#
# If no mirror pair exists, return -1.
#
#
#
# Example 1:
#
# Input: nums = [12,21,45,33,54]
#
# Output: 1
#
# Explanation:
#
# The mirror pairs are:
#
# (0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
# (2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
# The minimum absolute distance among all pairs is 1.
#
# Example 2:
#
# Input: nums = [120,21]
#
# Output: 1
#
# Explanation:
#
# There is only one mirror pair (0, 1) since reverse(nums[0]) = reverse(120) = 21 = nums[1].
#
# The minimum absolute distance is 1.
#
# Example 3:
#
# Input: nums = [21,120]
#
# Output: -1
#
# Explanation:
#
# There are no mirror pairs in the array.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109​​​​​​​
# Solution
# Python O(Nlog10(max(N))) O(N) Math HashMap
class Solution:
    def get_mirror(self, x: int) -> int:
        output: int = 0
        while x:
            output = output * 10 + x % 10
            x //= 10
        return output

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n: int = len(nums)
        seen: dict[int, int] = defaultdict(int)
        diff: int = -1
        for i in range(n):
            if nums[i] in seen:
                cur_diff: int = i - seen[nums[i]]
                if diff == -1 or diff > cur_diff:
                    diff = cur_diff
            seen[self.get_mirror(nums[i])] = i
        return diff

# C++ O(Nlog10(max(N))) O(N) HashMap Math
class Solution {
public:
    long long getMirror(int x) {
        long long output = 0;
        while (x) {
            output = output * 10 + x % 10;
            x /= 10;
        }
        return output;
    }

    int minMirrorPairDistance(vector<int>& nums) {
        size_t n = nums.size();
        std::unordered_map<long long, size_t> seen;
        size_t diff = 0;
        for (size_t i = 0; i < n; ++i) {
            if (seen.count(nums[i])) {
                size_t curDiff = i - seen[nums[i]];
                if (!diff || diff > curDiff) diff = curDiff;
            }
            long long revert = getMirror(nums[i]);
            seen[revert] = i;
        }
        return (diff ? diff : -1);
    }
};