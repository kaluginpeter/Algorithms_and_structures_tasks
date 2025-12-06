# You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.
#
# Return the total number of ways to partition nums under this condition.
#
# Since the answer may be too large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: nums = [9,4,1,3,7], k = 4
#
# Output: 6
#
# Explanation:
#
# There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:
#
# [[9], [4], [1], [3], [7]]
# [[9], [4], [1], [3, 7]]
# [[9], [4], [1, 3], [7]]
# [[9], [4, 1], [3], [7]]
# [[9], [4, 1], [3, 7]]
# [[9], [4, 1, 3], [7]]
# Example 2:
#
# Input: nums = [3,3,4], k = 0
#
# Output: 2
#
# Explanation:
#
# There are 2 valid partitions that satisfy the given conditions:
#
# [[3], [3], [4]]
# [[3, 3], [4]]
#
#
# Constraints:
#
# 2 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 109
# 0 <= k <= 109
# Solution
# Python O(N) O(N) PrefixSum
mod: int = 10**9 + 7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        dp: list[int] = [0] * (n + 1)
        prefix: list[int] = [0] * (n + 1)
        min_q: list[int] = deque()
        max_q: list[int] = deque()
        dp[0] = 1
        prefix[0] = 1
        j: int = 0
        for i in range(n):
            while max_q and nums[max_q[-1]] <= nums[i]: max_q.pop()
            max_q.append(i)
            while min_q and nums[min_q[-1]] >= nums[i]: min_q.pop()
            min_q.append(i)
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == j: max_q.popleft()
                if min_q[0] == j: min_q.popleft()
                j += 1
            if j > 0:
                dp[i + 1] = (prefix[i] - prefix[j - 1] + mod) % mod
            else:
                dp[i + 1] = prefix[i] % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod
        return dp[n]

# C++ O(N) O(N) Prefix
constexpr long long mod = 1000000007;
class Solution {
public:
    int countPartitions(vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<long long> dp(n + 1), prefix(n + 1);
        std::deque<int> minQ, maxQ;
        dp[0] = 1;
        prefix[0] = 1;
        for (int i = 0, j = 0; i < n; ++i) {
            while (!maxQ.empty() && nums[maxQ.back()] <= nums[i]) maxQ.pop_back();
            maxQ.push_back(i);
            while (!minQ.empty() && nums[minQ.back()] >= nums[i]) minQ.pop_back();
            minQ.push_back(i);
            while (!maxQ.empty() && !minQ.empty() &&
                   nums[maxQ.front()] - nums[minQ.front()] > k) {
                if (maxQ.front() == j) maxQ.pop_front();
                if (minQ.front() == j) minQ.pop_front();
                ++j;
            }
            dp[i + 1] = (prefix[i] - (j > 0 ? prefix[j - 1] : 0) + mod) % mod;
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod;
        }
        return dp[n];
    }
};