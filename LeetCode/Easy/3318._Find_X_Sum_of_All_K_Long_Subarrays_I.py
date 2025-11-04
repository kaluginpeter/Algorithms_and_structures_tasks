# You are given an array nums of n integers and two integers k and x.
#
# The x-sum of an array is calculated by the following procedure:
#
# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
#
# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the
# subarray
#  nums[i..i + k - 1].
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
# 1 <= n == nums.length <= 50
# 1 <= nums[i] <= 50
# 1 <= x <= k <= nums.length
# Solution
# Python O(NKlogK) O(N) HashMap Sorting Simulation
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans: list[int] = []
        for i in range(len(nums) - k + 1):
            hashmap: dict[int, int] = dict()
            for idx in range(i, i + k):
                hashmap[nums[idx]] = hashmap.get(nums[idx], 0) + 1
            sequence: list[int] = sorted(hashmap.keys(), key=lambda x: (hashmap[x], x), reverse=True)
            ans.append(sum(y * hashmap[y] for y in sequence[:x]))
        return ans



# Python O(ND + (N-K+1)(D+DlogD) + X) O(ND + X) PrefixArray HashMap Sorting
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        prefix_map: list[list[int]] = []
        hashmap: list[int] = [0] * 51
        prefix_map.append(hashmap.copy())
        for num in nums:
            hashmap[num] += 1
            prefix_map.append(hashmap.copy())
        n: int = len(nums)
        answer: list[int] = [0] * (n + 1 - k)
        for i in range(k, n + 1):
            dataset: list[tuple[int, int]] = []
            for j in range(51):
                rem_freq: int = prefix_map[i][j] - prefix_map[i - k][j]
                if rem_freq: dataset.append((rem_freq, j))
            dataset.sort(reverse=True)
            x_sum: int = sum(freq * num for freq, num in dataset[:min(x, len(dataset))])
            answer[i - k] = x_sum
        return answer

# C++ O(ND + (N-K+1)(D+DlogD) + X) O(ND + X) PrefixArray HashMap Sorting
class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        std::vector<std::vector<int>> prefixMap;
        std::vector<int> hashmap(51, 0);
        prefixMap.push_back(hashmap);
        for (int& num : nums) {
            ++hashmap[num];
            prefixMap.push_back(hashmap);
        }
        size_t n = nums.size();
        std::vector<int> answer(n + 1 - k, 0);
        for (size_t i = k; i <= n; ++i) {
            std::vector<std::pair<int, int>> dataset;
            for (int j = 0; j < 51; ++j) {
                int remFreq = prefixMap[i][j] - prefixMap[i - k][j];
                if (remFreq) dataset.push_back({j, remFreq});
            }
            std::sort(
                dataset.begin(),
                dataset.end(),
                [&](const std::pair<int, int>& x, const std::pair<int, int>& y) {
                    if (x.second != y.second) return x.second > y.second;
                    return x.first > y.first;
                }
            );
            int xSum = 0;
            for (size_t i = 0; i < std::min(static_cast<size_t>(x), dataset.size()); ++i) xSum += dataset[i].first * dataset[i].second;
            answer[i - k] = xSum;
        }
        return answer;
    }
};