# You are given an array nums of n integers and two integers k and x.
#
# The x-sum of an array is calculated by the following procedure:
#
# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
#
# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
#
# Output: [6,10,12]
#
# Explanation:
#
# For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
# For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
# For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
# Example 2:
#
# Input: nums = [3,8,7,8,7,5], k = 2, x = 2
#
# Output: [11,15,15,15,12]
#
# Explanation:
#
# Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].
#
#
#
# Constraints:
#
# nums.length == n
# 1 <= n <= 105
# 1 <= nums[i] <= 109
# 1 <= x <= k <= nums.length
# Solution
# C++ O((N - K + 1)(logK + logX)) O(K + X + (N - K + 1)) Set Greedy
class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        std::unordered_map<int, int> hashmap;
        std::set<std::pair<int, int>> window, extra;
        std::vector<long long> output;
        long long xSum = 0;
        for (size_t i = 0; i < nums.size(); ++i) {
            if (i >= k) {
                --hashmap[nums[i - k]];
                std::pair<int, int> tmp = {hashmap[nums[i - k]] + 1, nums[i - k]};
                if (window.count(tmp)) {
                    window.erase(tmp);
                    window.insert({hashmap[nums[i - k]], nums[i - k]});
                    xSum -= nums[i - k];
                } else {
                    extra.erase(tmp);
                    extra.insert({hashmap[nums[i - k]], nums[i - k]});
                }
            }
            ++hashmap[nums[i]];
            std::pair<int, int> tmp = {hashmap[nums[i]] - 1, nums[i]};
            if (window.count(tmp)) {
                xSum += nums[i];
                window.erase(tmp);
                window.insert({hashmap[nums[i]], nums[i]});
            } else if (window.size() < x) {
                window.insert({hashmap[nums[i]], nums[i]});
                xSum += nums[i];
            } else {
                if (extra.count(tmp)) extra.erase(tmp);
                extra.insert({hashmap[nums[i]], nums[i]});
                std::set<std::pair<int, int>>::iterator windowLeast = window.begin();
                std::set<std::pair<int, int>>::iterator extraMost = std::prev(extra.end());
                if (
                    (extraMost->first > windowLeast->first)
                    || (extraMost->first == windowLeast->first && extraMost->second > windowLeast->second)
                ) {
                    int freq = windowLeast->first, num = windowLeast->second;
                    xSum -= static_cast<long long>(freq) * num;
                    window.erase(*windowLeast);
                    window.insert(*extraMost);
                    xSum += static_cast<long long>(extraMost->first) * extraMost->second;
                    extra.erase(*extraMost);
                    extra.insert({freq, num});
                }
            }
            if (extra.size()) {
                std::set<std::pair<int, int>>::iterator windowLeast = window.begin();
                std::set<std::pair<int, int>>::iterator extraMost = std::prev(extra.end());
                if (
                    (extraMost->first > windowLeast->first)
                    || (extraMost->first == windowLeast->first && extraMost->second > windowLeast->second)
                ) {
                    int freq = windowLeast->first, num = windowLeast->second;
                    xSum -= static_cast<long long>(freq) * num;
                    window.erase(*windowLeast);
                    window.insert(*extraMost);
                    xSum += static_cast<long long>(extraMost->first) * extraMost->second;
                    extra.erase(*extraMost);
                    extra.insert({freq, num});
                }
            }
            if (i + 1 >= k) output.push_back(xSum);
        }
        return output;
    }
};