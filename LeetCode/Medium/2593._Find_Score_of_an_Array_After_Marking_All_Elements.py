# You are given an array nums consisting of positive integers.
#
# Starting with score = 0, apply the following algorithm:
#
# Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score.
# Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.
#
#
#
# Example 1:
#
# Input: nums = [2,1,3,4,5,2]
# Output: 7
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
# - 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
# - 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
# Our score is 1 + 2 + 4 = 7.
# Example 2:
#
# Input: nums = [2,3,5,1,3,2]
# Output: 5
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
# - 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
# - 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
# Our score is 1 + 2 + 2 = 5.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# Solution
# Python O(NlogN) O(N) Bitmask
class Solution:
    def findScore(self, nums: List[int]) -> int:
        num_index: list[tuple[int, int]] = []
        n: int = len(nums)
        for idx in range(n):
            num_index.append((nums[idx], idx))
        num_index.sort()
        bitmask: list[bool] = [False] * n
        score: int = 0
        for main_idx in range(n):
            num, idx = num_index[main_idx]
            if bitmask[idx]: continue
            bitmask[max(idx - 1, 0)] = True
            bitmask[idx] = True
            bitmask[min(idx + 1, n - 1)] = True
            score += num
        return score

# C++ O(NlogN) O(N) Bitmask
class Solution {
public:
    long long findScore(vector<int>& nums) {
        int n = nums.size();
        long long score = 0;
        std::vector<std::pair<int, int>> numIndex;
        for (int idx = 0; idx < n; ++idx) {
            numIndex.push_back({nums[idx], idx});
        }
        std::sort(numIndex.begin(), numIndex.end());
        std::vector<bool> bitmask(n, false);
        for (std::pair<int, int>& p : numIndex) {
            if (bitmask[p.second]) {
                continue;
            }
            bitmask[std::max(p.second - 1, 0)] = true;
            bitmask[p.second] = true;
            bitmask[std::min(p.second + 1, n - 1)] = true;
            score += p.first;
        }
        return score;
    }
};

# Python O(NlogN) O(N) HashSet
class Solution:
    def findScore(self, nums: List[int]) -> int:
        num_index: list[tuple[int, int]] = []
        n: int = len(nums)
        for idx in range(n):
            num_index.append((nums[idx], idx))
        num_index.sort()
        hashset: set[int] = set()
        score: int = 0
        for main_idx in range(n):
            num, idx = num_index[main_idx]
            if idx in hashset: continue
            hashset.add(idx - 1)
            hashset.add(idx)
            hashset.add(idx + 1)
            score += num
        return score

# C++ O(N) O(N) HashSet
class Solution {
public:
    long long findScore(vector<int>& nums) {
        long long score = 0;
        int maxNum = 0;
        for (int& num : nums) {
            if (num > maxNum) {
                maxNum = num;
            }
        }
        std::vector<std::vector<int>> bucket(maxNum + 1);
        for (int idx = 0; idx < nums.size(); ++idx) {
            bucket[nums[idx]].push_back(idx);
        }
        std::unordered_set<int> hashset;
        int num = 0;
        while (num < maxNum + 1) {
            if (!bucket[num].empty()) {
                for (int& numIdx : bucket[num]) {
                    if (!hashset.count(numIdx)) {
                        score += num;
                        hashset.insert(numIdx - 1);
                        hashset.insert(numIdx);
                        hashset.insert(numIdx + 1);
                    }
                }
            }
            ++num;
        }
        return score;
    }
};

# Python O(NlogN) O(N) Min Heap
class Solution:
    def findScore(self, nums: List[int]) -> int:
        min_heap: list[tuple[int, int]] = []
        for idx in range(len(nums)):
            heapq.heappush(min_heap, (nums[idx], idx))
        score: int = 0
        hashset: set[int] = set()
        while min_heap:
            num, idx = heapq.heappop(min_heap)
            if idx in hashset: continue
            hashset.add(idx - 1)
            hashset.add(idx)
            hashset.add(idx + 1)
            score += num
        return score

# C++ O(NlogN) O(N) Min Heap
class Solution {
public:
    long long findScore(vector<int>& nums) {
        long long score = 0;
        std::unordered_set<int> hashset;
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
        for (int idx = 0; idx < nums.size(); ++idx) {
            minHeap.push({nums[idx], idx});
        }
        while (minHeap.size()) {
            int num = minHeap.top().first;
            int idx = minHeap.top().second;
            minHeap.pop();
            if (hashset.count(idx)) {
                continue;
            }
            hashset.insert(idx);
            hashset.insert(idx - 1);
            hashset.insert(idx + 1);
            score += num;
        }
        return score;
    }
};